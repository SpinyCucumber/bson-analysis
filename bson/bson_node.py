from __future__ import annotations

__all__ = ["BsonNode"]

class BsonNode:
    size: int
    name: str
    children: list[BsonNode]

    def __init__(self) -> None:
        self.children = []