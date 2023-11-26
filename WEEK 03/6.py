op = int(input('Enter Number 1 for Celsius to Fahrenheit or enter ‘2’ for Fahrenheit to Celsius'))
try:
    op = int(op)
except ValuError as e:
    print("Please Enter a number")
    exit(1)

if op ==1:
    c=float(input('Enter Celsius value'))
    f = (c * 1.8) + 32
    print(f,'Fahrenheit')
elif op ==2:
    f=float(input('Enter Fahrenheit value'))
    c = (f - 32) / 1.8
    print(f,'Celsius')

else:
    print('Invalid Value')

          
         
