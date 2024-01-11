#!/usr/bin/python3
"""
console
"""
import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Main class
    """
    prompt = "(hbnb) "
    models = {'BaseModel': BaseModel, 'Amenity': Amenity,
               'City': City, 'Place': Place, 'Review': Review,
               'State': State, 'User': User}


    def do_quit(self, arg):
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

    def precmd(self, arg):
        """
        preprocess the arg
        """

        return arg



if __name__ == "__main__":
    HBNBCommand().cmdloop()

