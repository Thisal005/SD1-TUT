import random

print("WELCOME TO GUESS NUMBER")
comnum = random.randint(1,20)
while True: 
    num = input("Enter your Number (1-20): ")
    try:
        num = int(num) 
    except ValueError:
        print("Please enter a valid number.")
        continue
    if num == comnum:
        print(num, "was correct")
        break
    elif num < comnum:
        print("Too low. Try a higher number.")
    else:
        print("Too high. Try a lower number.")
