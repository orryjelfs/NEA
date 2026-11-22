from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Coord:
    x: int
    y: int
