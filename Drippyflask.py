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
# Setting the boundaries of the number limit for the Ph number to 7 and 10 for the ph num
PH_LOW = 7
PH_HIGH= 10


# Lists 
# List of random names
names = ["Marlon","Peire","Fatimah",
        "Zara","Hannah","Yammy","Quin",
        "Gabriel","Karen","Eren"]
# Lists of bottle names
bottle_names =['Ice cool blue','Red and hot','Chill green',
            'Relax rainbow','Black and bold','Humble purple',
            'Aqua flask','Luxury Gold','Silvery simple',
            'Orange hub','Clean White','Lovely pink']
# Lists of bottle prices
bottle_prices=[60, 65, 65, 62, 55, 62, 66, 69, 47, 69, 49, 52,]
# list to store ordered waterbottles
order_list= []
# list to store waterbottles prices
order_cost= []

# Customer details dictionary
customer_details ={}

# Validates inputs to check if they are blank
def not_blank(question):
    valid = False
    while not valid:
        response=input(question)
        if  response != "":
            return response.title()
        else:
            print("This cannot be blank")
#Check string for name make sure its only alphabets
def check_string(question):
    while True:
        response = input(question)
        #Checks that everything in the response is a letter
        x = response.isalpha()
        if x == False:
            print("Input must only contain letters")
        else:
            return response.title()

# Validates inputs to check if they are an integer
def val_int(low, high, question):
    while True:
        try:
            num = int(input(question))
            if num >= low and num  <= high:
                return num
            else:
                print(f"Please Enter a number between {low} and {high}")
        except ValueError:
            print ("That is not a valid number")
            print (f"Please enter a number between {low} and {high}")

# Check phone
def check_phone(question, PH_LOW, PH_HIGH):
    while True:
        try:
            #Prints the question
            num = int(input(question))
            test_num = num
            count = 0
            while test_num >0:
                test_num = test_num//10
                count = count + 1
            # This will accept the number if the number is > than 7 or if it is < 10
            if count >= PH_LOW and count <=PH_HIGH:
                return str(num)
            else:
            # Prints the statement if the number isnt between 7 and 10 digits
                print ("NZ phone numbers have between 7 and 10 digits")
                

        except ValueError:
            print ("Please enter numbers only")



# Welcome Message
def welcome():
    '''
    Purpose: To generate a random name from the list and print out
    a welcome message
    Parameters:None
    Returns:None
    '''
    num = randint(0,9)
    name = (names[num])
    print("****** WELCOME TO DRIPPYFLASKS *****")
    print("****** My name is", name ,"******")
    print("****** I will be here to help you order your drippy flask/s ******")

# Menu for pickup or delivery
def order_type():
    del_pick = ""
# The question that asks the customer to enter a number between the numbers 1 or 2 
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("Is your order for pickup or delivery?") 
    print ("For pick up please enter 1")
    print ("For delivery please enter 2")
    delivery = val_int(LOW, HIGH, question)
#Sets it up so the code will run the pickup function if customer chose number 2
    if delivery == 1: 
        print ("Pickup")
        del_pick="pickup"
        pickup_info()
#Sets it up so the code will run the delivery function if customer chose number 2
    else:
        print ("Delivery")
        delivery_info()
        del_pick = "delivery"
    return del_pick

#Pick up information - name and phone number
def pickup_info():
    question = ("Please enter your name ")
    customer_details ['name'] = check_string(question)
    print (customer_details ['name']) 

    question = ("Please enter your phone number ")
    customer_details ['phone'] = check_phone(question, PH_LOW, PH_HIGH)
    print (customer_details ['phone'])  
    print (customer_details)
#Delivery Information - name address and phone
def delivery_info():
    question = ("Please enter your name ")
    customer_details ['name'] = check_string(question)
    print (customer_details ['name']) 

    question = ("Please enter your phone number ")
    customer_details ['phone'] = check_phone(question, PH_LOW, PH_HIGH)
    print (customer_details ['phone'])  
    
    question = ("Please enter your house number ")
    customer_details ['house'] = not_blank(question)
    print (customer_details ['house'])  

    question = ("Please enter your street name ")
    customer_details ['street'] = check_string(question)
    print (customer_details ['street'])  

    question = ("Please enter your suburb ")
    customer_details ['suburb'] = check_string(question)
    print (customer_details ['suburb']) 

