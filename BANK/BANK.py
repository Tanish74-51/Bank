import json

try:
    with open('bank_data','r') as f:
        bank_data=json.load(f)
except (FileNotFoundError,json.JSONDecodeError):
    bank_data=[]







#name\dob\mobile\email\address\occupation\income_range

with open('bank_data','w') as f:
    json.dump(bank_data,f,indent=4)


#name
def name_input():
    name=input("ENTER YOUR NAME:")
    while not name.isalpha():
        name=input("ENTER VALID NAME:")
    return name


#address 
def address():
    input_state=input("STATE: ").lower()
    input_district=input("DISTRICT: ").lower()
    state=["jammu and kashmir", "ladakh", "himachal pradesh", "punjab",
            "haryana", "uttarakhand", "uttar pradesh", "rajasthan", "delhi", "chandigarh"]
    dist=["agar", "agra", "ahmednagar", "ajmer", "aligarh", "alipurduar", "almora", "ambala", "amethi", "amritsar", "anantnag", "araria", "auraiya", "ayodhya",
"baghpat", "bahraich", "ballia", "balrampur", "bandipora", "banda", "barabanki", "baramulla", "bareilly", "basti", "bhiwani", "bijnor", "bikaner", "bilaspur", "bulandshahr",
"chamba", "chandigarh", "charkhi dadri", "chitrakoot", "churu",
"dausa", "dehradun", "delhi central", "delhi east", "delhi new", "delhi north", "delhi north east", "delhi north west", "delhi shahdara", "delhi south", "delhi south east", "delhi south west", "delhi west", "doda",
"etah", "etawah",
"faridabad", "farrukhabad", "fatehabad", "fatehpur", "firozabad",
"ganderbal", "ghaziabad", "ghazipur", "gonda", "gorakhpur", "gurgaon",
"hamirpur", "hardoi", "haridwar", "hathras", "hisar", "hoshiarpur",
"jaisalmer", "jammu", "jaunpur", "jhajjar", "jhansi", "jind", "jodhpur",
"kangra", "kannauj", "kanpur dehat", "kanpur nagar", "kathua", "kaushambi", "khandwa", "kishtwar", "kullu", "kupwara", "kurukshetra",
"kargil", "leh",
"lakhimpur kheri", "lalitpur", "lucknow",
"mahendragarh", "mathura", "meerut", "mewat", "moradabad", "muzaffarnagar",
"nainital", "noida",
"pauri garhwal", "pilibhit", "poonch", "prayagraj", "pulwama",
"rajouri", "rampur", "reasi", "rewari", "rohtak",
"saharanpur", "samba", "shimla", "shopian", "sikar", "sirsa", "sitapur", "sirmaur", "srinagar",
"tehri garhwal", "udhampur", "una",
"varanasi",
"yamunanagar"]    
    while input_state not in state:
        input_state=input("VALID STATE: ").lower()
    while input_district not in dist:
         input_district=input("DISTRICT: ").lower()
    return (input_state,input_district)


#income range
def income():
    income_range = {
        0:"below 10000",
        1:"10000-20000",
        2:"20001-30000",
        3:"30001-50000",
        4:"50001-75000",
        5:"75001-100000",
        6:"above 100000"}
    print("\nYOUR MONTHLY INCOME RANGE:")
    for key,value in income_range.items():
        print(f"{key}.{value}")
    choice=(input("ENTER YOUR CHOICE:"))
    while True:
        try:
            choice = int(input("ENTER OPTION (1-7): "))
            if 1 < choice <len(income_range):
                return income_range[choice]
            else:
                print("PLEASE SELECT A VALID OPTION (1-7)")
        except ValueError:
            print("PLEASE ENTER A NUMBER ONLY")

income()









