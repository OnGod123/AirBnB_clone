from typing import Dict, Union
import json
from datetime import datetime

class BaseModel:
    """Forward declaration to avoid circular import issues."""
    pass

class FileStorage:
    """Class to serialize and deserialize objects to/from JSON file."""

    __file_path = "file.json"
    __objects: Dict[str, Union['BaseModel', Dict[str, Union[str, datetime]]]] = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                serialized_objects = json.load(file)
                for key, value in serialized_objects.items():
                    class_name, obj_id = key.split('.')

                    # Import BaseModel here to avoid circular import
                    from models.base_model import BaseModel

                    # Create an instance from the dictionary representation
                    obj = BaseModel.from_dict(value)

                    # Set the object in __objects dictionary
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass




