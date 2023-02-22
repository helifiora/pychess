from __future__ import annotations
from enum import Enum


class Color(Enum):
    WHITE = 0
    BLACK = 1

    def inverse(self) -> Color:
        return Color.WHITE if self.BLACK else Color.BLACK
