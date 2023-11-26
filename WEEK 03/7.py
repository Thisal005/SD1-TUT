cost = int(input('Enter Your cost'))
sat = int(input('Enter  satisfaction level using ratings: 1 = Totally satisfied, 2 = Satisfied, 3 = Dissatisfied'))
if sat == 1:
    total = cost*20/100
elif sat == 2:
    total = cost*15/100
else :
     total = cost*10/100

print(total)
