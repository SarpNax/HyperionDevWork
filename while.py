c_code = True     # to continue code
variable_total = 0  # total of variables added
entry_number = 0  # number of entries
v_collection = 0  # collection of variables

while c_code: # loop for the code
    variable_1 = input("Please enter a number: \n > ")
    float(entry_number) + 1
    if variable_1 == "-1":  # the breaking input.
        c_code = False
        variable_av = float(v_collection) / float(num_entry)
        print("The average number of your entries is > " + str(variable_av))
    else:   # continuation of the loop.
        num_entry = entry_number + 1
        v_collection = float(variable_1) + float(variable_total)   # average of the formula.