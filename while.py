i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Done")


# guessing game 
print('you have 3 chances to gues the right number')
ready = input('are you ready? yes-no: ')

if ready.lower()== 'no':
    print('ok next time')

else:
    secret_num = 9
    count = 0
    limit = 3

    while count < limit:
        guess = int(input('Guess: '))
        count +=1
        if guess == secret_num:
            print('you win')
            break
    else:
        print('you lost')

# car game
command = ""
car_started = False
car_stopped = False
while True: 
    command = input("> ").lower()
    if command == "start":
        if car_started:
            print('car is already started')
        else:
            print('car has started')
        car_started = True
        car_stopped = False
    elif command == "stop":
        if car_stopped:
            print('the car is already stopped')
        else:
            print('car has stopped')
        car_stopped = True
        car_started = False
    elif command == "help":
        print("""
start-to start car
stop-to stop car
quit to exit
        """)
    elif command == "quit":
        break 
    else:
        print('I do not undersand')