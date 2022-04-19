#Drippy flask program
import random
from random import randint

#Lists 
#List of random names
names = ["Marlon","Peire","Fatimah","Zara","Hannah","Yammy","Quin","Gabriel","Karen","Eren"]
#Lists of bottle names
bottle_names =["Ice cool blue","Red and hot","Chill green","Relax rainbow","Black and bold","Humble purple",
"Aqua flask","Luxury Gold","Silvery simple","Orange hub","Clean White","Lovely pink"]
#Lists of bottle prices
bottle_prices=['60','65','65','62','55','62','66','69','47','69','49','52',]


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
    print ("Is your order for pickup or delivery?") 
    print ("For pick up please enter 1 ")
    print ("For delivery please enter 2")
    while True:
        try:
            delivery = int(input("Please enter a number"))
            if delivery >= 1 and delivery  <= 2:
                if delivery == 1: 
                    print ("Pickup")
                    pickup_info()
                    break

                elif delivery == 2:
                    print ("Delivery")
                    delivery_info()
                    break
            else:
                print("The Number must be 1 or 2")
        except ValueError:
            print ("That is not a valid number")
            print ("Please enter 1 or 2")

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
        print("{} {} ${:.2}" .format(count+1,bottle_names[count],bottle_prices[count]))

#Choose total number of Waterbottles

#Waterbottle options

#Main function
def main():
    '''
    Purpose: To run all functions in order that it is written
    Parameters:None
    Returns:None
    '''
    welcome()
    order_type()
    menu()
  

main()
