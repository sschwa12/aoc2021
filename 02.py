from typing import List

from utils import read_file

data = read_file('02')


class Dive:
    def __init__(self, course: List[str]):
        self.course = course
        self.depth = 0
        self.horizontal_pos = 0
        self.aim = 0

    def forward(self, units: int) -> None:
        self.horizontal_pos += units

    def down(self, units: int) -> None:
        self.depth += units

    def up(self, units: int) -> None:
        self.depth -= units

    def run(self) -> int:
        for step in self.course:
            direction, units = step.split()
            getattr(self, direction)(int(units))
        return self.depth * self.horizontal_pos


class PartTwoDive(Dive):
    def down(self, units: int) -> None:
        self.aim += units

    def up(self, units: int) -> None:
        self.aim -= units

    def forward(self, units: int) -> None:
        super().forward(units)
        self.depth += self.aim * units


print(Dive(data).run())
print(PartTwoDive(data).run())
