from typing import List, Dict

from node import Node

DEST_NODE_NAME_MAP: Dict[str, List[str]] = {
    '1': ['2', '3', '4'],
    '2': ['3'],
    '3': ['4', '5'],
    '4': ['5', '6', '7'],
    '5': ['7', '8'],
    '6': ['8'],
    '7': ['9', '10'],
    '8': ['9', '10', '11'],
    '9': ['11'],
    '10': ['11'],
    '11': []
}
