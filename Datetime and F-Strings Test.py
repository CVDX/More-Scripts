import datetime

two = datetime.date(2022,9,11)
three = datetime.date(1914,6,23)
four = datetime.date(2050,10,20)

print("Pick a number from 1-10. Then I will give a date.")
numbera = float(input())
print("You have picked " + str(numbera))

if(numbera == 1):
    print(datetime.time())
if(numbera == 2):
    print(f"{two:%A, %b %d, %Y}")
if(numbera == 3):
    print(f"{three:%Y, %x}")
if(numbera > 4):
    print(f"{four:%x}")
if(numbera > 11):
    print("YOU DIDNT FOLLOW MY DIRECTIONS")