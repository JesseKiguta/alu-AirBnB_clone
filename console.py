#!/usr/bin/python3
"""
console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Main class
    """
    prompt = "(hbnb) "


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

