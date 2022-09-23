while True:
    yob = int (input("enter your year of birth:"))
    if yob > 0 and yob <2022:
       break
max_age=160
age=2022-yob
if age> max_age:
    print (f"please stop playing!")
else:
    print(f"you are {age}years old!")
    