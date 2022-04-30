# Drippy flask program
# 20/02/22
# Bugs- Phone number input allows letters
# 20/03/22 Final printout is not printing customer details correctly
# 20/03/22 Some questions wont show up

import sys
import random
from random import randint
# Constants
LOW = 1 
HIGH = 2
# Setting the boundaries of the number limit 
# for the Ph number to 7 and 10 for the ph num
PH_LOW = 7
PH_HIGH= 10


# Lists 
# List of random names
names = ["Marlon","Peire","Fatimah",
        "Zara","Hannah","Yammy","Quin",
        "Gabriel","Karen","Eren"]
# Lists of bottle names
bottle_names =['Ice cool blue','Red and hot',
            'Chill green','Relax rainbow',
            'Black and bold','Humble purple',
            'Aqua flask','Luxury Gold',
            'Silvery simple','Orange hub',
            'Clean White','Lovely pink']
# Lists of bottle prices
bottle_prices=[60, 65, 65, 62, 55, 62, 66, 69, 47, 69, 49, 52,]
# list to store ordered waterbottles
order_list= []
# list to store waterbottles prices
order_cost= []
# Customer details dictionary
customer_details ={}

# Validates inputs to check if they are blank
# Takes question as parameter
# Returns response in title class if valid
def not_blank(question):
    valid = False
    while not valid: # While not false
        response=input(question) # Asks for input (string)
        if  response != "":
            return response.title()
            # if response not blank, it returns response in title class
        else:
            print("This cannot be blank")  # Prints error message
#Check string for name make sure its only alphabets
# Validtes inputs to check if they are an integer.
# Takes question as parameter
def check_string(question):
    while True: # sets up while loop     
        response = input(question) # asks for input(string)
        #Checks that everything in the response is a letter
        x = response.isalpha()
        if x == False: # If x is False prints error message 
            print("Input must only contain letters")
        else:
            return response.title() #if True returns response in title class

# Validates inputs to check if they are an integer
# Takes question as parameter
def val_int(low, high, question):
    # Defines code as val_int with low, high, question as parameter
    while True: # sets up while loop 
        try:  # While the function is true
            num = int(input(question)) # Asks thequestion
            if num >= low and num  <= high:
    # If input is greater or equal to low (1) and less than or equal to high (2)
                return num # Returns and accepts input 
            else: # If input is not the above
                print(f"Please Enter a number between {low} and {high}")
                # Asks for input again
        except ValueError:
            print ("That is not a valid number") # Prints error message
            print (f"Please enter a number between {low} and {high}")

# Check phone
# Validates input to check if they are a number
# Takes question as parameter
def check_phone(question, PH_LOW, PH_HIGH):
       # Defines code as check_phone with question, PH_LOW, PH_HIGH as parameter
    while True: # Sets up while loop 
        try:   # While the function is true
            #Prints the question
            num = int(input(question))
            test_num = num # Input equals variable
            count = 0  # Count set as 0
            while test_num >0: # While input is greater than 0
                test_num = test_num//10
                # Test_num is equal to test_num divided by 10
                count = count + 1  # Adds 1 to count
            # This will accept the number if the number is > than 7 or if it is < 10
            if count >= PH_LOW and count <=PH_HIGH:
                return str(num)  # Returns and accepts input
            else: # If input is not the above
            # Prints the statement if the number isnt between 7 and 10 digits
                print ("NZ phone numbers have between 7 and 10 digits")
                  #If value is not between 7 and 10 it will be error
        except ValueError:
            print ("Please enter numbers only") # Prints error message



# Welcome Message
def welcome():
    '''
    Purpose: To generate a random name from the list and print out
    a welcome message
    Parameters:None
    Returns:None
    '''
    num = randint(0,9) # Name of person is randomised
    
    name = (names[num]) # Name will be chosen by their number
# Prints Welcome TO DRIPPYFLASKS  with asterisks
    print("****** WELCOME TO DRIPPYFLASKS *****")
# Prints my name is (random name from list) with asterisks
    print("****** My name is", name ,"******")
# Prints message that they will helping the user make their order 
    print("****** I will be here to help you order your drippy flask/s ******")

# Menu for pickup or delivery
def order_type(): # Defines following code as order_type
    del_pick = "" # del_pick equals input
# The question that asks the customer to enter a number between the numbers 1 or 2 
    question = (f"Enter a number between {LOW} and {HIGH} ")
     # Prints messages
     # Prints message to user to indicate that Delivery equals to input (2)
    print ("Is your order for pickup or delivery?") 
    print ("For pick up please enter 1")
    print ("For delivery please enter 2")
    delivery = val_int(LOW, HIGH, question) # Delivery equals validated inpu
