from dataclasses import dataclass
from itertools import chain
from typing import List

from utils import read_file, chunks


@dataclass
class Num:
    value: int
    marked: bool


data = read_file('04')
stripped = [d for d in data if d != '']
nums = [int(s) for s in stripped[0].split(',')]
bingo_boards = list(chunks([[Num(value=int(n), marked=False) for n in b.split()] for b in stripped[1:]], 5))


class Bingo:
    def __init__(self, nums: List[int], boards: List[List[List[Num]]]):
        self.nums = nums
        self.boards = boards

    def mark(self, num: int, board: List[List[Num]]) -> None:
        for i in range(len(board)):
            for j in range(len(board)):
                val = board[i][j]
                if val.value == num:
                    val.marked = True
                    return

    def is_winner(self, board: List[List[Num]]) -> bool:
        cols = list(zip(*board))
        rows = board
        for r in rows:
            if all(n.marked for n in r):
                return True
        for c in cols:
            if all(n.marked for n in c):
                return True
        return False

    def calc_score(self, num: int, board: List[List[Num]]) -> int:
        return sum([n.value for n in chain(*board) if not n.marked]) * num

    def run(self):
        for num in self.nums:
            for board in self.boards:
                self.mark(num, board)
                if self.is_winner(board):
                    return self.calc_score(num, board)


class BingoLastWinner(Bingo):
    def run(self):
        winners = set()
        for num in nums:
            for i, board in enumerate(self.boards):
                self.mark(num, board)
                if self.is_winner(board):
                    if i not in winners:
                        winners.add(i)
                        if len(winners) == len(self.boards):
                            return self.calc_score(num, board)


bingo = Bingo(nums, bingo_boards)
print(bingo.run())

bingo_last_winner = BingoLastWinner(nums, bingo_boards)
print(bingo_last_winner.run())
