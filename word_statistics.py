# Encoding: UTF-8
import argparse
from collections import Counter
from itertools import chain

import matplotlib
matplotlib.use('agg')
# import matplotlib.pyplot as plt


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, required=True, help='Input text corpus')
    return parser


def word_frequencies(text: List[str]) -> Counter:
    tokens = chain.from_iterable(line.split() for line in text)
    return Counter(tokens)


if __name__ == '__main__':
    args = create_parser().parse_args()
    with open(args.input, '')