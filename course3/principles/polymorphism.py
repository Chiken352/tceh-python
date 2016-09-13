# -*- coding: utf-8 -*-

from __future__ import print_function

__author__ = 'sobolevn'


def func():
    pass


class Parent(object):
    def call(self):
        print('Parent')


class Child(Parent):
    def call(self):
        print('Child')


def call_obj(obj):
    obj.call()


if __name__ == '__main__':
    Parent().call()
    # Parent().call(1)
    Child().call()
    call_obj(Child())

