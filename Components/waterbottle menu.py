bottle_names =["Ice cool blue","Red and hot","Chill green","Relax rainbow","Black and bold","Humble purple",
"Aqua flask","Luxury Gold","Silvery simple","Orange hub","Clean White","Lovely pink"]

bottle_prices=['60','65','65','62','55','62','66','69','47','69','49','52',]

def menu():
    number_bottles = 12



    for count in range(number_bottles) :
        print("{} {} ${:.2}" .format(count+1,bottle_names[count],bottle_prices[count]))

menu()

