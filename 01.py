from typing import List

from utils import read_file

data = [int(n) for n in read_file('01')]

sample = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def find_depth_increases(depths: List[int]) -> int:
    cnt = 0
    for i, d in enumerate(depths):
        if d > depths[i - 1]:
            cnt += 1
    return cnt


def find_depth_sliding_window(depths: List[int], window_size: int = 3) -> int:
    return find_depth_increases([sum(depths[i:i + window_size]) for i, _ in enumerate(depths)])


# part 1
print(find_depth_sliding_window(data, 1))
# part 2
print(find_depth_sliding_window(data))
