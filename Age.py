# output = age of the user
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')

birthday = [int(x) for x in input().split('/')]
age = int(today[:4]) - birthday[0]

if birthday[1] > 12 or birthday[2] > 31:
    print('Wrong')
else:
    print(age)
