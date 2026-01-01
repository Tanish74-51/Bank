import json

try:
    with open('bank_data','r') as f:
        bank_data=json.load(f)
except (FileNotFoundError,json.JSONDecodeError):
    bank_data=[]









with open('bank_data','w') as f:
    json.dump(bank_data,f,indent=4)






















