# -*- coding: utf-8 -*-

__author__ = 'sobolevn'


if __name__ == '__main__':
    values = ['item%d' % s for s in range(1, 5)]
    print(values)

    values = ('item%d' % s for s in range(1, 5))
    print(values)
    print(list(values))

    values = [item for item in range(14) if item % 2 == 1]
    print(values)

    # Nested:
    res = [(x, y) for x in range(3) for y in range(3)]
    print(res)
    res = [[(x, y) for x in range(3)] for y in range(3)]
    print(res)

    value = 'MY STRING'

    # PEP-274
    # https://www.python.org/dev/peps/pep-0274/
    my_dict = {x.lower(): x for x in value if x != ' '}
    print(my_dict)
