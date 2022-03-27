import random, string, os
os.system("cls")
class Password(object):
    def __init__(self,lower ,upper, digits, symbols, length):
        self.lower = string.ascii_lowercase if lower == True else ""
        self.upper = string.ascii_uppercase if upper == True else ""
        self.digits = string.digits if digits == True else ""
        self.symbols = string.punctuation if symbols == True else ""
        self.length = length
    def create(self):
        password = self.lower+self.upper+self.digits+self.symbols
        return "".join(random.choices(password, k=self.length)) if password else ""
