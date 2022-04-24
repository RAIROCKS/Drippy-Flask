#Drippy flask program
import random
from random import randint

#Lists 
#List of random names
names = ["Marlon","Peire","Fatimah","Zara","Hannah","Yammy","Quin","Gabriel","Karen","Eren"]
#Lists of bottle names
bottle_names =['Ice cool blue','Red and hot','Chill green','Relax rainbow','Black and bold','Humble purple',
'Aqua flask','Luxury Gold','Silvery simple','Orange hub','Clean White','Lovely pink']
#Lists of bottle prices
bottle_prices=[60,65,65,62,55,62,66,69,47,69,49,52,]
#list to store ordered waterbottles
order_list= []
#list to store waterbottles prices
order_cost= []

 #Customer details dictionary
customer_details ={}

#Validates inputs to check if they are blank
def not_blank(question):
    valid = False
    while not valid:
        response=input(question)
        if  response != "":
            return response.title()
        else:
            print("This cannot be blank")


#Welcome Message
def welcome():
    '''
    Purpose: To generate a random name from the list and print out
    a welcome message
    Parameters:None
    Returns:None
    '''
    num = randint(0,9)
    name = (names[num])
    print ("****** WELCOME TO DRIPPYFLASKS *****")
    print("****** My name is", name ,"******")
    print("****** I will be here to help you order your drippy flask/s ******")

#Menu for pickup or delivery
def order_type():
    del_pick = ""
    print ("Is your order for pickup or delivery?") 
    print ("For pick up please enter 1 ")
    print ("For delivery please enter 2")
    while True:
        try:
            delivery = int(input("Please enter a number"))
            if delivery >= 1 and delivery  <= 2:
#Sets it up so the code will be delivery if customer chose number 2
                if delivery == 1: 
                    print ("Pickup")
                    del_pick="pickup"
                    pickup_info()
                    break
#Sets it up so the code will be delivery if customer chose number 2
                elif delivery == 2:
                    print ("Delivery")
                    #order_list.append("Delivery Charge")
                    #order_cost.append(5)
                    delivery_info()
                    del_pick = "delivery"
                    break
            else:
                print("The Number must be 1 or 2")
        except ValueError:
            print ("That is not a valid number")
            print ("Please enter 1 or 2")
    return del_pick

#Pick up information - name and phone number
def pickup_info():
    question = ("Please enter your name")
    customer_details ['name'] = not_blank(question)
    print (customer_details ['name']) 

    question = ("Please enter your phone number")
    customer_details ['phone'] = not_blank(question)
    print (customer_details ['phone'])  
    print (customer_details)
#Delivery Information - name address and phone
def delivery_info():
    question = ("Please enter your name ")
    customer_details ['name'] = not_blank(question)
    print (customer_details ['name']) 

    question = ("Please enter your phone number ")
    customer_details ['phone'] = not_blank(question)
    print (customer_details ['phone'])  
    
    question = ("Please enter your house number")
    customer_details ['house'] = not_blank(question)
    print (customer_details ['house'])  

    question = ("Please enter your street name")
    customer_details ['street'] = not_blank(question)
    print (customer_details ['street'])  

    question = ("Please enter your suburb")
    customer_details ['suburb'] = not_blank(question)
    print (customer_details ['suburb']) 

# Waterbottle menu
def menu():
    number_bottles = 12
    for count in range(number_bottles) :
        print("{} {} ${:.2f}" .format(count+1,bottle_names[count],bottle_prices[count]))

#Choose total number of Waterbottles
#Waterbottle order - from menu - printed each pizza ordered with cast
def order_waterbottle():
    #ask for total number of waterbottles for order
    num_waterbottles =0
    #Stops users from ordering more than 5 waterbottles
    while True:
        try:
            num_waterbottles =int(input ("How many waterbottles do you want to order?"))
            if num_waterbottles >=1 and num_waterbottles <=5:
                break
            else:
                print ("Your order must be between 1 and 5")
        except ValueError:
            print ("That is not a valid number")
            print ("Please enter a number between 1 to 5")
    print (num_waterbottles)
    #Choose waterbottle from menu
    #This next code's function will loop depending on the number the customer chooses
    for item in range (num_waterbottles):
        while num_waterbottles > 0:
            while True:
                try:
                    waterbottle_ordered =int(input ("Please choose your waterbottle by entering the number from the menu"))
                    if waterbottle_ordered >=1 and waterbottle_ordered <=12:
                        break
                    else:
                        print ("Your order must be between 1 and 12")
                except ValueError:
                    print ("That is not a valid number")
                    print ("Please enter a number between 1 to 12")
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
    
#Waterbottle options



#Option for new order or to exit

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


main()