# Waterbottle menu
def menu():
    number_bottles = 12
    for count in range(number_bottles) :
        print("{} {} ${:.2f}" .format(count+1,bottle_names[count],bottle_prices[count]))

#Choose total number of Waterbottles
#Waterbottle order - from menu - printed each pizza ordered with cast
#Stops users from ordering more than 5 waterbottles
def order_waterbottle():
    #ask for total number of waterbottles for order
    num_waterbottles =0
    NUM_LOW = 1
    NUM_HIGH = 5
    MENU_LOW=1
    MENU_HIGH=12
    #The question that asks the customer to enter a number between the numbers 1 or 12
    question = (f"Enter a number between {NUM_LOW} and {NUM_HIGH} ")
    print("How many water bottles do you want to order?")
    num_waterbottles =val_int(NUM_LOW, NUM_HIGH, question)

    #Choose waterbottle from menu
    #This next code's function will loop depending on the number the customer chooses
    for item in range (num_waterbottles):
        while num_waterbottles > 0:
            print ("Please choose your waterbottles by entering the number from the menu")
            question = (f"Enter a number between {MENU_LOW} and {MENU_HIGH} ")
            waterbottle_ordered =val_int(MENU_LOW, MENU_HIGH, question)
            #This function is there to prevent the program from skipping the first item on the menu
            waterbottle_ordered = waterbottle_ordered-1
            order_list.append(bottle_names[waterbottle_ordered])
            order_cost.append(bottle_prices[waterbottle_ordered])
            print("{} ${:.2f}" .format(bottle_names[waterbottle_ordered],bottle_prices[waterbottle_ordered]))
            num_waterbottles = num_waterbottles-1 

#Print order out _omfc;idomg of order os delivery or pickup and names and price of each pizza - total cost including any delivery charge
def print_order(del_pick):
    print()
    total_cost = sum(order_cost)
    print("Your Details")
    if del_pick == "pickup":
        print ("Your Order is for pickup")
        print(f"Customer name: {customer_details['name']} \nCustomer phone: {customer_details['phone']}")
    elif del_pick == "delivery":
        print ("Your Order is for delivery a $5.00 delivery charge applies")
        total_cost = total_cost + 5
        print(f"Customer name: {customer_details['name']} \nCustomer phone: {customer_details['phone']}\nCustomer Address:{customer_details['house']} {customer_details['street']} {customer_details['suburb']} ")
    print ()
    print("Your Order Details")
    count = 0
    for item in order_list:
        print ("Ordered: {} Cost ${:2}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Total Order Cost")
    print(f"${total_cost:.2f}")
    
# Ability to cancel or proceed with order
def confirm_cancel():
#The question that asks the customer to enter a number between the numbers 1 or 2 
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("Please Confirm your Order") 
    print ("To confirm please enter 1 ")
    print ("To cancel please enter 2")
    print ()

    confirm = val_int(LOW, HIGH, question)
    if confirm == 1: 
        print ("ORDER CONFIRMED")
        print ("Your order has been sent to our production/factory")
        print ("Your drippy and pretty hydroflask/waterbottle will be with your shortly")
        new_exit()
                
    elif confirm == 2:
        print ("YOUR ORDER HAS BEEN CANCELLED")
        print ("You can restart your order or exit the BOT")
        new_exit()




#Option for new order or to exit
def new_exit():
    print()
#The question that asks the customer to enter a number between the numbers 1 or 2 
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("Do you want to start another order or exit?") 
    print ("To start another order please enter 1 ")
    print ("To exit please enter 2")
    confirm = val_int(LOW, HIGH, question)

    if confirm == 1: 
        print ("New Order")
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        main()
    
    elif confirm == 2:
        print ("Exit")
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        sys.exit()

 
#Main function
def main():
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
