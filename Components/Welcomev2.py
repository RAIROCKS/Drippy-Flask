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


def main():
    '''
    Purpose: To run all functions
    Parameters:None
    Returns:None
    '''
    welcome()


main()
