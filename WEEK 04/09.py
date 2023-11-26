while True:
    try:
        menu = int(input("Enter Menu Number 1, 2, 3, or 4 to quit: "))

        if menu == 1:
            print("THIS IS MENU ONE")
        elif menu == 2:
            print("THIS IS MENU TWO")
        elif menu == 3:
            print("THIS IS MENU THREE")
        elif menu == 4:
            print("Exiting the menu.")
            break
        else:
            print("Invalid menu choice. Please enter 1, 2, 3, or 4.")

    except ValueError:
        print("Requires a valid integer! Please try again.")

        