from collections import Counter
from typing import List, Callable

from utils import read_file

data = read_file('03')


def bin_to_dec(binary: str) -> int:
    return int(binary, 2)


def get_power_consumption(report: List[str]) -> int:
    cols = list(zip(*report))
    gamma_rate = ''
    epsilon_rate = ''
    for col in cols:
        gamma, epsilon = Counter(col).most_common()
        gamma_rate += gamma[0][0]
        epsilon_rate += epsilon[0][0]
    return bin_to_dec(gamma_rate) * bin_to_dec(epsilon_rate)


print(get_power_consumption(data))


def oxygen_generator_rating(cnt: Counter, report: List[str], i: int) -> List[str]:
    mc = cnt.most_common()[0][0]
    if len(set(cnt.values())) == 1:
        mc = '1'
    return [bit_str for bit_str in report if bit_str[i] == mc]


def co2_scrubber_rating(cnt: Counter, report: List[str], i: int) -> List[str]:
    mc = cnt.most_common()[1][0]
    if len(set(cnt.values())) == 1:
        mc = '0'
    return [bit_str for bit_str in report if bit_str[i] == mc]


def get_rating(report: List[str], rating_fn: Callable) -> int:
    r = report.copy()
    i = 0
    while len(r) > 1:
        col = [ln[i] for ln in r]
        cnt = Counter(col)
        r = rating_fn(cnt, r, i)
        i += 1
    return bin_to_dec(r[0])


def get_life_support_rating(report: List[str]) -> int:
    return get_rating(report, oxygen_generator_rating) * get_rating(report, co2_scrubber_rating)


print(get_life_support_rating(data))
