birth_year = input('birth year: ')
age = 2024 - int(birth_year)
print(age)


weight_num = input('Weight: ')
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
     times = float(weight_num) * 0.45359237
     print("Weight in Kg: ", times)
elif unit.upper() == "L":
    times2 = float(weight_num) * 2.2046
    print("Weight in Lbs: ", times2)
else:
    print("NO")