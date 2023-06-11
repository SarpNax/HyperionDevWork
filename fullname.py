
full_name = input ("Please enter your full name: ") 
letter_count = len(full_name) # string for the number of letters 
if letter_count == 0: #first parameter
    print ("You haven't entered anything please enter your fullname")
elif letter_count <= 4: # second parameter
    print ("please make sure thay you have entered your name and surname.")
elif letter_count >= 25: # third parameter
    print ("you have entered more than 25 Characters. Please make sure that you have only entered your full name.")
else:   # the statement when conditions are not met for the other statements. 
    print ("Thank you for entering your full name.")