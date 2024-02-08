#!usr/bin/env python3

import cmd
import uuid
import json
import datetime


class HBNBCommand(cmd.Cmd):
    """Command line interpreter for CRUD in AirBnB console"""
    intro = "Welcome to HBNBCommand console. Type 'help' for more info"
    prompt = "(hbnb) "

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
            print ("** class name missing **")
            return
        class_name = args.split()[0]

        if class_name not in self.BaseModel:
            print("** class doesn't exist **")
            return
        
        instance_create = {"id": str(uuid.uuid4())}
        self.BaseModel[class_name].append(instance_create)
        print(instance_create['id'])

    def do_show(self, args):
        """Prints the string representation of an instance"""
        if not args:
            print("** class name missing **")
            return

        line = args.split()
        class_name = line[0]

        if class_name not in self.BaseModel:
            print ("** class doesn't exist **")
            return

        if len(line) < 2:
            print("** instance id missing **")
            return

        the_is = line[1]
        instance_show = [instance for instance in self.BaseModel[class_name] if instance['id'] == the_id]

        if not instance_show:
            print ("** no instance found **")
            return

        print (instance_show[0])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
