from time import time
from typing import Tuple, List
from tkinter import Tk, filedialog

from node import Node


def get_file_path(file_types: Tuple[str, str] = []) -> str or None:
    """Open file explorer to select a file"""
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfile(filetypes=file_types)
    if file_path is not None:
        return file_path.name
    return None


def print_progress(progress_amount: int, total: int, percent_increments: int) -> None:
    """Print a progress bar animation to the console"""
    percentage: float = progress_amount / total * 100
    fill_length: str = '=' * int(percentage // percent_increments)
    empty_length: str = ' ' * (100 // percent_increments - len(fill_length))
    print(f'[{fill_length}{empty_length}] {percentage:.2f}% complete', end='\r')


def calc_distance(city_a: Node, city_b: Node) -> float:
    """Calculate distance between cities using distance formula"""
    return ((float(city_b.x) - float(city_a.x)) ** 2 + (float(city_b.y) - float(city_a.y)) ** 2) ** (1 / 2)


def calc_total_distance(route: List[Node]) -> float:
    """Calculate the total distance of a Hamiltonian path starting and returning from/to the same city"""
    total_distance: float = 0
    if len(route) > 0:
        for i in range(len(route) - 1):
            total_distance += calc_distance(route[i], route[i + 1])
    return total_distance


def find_min_route(route_list: List[List[Node]]):
    """Find the shortest weighted route from a list of routes """
    min_bfs = route_list[0]
    for route in route_list:
        if calc_total_distance(route) < calc_total_distance(min_bfs):
            min_bfs = route
    return min_bfs


def calc_elapsed_ts(start_time: int) -> str:
    """Calculate and display the total time elapsed given a starting time in hh:mm:ss format"""
    total_seconds: int = time() - start_time
    hours: int = total_seconds // 3600
    total_seconds -= hours * 3600
    mins: int = total_seconds // 60
    total_seconds -= mins * 60
    return f'{hours:02.0f}:{mins:02.0f}:{total_seconds:06.3f}'


def print_list_of_routes(all_routes: List[List[Node]]) -> None:
    """Print to console the list of routes"""
    for route in all_routes:
        print(*map(lambda node: node.name, route))
