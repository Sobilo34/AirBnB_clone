#!usr/bin/env python3

import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
