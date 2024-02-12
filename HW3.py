# 1
from datetime import datetime as dtdt

dt_str = '22/11/93'
dt_obj = dtdt.strptime(dt_str, '%d/%m/%y')
current_date = dtdt.now()
diff = (current_date - dt_obj)
print(diff)

# 2
import random
lottery_nums = list(range(1, 30, 5))
random.shuffle(lottery_nums)

if any(number > 1000 or number < 1 for number in lottery_nums[:5]):
    print('[]')
else:
    print('Lucky Numbers: ', lottery_nums[:5])


# 3
user_num = input('Phone Number: ')

def normalize_phone(phone_number):
    # Remove spaces, hyphens, and parentheses
    cleaned_number = phone_number.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    
    # Check if the number starts with '+380', if not, add it
    if not cleaned_number.startswith("+380"):
        cleaned_number = "+380" + cleaned_number

    return cleaned_number

normalized_number = normalize_phone(user_num)
print("Нормалізований номер телефону для SMS-розсилки:", normalized_number)


# 4
import datetime as dt
from datetime import datetime as dtdt

users = [{'Name': 'Five Hargreeves', 'Birthday':'1989.10.01'}, {'Name':'Carl Gallagher', 'Birthday':'2002.01.12'}]

def get_upcoming_birthdays(users):
    tday = dtdt.today().date()
    bdays = []
    for user in users:
        brth_d = user['Birthday']
        brth_d = str(tday.year) + brth_d[4:]
        brth_d = dtdt.strptime(brth_d, '%Y.%m.%d').date()
        wday = brth_d.isoweekday()
        dbtwn_= (brth_d - tday).days
        if 0<=dbtwn_<7:
            if wday < 6:
                bdays.append({'Name': user['Name'], 'Birthday':brth_d.strftime('%Y.%m.%d')})
            else:
                if (brth_d + dt.timedelta(days = 1)).weekday()==0:
                    bdays.append({'Name': user['Name'], 'Birthday':(brth_d+dt.timedelta(days=1)).strftime('%Y.%m.%d')})
                elif (brth_d + dt.timedelta(days = 2)).weekday()==0:
                    bdays.append({'Name': user['Name'], 'Birthday':(brth_d+dt.timedelta(days=2)).strftime('%Y.%m.%d')})
            
    return bdays

print(get_upcoming_birthdays(users))
