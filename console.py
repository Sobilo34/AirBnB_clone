#!/usr/bin/env python3

"""Create an intractive and non interactive command line interpreter"""

import cmd
import uuid
import json
import datetime
from models.base_model import BaseModel
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command line interpreter for CRUD in AirBnB console"""
    prompt = "(hbnb) "
    __classes = [
            "BaseModel",
            "User",
            "Place",
            "Amenity",
            "City",
            "Review",
            "State"
            ]

    def precmd(self, line):
        suffix_all = ".all()"
        suffix_cnt = ".count()"
        all_meth = list(map(lambda x: x+suffix_all, HBNBCommand.__classes))
        count_meth = list(map(lambda x: x+suffix_cnt, HBNBCommand.__classes))

        if line in all_meth:
            # BaseModel.all() -> "all BaseModel"
            return "all" + " " + line.split(".")[0]

        if line in count_meth:
            # Amenity.count() -> "count Amenity"
            return "count" + " " + line.split(".")[0]

        if line.startswith(
                tuple(name + ".show" for name in HBNBCommand.__classes)
                ):
            # User.show(id) -> "show User id"
            name, id_part = line.split(".show(")
            name = name.strip()
            id_ = id_part.strip(")")
            return "show" + " " + name + " " + id_

        if line.startswith(
                tuple(name + ".destroy" for name in HBNBCommand.__classes)
                ):
            # Place.destroy(id) -> "destroy Place id"
            name, id_part = line.split(".destroy(")
            name = name.strip()
            id_ = id_part.strip(")")
            return "destroy" + " " + name + " " + id_

        if line.startswith(
                tuple(name + ".update" for name in HBNBCommand.__classes)
                ):
            # Split the line by ".update("
            parts = line.split(".update(")
            name = parts[0].strip()
            params = parts[1].strip(")").split(", ")

            # Now!, extract id_ and examine if the last parameter is a dict
            id_ = params[0]
            last_param = params[-1]

            if last_param.startswith("{") and last_param.endswith("}"):
                return "update {} {}".format(name, " ".join(params))
            else:
                attr_name = params[1]
                attr_val = params[2]
                return "update {} {} {} {}".format(
                        name, id_, attr_name, attr_val)
        return line

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, args):
        """Exit the console at End-of-file\n"""
        return True

    def emptyline(self):
        """Handles an empty line not to execute anything"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel and save it to JSON"""
        if not args:
            print("** class name missing **")
            return
        class_name = args.split()[0]

        if class_name not in HBNBCommand.__classes:
            """Print error if class is not in the specified classes"""
            print("** class doesn't exist **")
            return
        else:
            """Create an instance"""
            if class_name == 'BaseModel':
                my_instance = BaseModel()
            if class_name == 'User':
                my_instance = User()

            if class_name == 'Place':
                my_instance = Place()

            if class_name == 'State':
                my_instance = State()

            if class_name == 'Amenity':
                my_instance = Amenity()

            if class_name == 'Review':
                my_instance = Review()

            if class_name == 'City':
                my_instance = City()

            # Save the instance created to json file
            my_instance.save()
            print(my_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance"""
        args_list = args.split()
        len_ = len(args_list)
        if len_ == 0:
            print("** class name missing **")
            return
        if len_ == 1:
            print("** instance id missing **")
            return
        if len_ > 2:
            return

        obj_name = args_list[0]
        obj_id = args_list[1]

        if obj_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        storage.reload()
        my_dict = storage.all()
        key = ".".join([obj_name, obj_id])

        try:
            print(my_dict[key])
            return
        except KeyError:
            print("** no instance found **")
            return

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args_list = args.split()
        len_ = len(args_list)
        if len_ == 0:
            print("** class name missing **")
            return
        if len_ == 1:
            print("** instance id missing **")
            return
        if len_ > 2:
            return

        obj_name = args_list[0]
        obj_id = args_list[1]

        if obj_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        my_dict = storage.all()
        key = ".".join([obj_name, obj_id])

        try:
            del my_dict[key]
            storage.save()
        except KeyError:
            print("** no instance found **")
            return

    def do_all(self, args):
        """Print all the content in the dictionary"""
        my_dict = storage.all()
        array = []

        if not args:
            # If args is empty, print all instances
            array = [str(value) for key, value in my_dict.items()]
            print(array)
            return

        elif args not in HBNBCommand.__classes:
            # If args is not in the valid classes, print an error message
            print("** class doesn't exist **")
            return

        else:
            # Otherwise, filter instances based on the provided class name
            for key, value in my_dict.items():
                if value.__class__.__name__ == args:
                    array.append(str(value))

            print(array)
            return

    def do_count(self, args):
        """Retrives the number of instances of a class"""
        my_dict = storage.all()
        instances = []

        if not args:
            print("** class name missing **")
            return

        elif args not in HBNBCommand.__classes:
            # If args is not in the valid classes, print an error message
            print("** class doesn't exist **")
            return

        else:
            for key, value in my_dict.items():
                if value.__class__.__name__ == args:
                    instances.append((key, value))

            # Now! split the instances
            instance_dict = dict(instances)
            split_instance = {}

            for key, value in instance_dict.items():
                id_ = key.split('.')[1]
                split_instance[id_] = value

            instance_count = len(split_instance)
            print(instance_count)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        my_dict = storage.all()

        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        len_ = len(args_list)
        if len_ == 1:
            print("** instance id missing **")
            return

        if len_ == 2:
            print("** attribute name missing **")
            return
        if len_ == 3:
            obj_name, obj_id, dictionary = args_list
            key = ".".join([obj_name, obj_id])

            if not dictionary.startswith("{") and not dictionary.endswith("}"):
                print("** value missing **")
                return

            try:
                obj = my_dict.get(key)
                if obj:
                    attr_dict = eval(dictionary)
                    if isinstance(attr_dict, dict):
                        for attr_name, attr_value in attr_dict.items():
                            obj.__dict__[attr_name] = attr_value
                        obj.updated_at = datetime.now()
                        obj.save()
                        my_dict[key] = obj # Update the object in my_dic
            except Exception as e:
                print(e)

        if len_ > 4:
            return

        obj_name, obj_id, attr_name, value = args_list

        if obj_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        key = ".".join([obj_name, obj_id])

        try:
            obj = my_dict.get(key)
            if obj:
                setattr(obj, attr_name, value)
                obj.save()
            else:
                print("** no instance found **")
                return
        except Exception as e:
            print(e)
            print("** no instance found **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
