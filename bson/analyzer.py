from typing import BinaryIO, Optional
from bson.bson_node import BsonNode
from bson import decode_file_iter

import argparse
import sys

def output_bson_node(root: BsonNode, file: BinaryIO):

    def _print_with_depth(string: str, depth: int):
        print(f"{'  '*depth}{string}", file=file)

    def _print_node(node: BsonNode, parent: Optional[BsonNode], depth: int):
        header = f"{node.name}: {node.size}"
        # Size relative to parent
        if parent != None:
            percent = 100 * (node.size / parent.size)
            header += f" ({percent:.2f}%)"
        # Size relative to root
        # root_percent = 100 * (node.size / root.size)
        # header += f" [{root_percent:.2f}%]"
        _print_with_depth(header, depth)
        # Sort children by size
        sorted_children = sorted(node.children, key=lambda node: node.size, reverse=True)
        for child in sorted_children:
            _print_node(child, node, depth + 1)

    _print_node(root, None, 0)

def analyze_file():
    parser = argparse.ArgumentParser()
    parser.add_argument("bsonfile", type=argparse.FileType("rb"))
    parser.add_argument("outfile", nargs="?", type=argparse.FileType("w", encoding="utf-8"), default=sys.stdout)
    args = parser.parse_args()
    for _, node in decode_file_iter(args.bsonfile):
        output_bson_node(node, args.outfile)
    # Close files
    args.outfile.close()