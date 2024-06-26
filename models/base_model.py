import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base model class that defines all common attributes/methods for other classes."""
    globals = {}

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments for initializing attributes.
        """
        cls_name = self.__class__.__name__
        BaseModel.globals[cls_name] = self

        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        storage.new(self)

    def __str__(self):
        """Return a string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    @classmethod
    def from_dict(cls, dict_representation):
        """Recreate an instance from its dictionary representation.

        Args:
            dict_representation (dict): Dictionary representation of the instance.

        Returns:
            BaseModel: An instance of BaseModel with attributes set according to the dictionary representation.
        """
        # Extract relevant attributes from the dictionary
        id = dict_representation['id']
        created_at = datetime.fromisoformat(dict_representation['created_at'])
        updated_at = datetime.fromisoformat(dict_representation['updated_at'])

        # Create a new instance of BaseModel with extracted attributes
        instance = cls()
        instance.id = id
        instance.created_at = created_at
        instance.updated_at = updated_at

        return instance

    def to_dict(self):
        """Return a dictionary representation of the instance.

        The dictionary includes all instance attributes and adds a __class__ key.
        The created_at and updated_at attributes are converted to ISO format strings.
        """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict

