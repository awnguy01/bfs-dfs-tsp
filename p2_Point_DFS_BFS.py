"""
Project 2 TSP Search with BFS and DFS
@author Andrew Nguyen Vo
@copyright Copyright 2019, Andrew Nguyen Vo, All Rights Reserved
"""
from time import time
from typing import List

from next_node_map import DEST_NODE_NAME_MAP
from node import Node
from utils import get_file_path, calc_total_distance, find_min_route, print_list_of_routes, calc_elapsed_ts


def get_node_list(file_name: str) -> List[Node]:
    """"""
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
            for dest_name in DEST_NODE_NAME_MAP.get(node.name):
                for test_node in node_list:
                    if test_node.name == dest_name:
                        dest_list.append(test_node)
            node.dest_nodes = dest_list
    return node_list


def bfs(node_list: List[Node]) -> List[List[Node]]:
    all_routes: List[List[Node]] = [[node_list[0]]]
    queue: List[Node] = [node_list[0]]
    while len(queue):
        curr_node = queue.pop(0)
        affected_routes: List[List[Node]] = []

        for route_index, route in enumerate(all_routes):
            if route[-1] == curr_node:
                affected_routes.append(route)
                del all_routes[route_index]

        for dest in curr_node.dest_nodes:
            if dest != node_list[-1]:
                queue.append(dest)
            for aff_route in affected_routes:
                aff_route_copy = aff_route.copy()
                aff_route_copy.append(dest)
                all_routes.append(aff_route_copy)
    return all_routes


def dfs(node_list: List[Node]) -> List[List[Node]]:
    all_routes: List[List[Node]] = [[node_list[0]]]
    stack: List[Node] = [node_list[0]]

    while len(stack):
        curr_node = stack.pop()
        affected_routes: List[List[Node]] = []

        for route_index, route in enumerate(all_routes):
            if route[-1] == curr_node:
                affected_routes.append(route)
                del all_routes[route_index]

        for dest in curr_node.dest_nodes:
            if dest != node_list[-1]:
                stack.append(dest)
            for aff_route in affected_routes:
                aff_route_copy = aff_route.copy()
                aff_route_copy.append(dest)
                all_routes.append(aff_route_copy)

    return all_routes


def main():
    file_name: str = get_file_path([('TSP File', '*.tsp')])
    if file_name is not None:
        node_list: List[Node] = get_node_list(file_name)

        bfs_start: int = time()
        bfs_routes = bfs(node_list)
        bfs_elapsed: str = calc_elapsed_ts(bfs_start)

        for route in bfs_routes:
            # print(*map(lambda node: node.name, route), end=' = ')
            print(calc_total_distance(route))

        if len(bfs_routes):
            min_route = find_min_route(bfs_routes)
            print(*map(lambda node: node.name, min_route), end=' = ')
            print(calc_total_distance(min_route))
        else:
            print('BFS could not find any valid routes')

        print(f'Calculated in {bfs_elapsed}')

        ###############################################################

        dfs_start: int = time()
        dfs_routes = dfs(node_list)
        dfs_elapsed: str = calc_elapsed_ts(dfs_start)

        if len(dfs_routes):
            min_route = find_min_route(dfs_routes)
            print(*map(lambda node: node.name, min_route), end=' = ')
            print(calc_total_distance(min_route))
        else:
            print('DFS could not find any valid routes')

        print(f'Calculated in {dfs_elapsed}')


if __name__ == "__main__":
    main()
