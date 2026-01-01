import json
from datetime import date
import re
print(date.today())
try:
    with open('bank_data','r') as f:
        bank_data=json.load(f)
except (FileNotFoundError,json.JSONDecodeError):
    bank_data=[]






def valid_dob():
    while True:
        try:
            date_today=date.today()
            dob=input("Enter your date of birth: mm/dd/yy ").split('/')
            month=int(dob[0])
            day=int(dob[1])
            year=int(dob[2])

            if year<=date.today().year%100:
                year+=2000
            else:
                year+=1900

            birth_date=date(year,month,day)

            age=date_today.year-birth_date.year
            if age<18:
                print("You must be at least 18 years old.")
                continue
            return birth_date
        except ValueError:
            print("Please enter a valid date of birth.")



def valid_email(email):
    while True:
        email=input("Enter your email: ").strip()
        email_pattern=r'^[\w.-]+@([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
        if re.match(email_pattern,email):
            return email
        else:
            print("Please enter a valid email.")
            continue






with open('bank_data','w') as f:
    json.dump(bank_data,f,indent=4)






















