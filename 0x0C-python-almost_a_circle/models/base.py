#!/usr/bin/python3
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = cls.__name__ + ".json"
        with open(file_name, "w", encoding="utf-8") as file:
            json_data = [obj.to_dictionary() for obj in list_objs]
            file.write(Base.to_json_string(json_data))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or not json_string:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        with open(filename, "r") as file:
            data = file.read()
            if data:
                list_dicts = cls.from_json_string(data)
                return [cls.create(**d) for d in list_dicts]
            else:
                return "[]"
