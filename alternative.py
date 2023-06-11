
string1 = "I am learning to code"
string2 = ""  # Define string before use

for i, x in enumerate(string1):  # to make sure its individual letters
    if i % 2 == 0:
        string2 += string1[i].upper()  # upper case letter
    else:
        string2 += string1[i].lower()  # lower case letter
print(string2)
string3 = "I am learning to code"
string_split = string3.split()  # To store the split string -creates a list

string4 = ""  # Define string before use
for i in range(len(string_split)):
    if i % 2 == 0:
        string4 += string_split[i].upper() + " "  # if the item is divisible by 2 it will be upper case
    else:
        string4 += string_split[i].lower() + " "  # lower case conversion
print(string4)
