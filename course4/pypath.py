# -*- coding: utf-8 -*-

# from __future__ import absolute_import

import sys


if __name__ == '__main__':
    # run this file with python2 and 3, with and without venv:
    print('Modules are loaded from:', sys.path)

    # test:
    from exec_module import print_info
    print_info()
