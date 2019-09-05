from typing import List


class Node:
    def __init__(self, name: str, x: float = 0, y: float = 0, dest_nodes: List['Node'] = []):
        self.name = name
        self.x = x
        self.y = y
        self.dest_nodes = dest_nodes

    def __eq__(self, other):
        return self.name == other.name

    def dest_nodes_to_string(self):
        next_nodes_str: str = '['
        if self.dest_nodes is not None:
            for i, node in enumerate(self.dest_nodes):
                if i == 0:
                    next_nodes_str += node.name
                else:
                    next_nodes_str += f',{node.name}'
        next_nodes_str += ']'
        return next_nodes_str
