#list to store ordered waterbottles
order_list= ["Ice cool blue","Red and hot","Chill green","Relax rainbow",]
#list to store waterbottles prices
order_cost= ['60','65','65','62',]

count = 0
for item in order_list:
    print ("Ordered: {} Cost ${:2}".format(item, order_cost[count]))
    count = count+1

