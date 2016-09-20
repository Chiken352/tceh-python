# -*- coding: utf-8 -*-

from __future__ import print_function

from functools import reduce  # py3 compatibility

__author__ = 'sobolevn'


def make_double(x):
    return x * 2


def divide_by_two(number):
    return number / 2


def sum_data(data, x):
    print('reduce iteration', data, x)
    return data + x


def is_positive(num):
    return num > 0


def is_string(item):
    return isinstance(item, str)


if __name__ == '__main__':
    # map:
    s = [1, 2, 3, 4]
    double_s = list(map(make_double, s))
    print('double_s', double_s)

    k = [4, 8, 16, 32]
    divided_k = list(map(divide_by_two, k))
    print('divided_k', divided_k)

    # reduce:
    r = [1, 2, 3, 10, 15]
    sum_of_r = reduce(sum_data, r)
    print('sub_of_r by reduce()', sum_of_r)

    list_of_chars = ['p', 'y', 't', 'h', 'o', 'n']
    joined_chars = reduce(sum_data, list_of_chars)
    print('joined_chars by reduce()', joined_chars)

    # filter:
    numbs = [-13, 0, 9, 123, -12312412312, 0.3]
    positive = list(filter(is_positive, numbs))
    print('only positive by filter', positive)

    mixed = [1, '12', 'some', 'word', 123, object, {}]
    print('only strings', list(filter(is_string, mixed)))
