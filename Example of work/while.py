# Set num with the inital input, then create while loop to repeat question.
# Then set if condition for -1
# To calaculate average number of entries, add vairable for total input added together and amount of inputs. When -1 entered divide total by count to reach an average.
num = int(input("please enter a number"))
count = 0
total = 0
while num != -1:
    count += 1
    total += num
    num = int(input("please enter a number"))
    if num == -1:
        break
average = (total/count)
print (num) 
print (average)

    

