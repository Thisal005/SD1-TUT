total = 0 
count = 0 


while True:
    score = int(input("Enter score, (Enter -9 to end): ") )
    if score == -9:
        average = float( total ) / count 
        print("You have entered",count,"scores")
        print("Your total is",total)
        print("Class average is", average)
        
    else:
        total += score
        count += 1