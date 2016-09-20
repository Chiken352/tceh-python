# -*- coding: utf-8 -*-

from __future__ import print_function

from functools import reduce  # py3 compatibility

__author__ = 'sobolevn'


def big_function():
    for _ in range(10000000):
        print('Waiting...')


if __name__ == '__main__':
    (lambda x, y: print(x, y))(1, 2)

    # Use cases:

    # Sorting:
    values = {(1, 3): 'one', (3, 0): 'three', (2, 2): 'two_'}
    print(sorted(values, key=lambda key: key[1]))
    print(sorted(values, key=lambda key: key[0]))
    print(sorted(values.items(), key=lambda key: len(key[1])))

    # map, filter, reduce:
    values = [1, 2, 3, 4]
    new_values = map(lambda v: v*2, values)
    print(new_values)
    new_values = list(new_values)  # py3 compatibility
    print(new_values)

    new_values = reduce(lambda result, v: result + v, values)
    print(new_values)

    new_values = list(filter(lambda x: x > 2, values))
    print(new_values)

    # Lazy-values:
    lazy = lambda: big_function()
    print(lazy)

    # This will call big_function() inside lambda:
    # lazy()
