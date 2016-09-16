# -*- coding: utf-8 -*-

# from sub_two import get_info
from imports_example.sub_package.sub_two import get_info
get_info()

# from sub_two import *
from imports_example.sub_package.sub_two import *
get_info()

try:
    wont_work()
except NameError as ex:
    print(ex)
