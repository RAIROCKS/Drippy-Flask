#Lists of bottle names
bottle_names =["Ice cool blue","Red and hot","Chill green","Relax rainbow","Black and bold","Humble purple",
"Aqua flask","Luxury Gold","Silvery simple","Orange hub","Clean White","Lovely pink"]
#Lists of bottle prices
bottle_prices=['60','65','65','62','55','62','66','69','47','69','49','52',]

#list to store ordered waterbottles
order_list= []

#list to store waterbottles prices
order_cost= []

#List to store order cost

def menu():
    number_bottles = 12

    for count in range(number_bottles) :
        print("{} {} ${:.2}" .format(count+1,bottle_names[count],bottle_prices[count]))

menu()

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
        print("{} ${:.2}" .format(bottle_names[waterbottle_ordered],bottle_prices[waterbottle_ordered]))
        num_waterbottles = num_waterbottles-1 







#Countdown until all waterbottle are ordered 


#Print order