#Sets it up so the code will run the pickup function if customer chose number 2
    if delivery == 1:  # If Delivery equals input (1)
        print ("Pickup") # Prints pickup"
        del_pick="pickup" # del_pick equals pickup  
        pickup_info()  # pickup_info function
#Sets it up so the code will run the delivery function if customer chose number 2
    else:
        print ("Delivery")  # Prints "Delivery"
        delivery_info()  # delivery_info function
        del_pick = "delivery"  # del_pick equals Delivery
    return del_pick  # Returns and accepts inputs

#Pick up information - name and phone number
def pickup_info(): # Defines following code as pickup_info
    question = ("Please enter your name ")  # Asks user to enter their name
    customer_details ['name'] = check_string(question)
    # Validates the input of customer name
    print (customer_details ['name'])  # Prints customer's name

    question = ("Please enter your phone number ")
    # Asks user to enter their phone number
    customer_details ['phone'] = check_phone(question, PH_LOW, PH_HIGH)
    # print (customer_details['phone'])
    print (customer_details ['phone'])  
    print (customer_details)  # Prints customer's phone number

#Delivery Information - name address and phone
def delivery_info():  # Defines following code as delivery_info
    question = ("Please enter your name ") # Asks user to enter their name
    customer_details ['name'] = check_string(question)
    # Validates the input of customer name
    print (customer_details ['name']) # Prints customer's name

    question = ("Please enter your phone number ")
    # Asks user to enter their phone number
    customer_details ['phone'] = check_phone(question, PH_LOW, PH_HIGH)
    # Validates input of customer phone number
    print (customer_details ['phone'])  
    # Prints customer phone number

    question = ("Please enter your house number ")
    # Asks user to enter their house number
    customer_details ['house'] = not_blank(question)
    # Validates customer house number
    print (customer_details ['house'])  # Prints house number

    question = ("Please enter your street name ")
    # Asks user to enter their street name
    customer_details ['street'] = check_string(question)
    # Validates the input of street name
    print (customer_details ['street'])  # Prints street name

    question = ("Please enter your suburb ") # Asks user to enter their suburb
    customer_details ['suburb'] = check_string(question)
    # Validates the input of suburb
    print (customer_details ['suburb']) 
    # Prints customer's suburb 

# Waterbottle menu
def menu(): # Defines following code as menu
    number_bottles = 12  # Sets there are 12 waterbottles on the menu
    for count in range(number_bottles) : # For water bottle(s) ranged between 1 and 12
        print("{} {} ${:.2f}" .format(count+1,bottle_names[count],bottle_prices[count]))
        # Print the waterbottle menu with prices

#Choose total number of Waterbottles
#Waterbottle order - from menu - printed each pizza ordered with cast
#Stops users from ordering more than 5 waterbottles
def order_waterbottle(): # Defines following code as order_waterbottle
    #ask for total number of waterbottles for order
    num_waterbottles =0  # num_waterbottles equals 0
    NUM_LOW = 1  # Set Constant as 1
    NUM_HIGH = 5  # Set Constant as infinite
    MENU_LOW=1 # Set Constant as 1
    MENU_HIGH=12  # Set Constant as 12
    #The question that asks the customer to enter a number between the numbers 1 or 12
    question = (f"Enter a number between {NUM_LOW} and {NUM_HIGH} ")
    # Asks user to enter number between 1 and inf
    print("How many water bottles do you want to order?")
    # Prints how many waterbottle(s) do you want to order?
    num_waterbottles =val_int(NUM_LOW, NUM_HIGH, question)
    # num_waterbottles equals validated input

    #Choose waterbottle from menu
    #This next code's function will loop depending on the number the customer chooses
    for item in range (num_waterbottles): # For water bottle(s) between 1 and 12
        while num_waterbottles > 0: # While input is greater than 0
            print ("Please choose your waterbottles by entering the number from the menu")
            question = (f"Enter a number between {MENU_LOW} and {MENU_HIGH} ")
            # Prints Please choose your waterbottle(s) by entering the number from the menu
            waterbottle_ordered =val_int(MENU_LOW, MENU_HIGH, question)
            #This function is there to prevent the program from skipping the first item on the menu
            waterbottle_ordered = waterbottle_ordered-1
             # waterbottle_ordered equals waterbottle_ordered minus 1
            order_list.append(bottle_names[waterbottle_ordered])
            # waterbottle names get added to order list
            order_cost.append(bottle_prices[waterbottle_ordered])
            # waterbottle prices get added to order cost
            print("{} ${:.2f}" .format(bottle_names[waterbottle_ordered],bottle_prices[waterbottle_ordered]))
            # Print waterbottle(s) ordered with prices
            num_waterbottles = num_waterbottles-1 
             # num_waterbottles equals num_waterbottles minus 1

