n = input('Give me a number over 100:  ')
try:
     n = int(n)
except ValueError as e:
    print("Please Enter a number")
    exit(1)

n = int(n) 
if n <= 100: 
    print(n, 'is not over 100')
else:
    print(n,'Is over 100')
