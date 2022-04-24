#list to store ordered waterbottles
order_list= ["Ice cool blue","Red and hot","Chill green","Relax rainbow",]
#list to store waterbottles prices
order_cost= [60,65,65,62]

cust_details = {'name': 'Fatimah','phone':'0223922479','house':'45','street':'Novidgrad','suburb':'Howick'}

def print_order():
    total_cost = sum(order_cost)
    print("Customer Details")
    print(f"Customer name: {cust_details['name']}\nCustomer phone:{cust_details['phone']}\nCustomer Address:{cust_details['house']} {cust_details['street']} {cust_details['suburb']} ")
    print ()
    print("Order Details")
    count = 0
    for item in order_list:
        print ("Ordered: {} Cost ${:2}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Total Order Cost")
    print(f"${total_cost:.2f}")

print_order