#Print order out _omfc;idomg of order os delivery or pickup and names and price of each pizza - total cost including any delivery charge
# names and price of each waterbottle- total cost including any delivery charge 
def print_order(del_pick):
    # Defines code as print_order(del_pick) with parameter
    print() # print blank line
    total_cost = sum(order_cost)  # The total cost (Adds up all waterbottle ordered)
    print("Your Details") # Print "Customer Details"
    if del_pick == "pickup":
        # if delivery type was pickup
        print ("Your Order is for pickup")
        # Print your order is ready for pickup
        print(f"Customer name: {customer_details['name']} \nCustomer phone: {customer_details['phone']}")
        # Prints customers name and customers phone
    elif del_pick == "delivery":
        print ("Your Order is for delivery a $5.00 delivery charge applies")
        # Prints message
        total_cost = total_cost + 9
        # Adds $9 to the total cost of food ordered
        print(f"Customer name: {customer_details['name']} \nCustomer phone: {customer_details['phone']}\nCustomer Address:{customer_details['house']} {customer_details['street']} {customer_details['suburb']} ")
         # print customers name, phone, address, house etc.
    print ()  # Print blank line
    print("Your Order Details") # Print your order is ready
    count = 0 # Set count to 0
    for item in order_list:  # for the items in the order list
        print ("Ordered: {} Cost ${:2}".format(item, order_cost[count]))
        # Print customers order and cost
        count = count+1 # Adds 1 to count
    print()  # Print blank space
    print("Total Order Cost") # Prints Total Order Cost
    print(f"${total_cost:.2f}") # Prints the total cost in $
    
# Ability to cancel or proceed with order
# Asks user to confirm their order
# Asks user to enter 1 or 2 to confirm or cancel
def confirm_cancel(): # Defines the following code as confirm_cancel
#The question that asks the customer to enter a number between the numbers 1 or 2 
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("Please Confirm your Order")  # Prints Please Confirm Your Order 
    print ("To confirm please enter 1 ") # Prints To Confirm Please Enter 1
    print ("To cancel please enter 2") # Prints To Cancel Please Enter 2
    print ()
    # Order for confirmation
    # If confirm equals 1
    # Order is confirmed with message
    confirm = val_int(LOW, HIGH, question) # Confirm equals validated input
    if confirm == 1: # If input equals 1
        print ("ORDER CONFIRMED") # Prints Order Confirmed
        print ("Your order has been sent to our production/factory")
        # Prints Your order has been sent to our kitchen
        print ("Your drippy and pretty hydroflask/waterbottle will be with your shortly")
        # Prints Your Delicious Food will be with you shortly
        new_exit() # Moves on to option for new order or exit the bot
                
    elif confirm == 2:
        print ("YOUR ORDER HAS BEEN CANCELLED")
        print ("You can restart your order or exit the BOT")
        new_exit()




# Option for new order or to exit 
# Asks user to enter between 1 and 2
# (1) equals start another order
# (2) equals exit the bot
def new_exit(): # Defines the following code as new_exit
    print()
#The question that asks the customer to enter a number between the numbers 1 or 2 
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("Do you want to start another order or exit?") 
    # Prints do you want to start another order? or exit?
    print ("To start another order please enter 1 ")
    # Prints to start another order, they must enter 1
    print ("To exit please enter 2")
    # Prints to exit the bot, they must enter 2
    confirm = val_int(LOW, HIGH, question) # Confirm equals validated input


    if confirm == 1:  # If input equals 1
        print ("New Order") # Prints 'Exit' message
        order_list.clear() # Clears the list of food names
        order_cost.clear() # Clears the costs of foods
        customer_details.clear()  # Clears the previous customer details
        main() #Main Function
    
    elif confirm == 2: # Else if confirm input equals 2
        print ("Exit") # Prints 'Exit' message
        order_list.clear()  # Clears the list of food names
        order_cost.clear() # Clears the costs of foods
        customer_details.clear() # Clears the previous customer details
        sys.exit()  # Exits the bot fully

 
#Main function
def main():# Define the following code as main
    '''
    Purpose: To run all functions in order that it is written
    Parameters:None
    Returns:None
    '''
    welcome()
    del_pick = order_type()
    menu()
    order_waterbottle()
#Del pick is the variable used for print order to run
    print_order(del_pick)
    confirm_cancel()


main()
