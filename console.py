#!usr/bin/env python3

import cmd
import uuid
import json
import datetime


class HBNBCommand(cmd.Cmd):
    """Command line interpreter for CRUD in AirBnB console"""
    intro = "Welcome to HBNBCommand console. Type 'help' for more info"
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
            print ("** class name missing **")
            return
        class_name = args.split()[0]
        class_name = class_name.lower()

        self.BaseModel.setdefault(class_name, [])

        with open('BaseModel.json', 'w') as f:
            json.dump(self.BaseModel, f)

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

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        elif len(line) < 2:
            print("** instance id missing **")
            return

        the_id = line[1]

        if class_name not in self.BaseModel or the_id not in self.BaseModel[class_name]:
            print ("** no instance found **")
            return
        else:
            print (self.BaseModel[class_name][the_id])

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

        if class_name not in self.BaseModel:
            print("** class doesn't exist **")
            return

        instances = self.BaseModel[class_name]

        if not any(instance['id'] == instance_id for instance in instances):
            print("** no instance found **")
            return

        # Find the index of the instance with the given ID
        index = next((i for i, instance in enumerate(instances) if instance['id'] == instance_id), None)

        # Remove the instance from the list
        if index is not None:
            del instances[index]
            print('Instance deleted successfully')
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
