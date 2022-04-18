#Drippy flask program
import random
from random import randint

#List of random names
names = ["Marlon","Peire","Fatimah","Zara","Hannah","Yammy","Quin","Gabriel","Karen","Eren"]
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
                    break

                elif delivery == 2:
                    print ("Delivery")
                    break
            else:
                print("The Number must be 1 or 2")
        except ValueError:
            print ("That is not a valid number")
            print ("Please enter 1 or 2")

#Pick up information - name and phone number
def pickup():
    question = ("Please enter your name")
    customer_details ['name'] = not_blank(question)
    print (customer_details ['name']) 

    question = ("Please enter your phone number")
    customer_details ['phone'] = not_blank(question)
    print (customer_details ['phone'])  
    print (customer_details)


#Main function
def main():
    '''
    Purpose: To run all functions in order that it is written
    Parameters:None
    Returns:None
    '''
    welcome()
    order_type()
    pickup()

main()
