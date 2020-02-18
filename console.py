#!/usr/bin/python3
""" This module contains base class for the console """
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Base console class """

    prompt = "(hbtn) "
    classes = {"BaseModel"}

    def emptyline(self):
        """Blank lines handling"""
        pass

    def do_quit(self, arg):
        """Quit the console
        """
        return True

    def do_EOF(self, arg):
        """Quit the console using EOF signal"""
        return True

    def do_create(self, arg):
        """Creates a new object"""
        if not arg:
            print("** class name missing **")
        if arg not in self.classes:
            print("** class doesn't exist **")
        else:
            myobj = eval(arg)()
            print(myobj.id)
            storage.save()

    # def do_show(self, arg):
    #     """Prints string repr of an instance"""
    #     args = arg.split()
    #     if not args:
    #         print("** class name missing **")
    #     else if args[0] not in self.classes:
    #         print("** class doesn't exist **")
    #     else if not args[1]:
    #         print("** instance id missing **")
    #     objects = storage.all()
    #     for values in objects.values():
    #         if values.__class__.__name__ == args[0] and values.id == args[1]:
    #             print(v)
    #             return
    #     print("** no instance found **")

console = HBNBCommand()
console.cmdloop()
