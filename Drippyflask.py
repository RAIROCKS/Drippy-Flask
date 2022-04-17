#Drippy flask program
import random
from random import randint

#List of random names
names = ["Marlon","Peire","Fatimah","Zara","Hannah","Yammy","Quin","Gabriel","Karen","Eren"]

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
def pickup():
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






#Main function
def main():
    '''
    Purpose: To run all functions in order that it is written
    Parameters:None
    Returns:None
    '''
    welcome()
    pickup()


main()
