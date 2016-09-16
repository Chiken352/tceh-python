# -*- coding: utf-8 -*-

from __future__ import absolute_import

# This wont work together:
# from __future__ import absolute_import

# import module_two

# from . import module_two  # explicit relative import!
from imports_example import module_two

def test_imports():
    # without absolute_import (possible, but not right):
    # from sub_package import get_info
    # from sub_package.sub import help

    # with absolute_import:
    from imports_example.sub_package import get_info
    from imports_example.sub_package.sub import help

    help()
    module_two.do_work()

