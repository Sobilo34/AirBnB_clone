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

        for k in my_dict:
            if k == key:
                del my_dict[k]
                break
        
        storage.__object = my_dict
        storage.save()
        return

    def do_all(self, args):
            """Print all the content in the dictionary"""
            my_dict = storage.all()
            array = []

            if not args:
                # If args is empty, print all instances
                array = [str(value) for key, value in my_dict.items()]
                print(array)
            elif args not in HBNBCommand.__classes:
                # If args is not in the valid classes, print an error message
                print("** class doesn't exist **")
            else:
                # Otherwise, filter instances based on the provided class name
                for key, value in my_dict.items():
                    if value.__class__.__name__ == args:
                        array.append(str(value))
                    print(array)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""

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
            print("** value missing **")
            return
        if len_ > 4:
            return
        
        obj_name, obj_id, attr_name, value = args_list

        if obj_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        my_dict = storage.all()
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
