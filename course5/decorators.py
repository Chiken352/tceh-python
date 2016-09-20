# -*- coding: utf-8 -*-

from __future__ import print_function

__author__ = 'sobolevn'


def action_decorator(func):
    def inner(text):
        print('Someone is going to', func.__name__)
        func(text)

    return inner


# @action_decorator  # try to uncomment me
def shout(text):
    print(text.upper(), '!!!!')


# @action_decorator
def whisper(text):
    print(text.lower(), '...')


# @action_decorator
def say(something):
    something += '; was said.'
    print(something)



@action_decorator
def decorated_say(text):
    say(text)  # the same as `say()`, but decorated


if __name__ == '__main__':
    # Basic functions:
    say('hi')
    whisper('Hello')
    shout('i am here')

    # Decorated:
    decorated_say('hello, i am decorated')
