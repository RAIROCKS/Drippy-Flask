#Asks customer if they want to confirm their order or cancel it
print ("Please Confirm your Order") 
print ("To confirm please enter 1 ")
print ("To cancel please enter 2")
while True:
    try:
        confirm = int(input("Please enter a number"))
        if confirm >= 1 and confirm  <= 2:
            if confirm == 1: 
                print ("ORDER CONFIRMED")
                break

            elif confirm == 2:
                print ("ORDER CANCELLED")
                break
        else:
            print("The Number must be 1 or 2")
    except ValueError:
        print ("That is not a valid number")
        print ("Please enter 1 or 2")