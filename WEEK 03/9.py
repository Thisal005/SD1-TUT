mark=int(input('Enter Your Marks'))
if mark<0 or mark>100:
    print('Invalid Marks')
else:
    if mark >= 70: 
        print('Exceptional result!') 
    elif mark >= 40: 
        print('Satisfactory result!') 
    else: 
        print('You have failed.') 
