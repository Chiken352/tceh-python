# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import os
import errno

__author__ = 'sobolevn'


def _compat_open(filename, encoding='utf-8', permissions='r'):
    if sys.version_info.major == 3:
        f = open(filename, permissions, encoding='utf-8')  # py3 compat
    else:
        f = open(filename, permissions)
    return f


def open_and_read(filename):
    result = None

    try:
        f = _compat_open(filename)
        result = f.readlines()
    except IOError as ex:
        print(ex)
    else:
        f.close()

    return result


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def write_to_file(folders, filename, content):
    try:
        folder_path = os.path.join(*folders)
        mkdir_p(folder_path)  # path now exists
        path = os.path.join(folder_path, filename)

        with _compat_open(path, permissions='w') as _file:
            _file.write(content if sys.version_info.major == 3
                        else content.encode('utf-8'))

    except OSError as ex:
        print('os', ex)
    except IOError as ex:
        print('io', ex)


if __name__ == '__main__':
    print(open_and_read('bad_name'))

    valid_name = os.path.join('files', 'file1.txt')
    result = open_and_read(valid_name)
    print(result)
    list(map(print, result))  # py3 compat

    with _compat_open(valid_name) as _file:
        print(_file.read())

    folders = ['files', 'write', 'sub']
    write_to_file(folders, 'file1.txt', u'Файл с юникодом')
