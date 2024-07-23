try:    
    age = int(input("age: "))
    income = 2000
    risk = income / age
    if age >= 100:
        print("you are probably dead")
    elif age >=80 <=99:
        print("are you sure you know how to work a computer")
    else:
        print("you are " + str(age) + " years old")
except ZeroDivisionError:
    print("age can't be zero")
except ValueError:
    print('Plz type a number')
