is_hot = False
is_cold = False

if is_hot:
    print("Is's a hot day")
    print("Drink a lot of water")
elif is_cold: 
    print("It's a cold day")
    print("wear warm cloths")
else:
    print("It's a lovly day")
print("Enjoy your day")

price = 1000000
good_credit = False
bad_credit = True

if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: ${down_payment}")