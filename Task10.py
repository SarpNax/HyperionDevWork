Prog_repeat = True  # Repeating the calculation program
Prog_Cont = True  # Program loop variable
Prog_Read = True  # Read file boolean
answer_data = []  # List variable
while Prog_Read:  # Loop for New file or Old file.
    while True:
        try:  # exception handling
            print("Welcome to The Number Calculator!")
            Read_Cont = input("Would you like to read a file or create a new one? R/N\n >").upper()
            if Read_Cont == "R":
                old_text_file = input("please enter the name of the text file\n> ")
                try:  # To try and read an old file withing the same folder.
                    old_text_file = open(old_text_file, 'r+')
                    print(old_text_file.read())
                except FileNotFoundError:
                    print("The file {} does not exist".format(old_text_file))
            elif Read_Cont == "N":
                break  # To continue code
        finally:  # make sure the loop is broken.
            Prog_Read = False
while Prog_repeat:
    while Prog_Cont:  # loop beginning
        while True:  # Exception handling 1
            first_num = "0"  # ensure number resets to 0 after first loop
            sec_num = "0"  # ensure number resets to 0 after first loop
            try:
                first_num = input("Please enter the first number \n> ")
                first_num = int(first_num)  # exception handling
                break
            except ValueError:
                print("Please enter a Valid Entry")
        while True:  # Exception handling 2
            try:
                sec_num = input("Please enter the second number \n> ")
                sec_num = int(sec_num)
                break
            except ValueError:
                print("Please enter a Valid Entry")
# Code to allow for operations such as addition subtraction multiplication etc.
        operation = input(" please enter an operation \n 'x,-,/,+'> ")
        if operation == "-":
            answer = float(first_num) - float(sec_num)
            Prog_Cont = False  # breaking the loop for the whole program
            Prog_repeat = False
        elif operation == "+":
            answer = float(first_num) + float(sec_num)
            Prog_Cont = False
            Prog_repeat = False
        elif operation == "/":
            answer = float(first_num) / float(sec_num)
            Prog_Cont = False
            Prog_repeat = False
        elif operation == "x":
            answer = float(first_num) * float(sec_num)
            Prog_Cont = False
            Prog_repeat = False
        elif operation != ("-" or "+" or "/" or "x"):  # Exception handling of operations
            print("Please enter a valid entry")
# Set of Code to allow for repeat iterations of the simple calculator.
    print(str(answer))
    answer_text_list = (str(first_num), str(operation), str(sec_num), "=", str(answer))
    answer_data.append(answer_text_list)
    Prog_Check = input("Would you Like the program to continue? Y/N?\n> ").upper()
    if Prog_Check == "Y":
        print("Number of solutions >", len(answer_data))   # to show the number of answers they have
        Prog_repeat = True
        Prog_Cont = True
    else:
        break
Prog_repeat = False  # Repeating the calculation program
Prog_Cont = False  # Program loop variable
Prog_Read = False  # Read file boolean
new_file = input("Please enter the name of the file\n> ")
new_file_txt = new_file + ".txt"
file_obj = open(new_file_txt, "w+")  # modify the existing file
file_obj.write(str(answer_data))
print(file_obj)
print("thank you for using my calculator")
# This task was very hard and I did not understand why the function 'replace' and 'split' didn't work.
