#import math
import math
investment = True

while investment: #The loop section.
    print("Investment - to calculate the amount of interest you'll earn on your invesment")
    print("bond\t  - to calculate the amount you'll have to pay on a home loan")
    user_input = input("\n Enter either 'interest ' or 'bond from the menu above to proceed\n > ").lower()
# The calculation for the interest rate using math.pow .
    if user_input == "interest":
        customer_m = input("Please enter an amount (please use whole numbers) \n> ") # customers money.
        customer_i = input("Please enter the amount of interest payable ( Please use whole numbers)\n> ")#Customer interest.
        customer_pi = float(customer_i)/100 # formular for calculating interest%.
        customer_y = input("Please enter the years to invest\n> ")# customers year.
        interest_b = float(customer_m) * math.pow((1+float(customer_pi)), float(customer_y))  # interest value.
        print("The total amount of interest + investment is \n = " + str(interest_b))
        stop_prog = input("would you like to end program Y/N?\n >").upper()
        # statement breaking process.
        if stop_prog == "Y":
            investment = False
        else:
            continue
# The calculation for the bond repayment plan/interest.
    elif user_input == "bond":
        customer_hp = float(input("Please enter the value of the House/Flat\n>£ ")) # House/flat price.
        customer_i = float(input("Please enter the interest value (Whole numbers  please) \n> % "))
        customer_pi = (float(customer_i)/100) / 12 #bond monthly interest calculation.
        customer_mp = float(input("please put repayment duration in number of months/n (120(10 years),180(15 years) etc)\n> "))
        customer_r = (customer_pi * customer_hp) / ( 1 - (1 + customer_pi) ** (-customer_mp))
        print("Your monthly payments will be \n> " + str(customer_r)) # customers payments per month
        stop_prog = input("would you like to end the program Y/N?\n >").upper()
        if stop_prog == "Y":# statement breaking process.
            investment = False
        else:
            continue
    # if invalid input has been placed.
    else:
        print("Please try again")