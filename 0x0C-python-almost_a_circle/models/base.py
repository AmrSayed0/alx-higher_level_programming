#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv
import turtle


class BaseModel:
    """Represent the base model.

    BaseModel is the "base" for all other classes in this project.

    Attributes:
        __nb_instances (int): The number of instances of BaseModel.
    """

    __nb_instances = 0

    def __init__(self, id=None):
        """Initialize a new instance of BaseModel.

        Args:
            id (int): The ID of the new instance.
        """
        if id is not None:
            self.id = id
        else:
            BaseModel.__nb_instances += 1
            self.id = BaseModel.__nb_instances

    @staticmethod
    def serialize_to_json(list_dicts):
        """Return the JSON serialization of a list of dictionaries.

        Args:
            list_dicts (list): A list of dictionaries.
        """
        if list_dicts is None or list_dicts == []:
            return "[]"
        return json.dumps(list_dicts)

    @classmethod
    def save_to_file(cls, list_instances):
        """Write the JSON serialization of a list of instances to a file.

        Args:
            list_instances (list): A list of instances of BaseModel or subclasses.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_instances is None:
                jsonfile.write("[]")
            else:
                list_dicts = [inst.to_dictionary() for inst in list_instances]
                jsonfile.write(BaseModel.serialize_to_json(list_dicts))

    @staticmethod
    def deserialize_from_json(json_string):
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **attributes):
        """Return a new instance of a BaseModel subclass, initialized from a dictionary.

        Args:
            **attributes (dict): Key/value pairs of attributes to initialize.
        """
        if attributes and attributes != {}:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 1)
            else:
                new_instance = cls(1)
            new_instance.update(**attributes)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances of a BaseModel subclass, deserialized from a file.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = BaseModel.deserialize_from_json(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_instances):
        """Write the CSV serialization of a list of instances to a file.

        Args:
            list_instances (list): A list of instances of BaseModel or subclasses.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#00ff00")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(4):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()
