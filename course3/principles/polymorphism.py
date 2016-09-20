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


class Example(object):
    def call(self):
        print('Ex')


def call_obj(obj):
    obj.call()


if __name__ == '__main__':
    call_obj(Child())
    call_obj(Parent())
