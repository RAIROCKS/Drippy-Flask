#list to store ordered waterbottles
order_list= ["Ice cool blue","Red and hot","Chill green","Relax rainbow",]
#list to store waterbottles prices
order_cost= ['60','65','65','62',]

cust_details = {'name': 'Fatimah','phone':'0223922479','house':'45','street':'Novidgrad','suburb':'Howick'}



#print("\n",cust_details['name'],"\n",cust_details['phone'],"\n",cust_details['house'],"\n",cust_details['street'],"\n",cust_details['suburb'])
#print("\n Customer name: {} Customer phone:\n{} Customer House number:\n{} Customer street name:\n{} Customer suburb:\n{}" .format (cust_details['name'],cust_details['phone'],cust_details['house'],cust_details['street'],cust_details['suburb']))

print (f"{cust_details['name']} {cust_details['phone']} {cust_details['house']} {cust_details['street']} {cust_details['suburb']} ")


count = 0
for item in order_list:
    print ("Ordered: {} Cost ${:2}".format(item, order_cost[count]))
    count = count+1

