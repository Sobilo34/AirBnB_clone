#!/usr/bin/env python3

"""Create an intractive and non interactive command line interpreter"""

import cmd
import uuid
import json
import datetime
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command line interpreter for CRUD in AirBnB console"""
    prompt = "(hbnb) "
    __classes = ["BaseModel", "OtherClass"]

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, args):
        """Exit the console at End-of-file\n"""
        return True

    def emptyline(self):
        """Handles an empty line not to execute anything"""
        pass

    def __init__(self):
        """Initializes the BaseModel"""
        super().__init__()
        self.BaseModel = {}

    def do_create(self, args):
        """Creates a new instance of BaseModel and save it to JSON"""
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]

        if class_name not in HBNBCommand.__classes:
            """Print error if class is not in the specified classes"""
            print("** class doesn't exist **")
            return
        else:
            """Create an instance"""
            if class_name == 'BaseModel':
                my_instance = BaseModel()

            # Save the instance created to json file
            my_instance.save()
            print(my_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance"""
        if not args:
            print("** class name missing **")
            return

        line = args.split()
        if len(line) < 2:
            print("** instance id missing **")
            return

        class_name = line[0]
        the_id = line[1]
        my_dict = storage.all()

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        elif (class_name, the_id) not in my_dict:
            print("** no instance found **")
            return
        else:
            print(my_dict["{}.{}".format(class_name, the_id)])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        if len(args_list) < 2:
            print("** instance id missing **")
            return

        class_name = args_list[0]
        instance_id = args_list[1]
        my_dict = storage.all()

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        elif (class_name, the_id) not in my_dict:
            print("** no instance found **")
            return

        else:
            del my_dict["{}.{}".format(class_name, instance_id)]
            storage.save()

    def do_all(self, args):
        """Print all the content in the dictionary"""
        my_dict = storage.all()
        array = []

        if args not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for key, value in my_dict.items():
                if value.__class__.__name__ == args:
                    array.append(str(value))
                    print(array)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        my_dict = storage.all()

        if not args:
            print("** class name missing **")
            return

        line = args.split()
        if len(line) < 2:
            print("** instance id missing **")
            return

        class_name = line[0]
        the_id = line[1]
        my_dict = storage.all()

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        elif (class_name, the_id) not in my_dict:
            print("** no instance found **")
            return

        elif len(line) < 2:
            print("** instance id missing **")
            return

        elif len(line) < 3:
            print("** attribute name missing **")
            return

        else:
            for key, value in my_dict.items():
                class_name = value.__class__.__name__
                id_val = value.id
                dict_val = value.__dict__

                if id_val == line[1] and class_name == line[0]:
                    if len(line) < 4:
                        print("** value missing **")
                        break

                    attribute_name = line[2]
                    new_value = line[3]

                    if attribute_name in dict_val:
                        # Update attribute value
                        attribute_type = type(dict_val[attribute_name])
                        dict_val[attribute_name] = attribute_type(new_value)
                    else:
                        # Add new attribute
                        dict_val[attribute_name] = new_value

                    storage.save()
                    break
                else:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
