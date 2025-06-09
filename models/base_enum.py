from enum import Enum

class BaseEnum(Enum):

    @classmethod
    def choices(cls):
        return [(item.name, str(item)) for item in cls]
    
    def __str__(self):
        return self.value
