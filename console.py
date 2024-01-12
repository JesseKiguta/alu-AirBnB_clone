#!/usr/bin/python3
"""
console
"""
from models.base_model import BaseModel
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Main class
    """
    prompt = "(hbnb) "

    classes = {"BaseModel": BaseModel}


    def do_quit(self, args):
        """
        exiting the console
        """
        return True

    def emptyline(self):
        """
        do nothing
        """
        pass

    def do_EOF(self, args):
        """
        keyboard interruption
        """
        return True

    def precmd(self, args):
        """
        preprocess the arg
        """

        return args


    def do_create(self, args):
        """
        create and save a new object
        ex: create BaseModel
        """
        if len(args) < 1:
            print("** class name missing **")
        else:
            cls = HBNBCommand.classes.get(args)
            if cls is None:
                print("** class doesn't exist **")
            else:
                obj = cls()
                obj.save()
                print(obj.id)


    def do_show(self, args):
        """
        show the dict representation of an object
        ex: show BaseModel 12345
        """
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            obj = storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)


    def do_destroy(self, args):
        """
        delete and object
        based on its class and id
        ex: destroy BaseModel 1234567
        """
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            obj = storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()


    def do_all(self, args):
        """
        show all objects in storage or all objects of a certain class
        ex: all
        or
        ex: all BaseModel
        """
        res = []
        args = args.split()
        if len(args) < 1:
            for k, v in storage.all().items():
                res.append(str(v))
            print(res)
        else:
            cls = args[0]
            if cls not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                for k, v in storage.all().items():
                    if k.startswith(cls):
                        res.append(str(v))
                print(res)


    def do_update(self, args):
        """
        update an object by add or updating an attribute
        ex: update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args = args.split()
        try:
            cls = args[0]
            if cls not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
        except:
            print("** class name missing **")
            return
        try:
            iD = args[1]
            key = cls + "." + iD
            obj = storage.all().get(key)
            if obj is None:
                print("** no instance found **")
                return
        except:
            print("** instance id missing **")
            return
        try:
            attr_name = args[2]
        except:
            print("** attribute name missing **")
            return
        try:
            value = args[3]
            if '"' in value:
                value = value.strip('"')
        except:
            print("** value missing **")
            return
        setattr(obj, attr_name, value)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

