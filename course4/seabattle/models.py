# -*- coding: utf-8 -*-


class Field(object):
    def __init__(self):
        self.size = 10
        self.data = []
        for i in range(self.size):
            row = [0 for _ in range(self.size)]
            self.data.append(row)


class Storage(object):
    __obj = None

    players = None

    @classmethod
    def __new__(cls, *args):
        if cls.__obj is None:
            cls.__obj = object.__new__(cls)
            cls.items = []
        return cls.__obj


class Player(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

p = Player('Nikita')
p.__str__()
