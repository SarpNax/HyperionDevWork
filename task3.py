s_time = 0 # swimming time
r_time = 0 #competitors running time
c_time = 0 # cycling time
qf_time = 0 # Total Time
print ("Welcome to the county traithalon award calculator \nPlease enter the times for your 3 events in minutes:")
s_time = int (input ("Swimming time: "))
r_time = int (input ("Running time: "))
c_time = int (input ("Cycling time: "))

if s_time <= int(1): # to make sure the code can only be entered as numbers.
    print ("Please enter in minutes !")
if c_time <= int(1):
    print ("Please enter in minutes !")
if c_time <= int(1):
    print ("Please enter in minutes !")
else: # transfere the string from a letters to readable numbers
    s_time = int(s_time)
    r_time = int(r_time)
    c_time = int(c_time)
    int = qf_time = s_time + r_time + c_time
    print ("Your total time is " + str(qf_time))#total
#To find out if the sports man qualified. 
if qf_time > 111:   
    print("You have not qualified! ")
if qf_time < 100:
    print("Provincial Colours")
if (qf_time > 100) and (qf_time < 106):
    print ("Provincail Half Colours")
if (qf_time > 105) and (qf_time < 111):
    print ("Provincail Scroll")




