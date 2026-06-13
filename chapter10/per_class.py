#### building of car class
class car:
    def __init__(self, name, color, engine):
        self.name = name
        self.color = color
        self.engine = engine
        pass

    def intro (self):
        print(f"My car is {self.name} with {self.engine} engine.")

    def start (self):
        print(f"{self.name} engine is starting")

    def brake(self):
        print(f"{self.name} speed is halt")

car1 = car('Toyota','Blue', 'V4')
car2 = car('Volvo','red', 'V6')
car3 = car("Benz", 'white','V8')
car1.intro()
car2.brake()
car3.start()


### building of accountbalance class
class Bankacct:
    def __init__(self,name,balance=0):
        self.name = name
        self.__balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"{self.name} a sum of #{amount} is deposited into your account. Your new balance: #{self.__balance}")
        else:
            print("Deposited amount must be positive")

    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient funds")
            return False

        elif amount <=0:
            print("Withdrawal amount must be positive")
            return False
           
        else:
            self.__balance -= amount
            print(f"{self.name} a sum of #{amount} is withdrawn. Your new balance: #{self.__balance}")
            return True

    def checkbalance(self):
        print(f"{self.name}'s balance: #{self.__balance}")

    def transfer(self, amount, recipient_acct):
        print(f"\nTransferring #{amount} from {self.name} to {recipient_acct.name}.")

        if self.withdraw(amount):
            recipient_acct.deposit(amount)
            print("Transfer successful")

        elif amount <=0:
            print("Tranfer amount must be positive")

        elif amount >= self.__balance:
            print("Insufficient funds")

        else:
            print("Transfer successful")



acct1 = Bankacct("Adekanmi",100000)
acct2 = Bankacct('Otedola',)
acct3 = Bankacct('Dangote',1000000)

acct1.checkbalance()
acct2.deposit(100000)
acct3.transfer(1200000,acct2)
acct3.checkbalance()
acct2.checkbalance()
