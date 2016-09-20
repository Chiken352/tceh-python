# -*- coding: utf-8 -*-

# see
# http://stackoverflow.com/questions/16981921/relative-imports-in-python-3

from __future__ import absolute_import

# will also work:
# import imports_example.module_two

# Right one:
from imports_example import module_two

# Or also possible:
from imports_example.module_two import do_work

if __name__ == '__main__':
    # module_two.do_work()
    do_work()

    from imports_example.module_one import test_imports as test
    test()
