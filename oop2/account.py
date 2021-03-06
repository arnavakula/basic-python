'''
account is the object
attributes: init balance, 
instance vars: filepath, balance
hierarchy:
    Class
    (Sub) class
    Data member
        Class var independent to all objects
        Instance var of self independent to object
    Doc string (class description """""") accesed with .__doc__
    Constructor
Methods
'''
class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as f:
            self.balance = int(f.read())

    def get_balance(self):
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= int(amount)
        self.commit()
    
    def deposit(self, amount):
        self.balance += int(amount)
        self.commit()

    def commit(self):
        with open(self.filepath, 'w') as f:
            f.write(str(self.balance))

class CheckingAccount(Account):
    """This class handles checking accounts""" #doc string

    type = 'checking' #class var
    
    def __init__(self, filepath):
        super().__init__(filepath) #no self needed
        self.user = 'Arnav' #can add additional instance vars
    
    def transfer(self, amount, account):
        self.balance -= amount
        account += amount
        self.commit()

acc1 = Account('balance.txt')
acc1.deposit(100)
print(acc1.balance)

cacc1 = CheckingAccount('balance.txt')
cacc1.deposit(100)
print(cacc1.balance)
print(cacc1.__doc__)