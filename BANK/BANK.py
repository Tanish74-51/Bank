class Bank():
    def __init__(self,name,account_no,balance):
        self.name=name
        self.account_no=account_no
        self.balance=balance

    def show_balance(self):
        print(self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print('Invalid Input: Withdraw amount must be less than balance')
        else:
            self.balance=self.balance-amount
            print(f'Current amount: {self.balance}')
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f'Current amount: {self.balance}')

user_one=Bank('Harjot Singh Sodhi',123456789,100000)
user_two=Bank('Tanish pal Singh Sodhi',123498765,100000)

user_one.deposit(100)
user_two.withdraw(100)

























'''import json
try:
    with open('bank_data.json','r') as f:
        user_data=json.load(f)
except (FileNotFoundError,json.JSONDecodeError):
    user_data=[]

def to_dict(self):
    return {"name":self.name,
            "account_no":self.account_no,
            "balance":self.balance}
with open('bank_data.json','w') as f:
    json.dump(user_data,f)'''