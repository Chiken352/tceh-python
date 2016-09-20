# -*- coding: utf-8 -*-

__author__ = 'sobolevn'


# First example:
class Person(object):
    def say(self):
        print('I am a person!')


class Teacher(object):
    def tell_about_yourself(self):
        print('I am a teacher!')


# Second example:
class Square(object):
    def __init__(self, size):
        self.height = size
        self.width = size
        print('Area is %d' % (self.height * self.width))

    def __str__(self):
        return 'Square with area: %d' % (self.width * self.height)


if __name__ == '__main__':
    # 1:
    Person().say()
    Teacher().tell_about_yourself()

    # 2:
    print(Square(4))
