
from field import Field
from datetime import datetime

class Birthday(Field):

    def __init__(self, value):
        if self.is_valid_birthday(value):
            super().__init__(value)
        else: 
            raise ValueError("Invalid birthday format")
    
    def is_valid_birthday(self, someString): 
        try: 
            datetime.strptime(someString, "%d.%m.%Y")
            return True
        except ValueError:
            return False
