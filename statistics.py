#!/usr/bin/env python3
# Encoding: UTF-8
import argparse
from collections import Counter
from itertools import chain
from sys import stdin, exit
from typing import List, Tuple

import matplotlib
matplotlib.use('agg')
# import matplotlib.pyplot as plt


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=argparse.FileType('w'), default=stdin,
                        help='Input text corpus')
    parser.add_argument('--type', choices=['freq', 'mc'], help='Type of counting - either '
                                                               'frequencies or most-common words')
    parser.add_argument('--n', type=int, help='Threshold for type.')
    return parser


def word_frequencies(text: List[str]) -> Counter:
    tokens = chain.from_iterable(line.split() for line in text)
    return Counter(tokens)


def total_count(word_frequencies: Counter) -> int:
    return sum(count for count in word_frequencies.values())


def frequencies_percentage(n: int, word_frequencies: Counter) -> Tuple[float,int]:
    freq_count = sum(freq for freq in word_frequencies.values() if freq > n)
    return freq_count / total_count(word_frequencies), freq_count


def most_common_percentage(n: int, word_frequencies: Counter) -> Tuple[float,int]:
    mc_count = sum(mc[1] for mc in word_frequencies.most_common(n))
    return mc_count / total_count(word_frequencies), mc_count


if __name__ == '__main__':
    args = create_parser().parse_args()
    if args.type and not args.n:
        print('You need to provide both type and n parameters!')
        exit(1)

    with args.input as f:
        lines = f.read().splitlines()

    word_freq = word_frequencies(lines)
    print("Total word count: {}".format(total_count(word_freq)))

    if args.type == 'freq':
        p, count = frequencies_percentage(args.n, word_freq)
        print('Percentage of freq: {}\nPruned count: {}'.format(p, count))
    else:
        p, count = most_common_percentage(args.n, word_freq)
        print('Percentage of most-common: {}'.format(p, count))
