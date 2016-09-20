# -*- coding: utf-8 -*-

import json
import os

__author__ = 'sobolevn'


class Person(object):
    def __init__(self, name, age, is_male):
        self.name = name
        self.age = age
        self.gender = 'male' if is_male else 'female'

    def __str__(self):
        return '{} {} {}'.format(self.name, self.age, self.gender)

    def __repr__(self):
        return str(self)


class PersonEncoder(json.JSONEncoder):
    def default(self, o):
        # print(o)
        if isinstance(o, Person):
            return {
                'name': o.name,
                'age': o.age,
                'is_male': o.gender == 'male',
            }
        else:
            return json.JSONEncoder().default(o)


class PersonDecoder(json.JSONDecoder):
    def _parse_person(self, default_obj):
        return Person(
            default_obj['name'],
            default_obj['age'],
            default_obj['is_male'],
        )

    def decode(self, json_string, **kwargs):
        default_obj = super(PersonDecoder, self).decode(
                json_string, **kwargs)
        if isinstance(default_obj, (tuple, list)):
            return [self._parse_person(item) for item in default_obj]

        return self._parse_person(default_obj)

if __name__ == '__main__':
    represent = json.dumps({
        "value": "1",
        "int_value": 2,
        'lst': [1, 2, 'item']
    })
    print('now it is a string', represent)
    print('now dict', json.loads(represent))

    p = Person('A', 1, True)
    result_json = PersonEncoder().encode(p)
    print(result_json)

    new_object = PersonDecoder().decode(result_json)
    print(new_object)

    persons_file = os.path.join('files', 'objects.json')

    with open(persons_file) as _file:
        print(json.load(_file, cls=PersonDecoder))
