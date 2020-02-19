#!/usr/bin/python3
""" This module contains base class for the console """
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Base console class """

    prompt = "(hbnb) "
    classes = {"BaseModel",
               "User",
               "State",
               "City",
               "Amenity",
               "Place",
               "Review"}

    def emptyline(self):
        """Blank lines handling"""
        pass

    def do_quit(self, arg):
        """Quit the console"""
        return True

    def do_EOF(self, arg):
        """Quit the console using EOF signal"""
        print("")
        return True

    def do_create(self, arg):
        """Creates a new object"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            myobj = eval(arg)()
            print(myobj.id)
            storage.save()

    def do_show(self, arg):
        """Prints string repr of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        objects = storage.all()
        for values in objects.values():
            if values.__class__.__name__ == args[0] and values.id == args[1]:
                print(values)
                return
        print("** no instance found **")

    def do_destroy(self, arg):
        """Destroys an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        objects = storage.all()
        key = args[0] + "." + args[1]
        if key in objects:
            storage.delete(key)
            storage.save()
            return
        print("** no instance found **")

    def do_all(self, arg):
        """Shows all classes optionally refined with classname"""
        objects = storage.all()
        v = 0
        i = 0
        if arg:
            if len(objects) != 0:
                print('["', end="")
            for value in objects.values():
                if value.__class__.__name__ == arg:
                    if i != 0:
                        print('"', end="")
                    print(value, end="")
                    if i != len(objects.values()) - 1:
                        print('", ', end="")
                    i = i + 1
                    v = 1
            if len(objects) != 0:
                print('"]')
            if v == 0:
                print("** class doesn't exist **")
                return
            return
        i = 0
        if len(objects) != 0:
            print('["', end="")
        for value in objects.values():
            if i != 0:
                print('"', end="")
            print(value, end="")
            if i != len(objects.values()) - 1:
                print('", ', end="")
            i = i + 1
        if len(objects) != 0:
            print('"]')

    def do_update(self, arg):
        """Updates an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        objects = storage.all()
        key = args[0] + "." + args[1]
        if key in objects:
            storage.update(key, args[2], args[3])
            storage.save()
            return
        print("** no instance found **")

    def do_BaseModel(self, arg):
        """BaseModel class method handling"""
        if arg == ".all()":
            self.do_all("BaseModel")

    def do_User(self, arg):
        """User class method handling"""
        if arg == ".all()":
            self.do_all("User")

    def do_Amenity(self, arg):
        """Amenity class method handling"""
        if arg == ".all()":
            self.do_all("Amenity")

    def do_State(self, arg):
        """State class method handling"""
        if arg == ".all()":
            self.do_all("State")

    def do_Place(self, arg):
        """Place class method handling"""
        if arg == ".all()":
            self.do_all("Place")

    def do_Review(self, arg):
        """Review class method handling"""
        if arg == ".all()":
            self.do_all("Review")

    def do_City(self, arg):
        """City class method handling"""
        if arg == ".all()":
            self.do_all("City")


console = HBNBCommand()
if __name__ == "__main__":
    console.cmdloop()
