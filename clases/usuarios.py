import random


class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.id = random.randint(000, 999)
        self.loans = []
    
    def register_loan(self, loan):
        self.loan