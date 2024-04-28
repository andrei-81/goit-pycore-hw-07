from field import Field

class Phone(Field):

    def __init__(self, value):
        if self.is_valid_phone(value):
            super().__init__(value)
        else: 
            raise TypeError("Invalid phone number format")
    
    def is_valid_phone(self, number): 
        #len 3 for testing
        return len(str(number)) in [3, 10] and str(number).isdigit() 
