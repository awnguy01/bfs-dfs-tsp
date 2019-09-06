"""
Project 2 TSP Search with BFS and DFS
@author Andrew Nguyen Vo
@copyright Copyright 2019, Andrew Nguyen Vo, All Rights Reserved
"""
from time import time
from typing import List, Callable

from next_node_map import DEST_NODE_NAME_MAP
from node import Node
from utils import get_file_path, calc_total_distance, find_min_route, print_list_of_routes, calc_elapsed_ts


def get_node_list(file_name: str) -> List[Node]:
    """Reads a TSP file and extracts list of nodes"""
    node_list: List[Node] = []
    with open(file_name) as f:
        for index, line in enumerate(f):
            if index > 6:
                sub_lines: List[str] = line.split(' ')
                node_name: str = str(sub_lines[0]).strip()
                x: float = sub_lines[1]
                y: float = sub_lines[2]
                new_node = Node(node_name, x, y)
                node_list.append(new_node)
        for node in node_list:
            dest_list: List[Node] = []
            # Destination nodes for each node retrieved from a hardcoded map
            for dest_name in DEST_NODE_NAME_MAP.get(node.name):
                for test_node in node_list:
                    if test_node.name == dest_name:
                        dest_list.append(test_node)
            node.dest_nodes = dest_list
    return node_list


def bfs(node_list: List[Node]) -> List[List[Node]]:
    """Modified iterative breadth first search to get list of possible routes"""
    all_routes: List[List[Node]] = [[node_list[0]]]
    queue: List[Node] = [node_list[0]]
    while len(queue):
        # De-queue algorithm characteristic of BFS
        curr_node = queue.pop(0)

        # Container for routes that end it the currently de-queued node
        affected_routes: List[List[Node]] = []

        for route_index, route in enumerate(all_routes):
            if route[-1] == curr_node:
                affected_routes.append(route)

                # Remove affected routes in this loop from final list to be replaced by the post-append routes
                del all_routes[route_index]

        # Append each destination node to each affected route and append to final list
        for dest in curr_node.dest_nodes:
            if dest != node_list[-1]:
                # Queue every destination to continue BFS until final destination is reached
                queue.append(dest)
            for aff_route in affected_routes:
                aff_route_copy = aff_route.copy()
                aff_route_copy.append(dest)
                all_routes.append(aff_route_copy)
    return all_routes


def dfs(node_list: List[Node]) -> List[List[Node]]:
    """Modified iterative depth first search to get list of possible routes"""
    all_routes: List[List[Node]] = [[node_list[0]]]
    stack: List[Node] = [node_list[0]]

    while len(stack):
        # Stack pop algorithm characteristic of DFS
        curr_node = stack.pop()

        # Container for routes that end in the currently popped node
        affected_routes: List[List[Node]] = []

        for route_index, route in enumerate(all_routes):
            if route[-1] == curr_node:
                affected_routes.append(route)

                # Remove affected routes in this loop from final list to be replaced by the post-append routes
                del all_routes[route_index]

        # Append each destination node to each affected route and append to final list
        for dest in curr_node.dest_nodes:
            if dest != node_list[-1]:
                # Push every destination to continue DFS until final destination is reached
                stack.append(dest)
            for aff_route in affected_routes:
                aff_route_copy = aff_route.copy()
                aff_route_copy.append(dest)
                all_routes.append(aff_route_copy)

    return all_routes


def print_results(node_list: List[Node], search_fn: Callable[[List[Node]], List[List[Node]]]) -> None:
    """Print results of each search function in a template format"""
    time_start: float = time()
    all_routes: List[List[Node]] = search_fn(node_list)
    time_elapsed: str = calc_elapsed_ts(time_start)
    if len(all_routes):
        min_route = find_min_route(all_routes)
        print(*map(lambda node: node.name, min_route), end=' = ')
        print(calc_total_distance(min_route))
    else:
        print('Search could not find any valid routes')

    print(f'Calculated in {time_elapsed}')


def main():
    file_name: str = get_file_path([('TSP File', '*.tsp')])
    if file_name is not None:
        node_list: List[Node] = get_node_list(file_name)

        # EXECUTE BREADTH FIRST SEARCH
        print_results(node_list, bfs)

        # EXECUTE DEPTH FIRST SEARCH
        print_results(node_list, dfs)


if __name__ == "__main__":
    main()
