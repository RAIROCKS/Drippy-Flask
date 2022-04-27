def check_phone(question, ph_low, ph_high):
    while True:
        try:
            #Prints the question
            num = int(input(question))
            test_num = num
            count = 0
            while test_num >0:
                test_num = test_num//10
                count = count + 1
            # This will accept the number if the number is > than 7 or if it is < 10
            if count >= ph_low and count <=ph_high:
                return str(num)
            else:
            # Prints the statement if the number isnt between 7 and 10 digits
                print ("NZ phone numbers have between 7 and 10 digits")
                

        except ValueError:
            print ("Please enter numbers only")
# Setting the boundaries of the number limit for the Ph number to 7 and 10 
ph_low = 7
ph_high = 10
question = ("Please enter your phone number ")

phone = check_phone(question, ph_low, ph_high)
print(phone)