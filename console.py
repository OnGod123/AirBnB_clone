#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel
from models import storage
import sys

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.strip()
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = self.valid_classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        if not arg:
            instance_list = []
            for key, value in storage.all().items():
                instance_list.append(str(value))
            print(instance_list)
        else:
            class_name = arg.split()[0]
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return

            instance_list = []
            for key, value in storage.all().items():
                if key.split(".")[0] == class_name:
                    instance_list.append(str(value))
            print(instance_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]

        instance = storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def emptyline(self):
        """Called when an empty line is entered."""
        pass

    def do_quit(self, arg):
        """Exits the program."""
        sys.exit()

    def do_EOF(self, arg):
        """Handles EOF (Ctrl+D)"""
        print("")
        return True

    def cmdloop(self):
        """Starts the command loop."""
        self.valid_classes = {
            'BaseModel': BaseModel
            # Add other valid classes here
        }
        super().cmdloop()

if __name__ == "__main__":
    HBNBCommand().cmdloop()

