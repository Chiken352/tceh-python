# -*- coding: utf-8 -*-

__all__ = ('get_info', )

def get_info():
    print('Info is printed, file: %s, __name__: %s' % (__file__, __name__))

def wont_show():
    print('This will not be imported by *')
