# -*- coding: utf-8 -*-

import dis

class Test(object):
    name = 'Nikita'

    @classmethod
    def class_method(cls):
        print(cls.name)

    @staticmethod
    def static_method(surname):
        print('static')

if __name__ == '__main__':
    dis.dis(Test.class_method)
    print()
    dis.dis(Test.static_method)
