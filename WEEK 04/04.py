total = 0

for x in range(5):

    while True:
        num = input("Enter a number: ")
        try:
            n = int(num)
            total += n  
            break

        except ValueError:
            print("Requires a valid integer! Please try again.")

print("Your total is", total)
