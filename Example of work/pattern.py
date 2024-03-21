# Start by using a variable to make * symbol
# Then use for loop to print * in range 1-10 using the if statement to increase the count by 1 until it reaches 5 *'s
# Then use the else statement to then use count/position [-1] to lower the * by 1 until end of pattern.

star = "*"
for i in range (1, 10):
    if i < 6:
        print (star)
        star = star + "*"
    else:
        star = star [:-1]
        print (star)
print ("*")