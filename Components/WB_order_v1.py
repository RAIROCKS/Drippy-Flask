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

num_waterbottles =int(input ("How many waterbottles do you want to order?"))

print (num_waterbottles)


#Choose waterbottle from menu
print ("Please choose your waterbottle by entering the number from the menu")
#This next code's function will loop depending on the number the customer chooses
for item in range (num_waterbottles):
    while num_waterbottles > 0:
        waterbottle_ordered = int(input())
        order_list.append(bottle_names[waterbottle_ordered])
        order_cost.append(bottle_prices[waterbottle_ordered])
        num_waterbottles = num_waterbottles-1 

print (order_list)
print (order_cost)





#Countdown until all waterbottle are ordered 


#Print order