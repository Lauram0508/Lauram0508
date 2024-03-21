num1 = input("time for swimming in minutes?")
num2 = input("time for running in minutes?")
num3 = input("time for cycling in minutes?")
num1 = (int(num1))
num2 = (int(num2))
num3 = (int(num3))
total = (num1 + num2 + num3)
print (total)
if total <100:
    print ("you have won the award provincial colours")
elif total >= 101 and total <= 105:
    print ("you have won the award provincial half colours")
elif total >= 110 and total <= 106:
    print ("you have won the provincial scroll")
elif total >111:
    print ("you have won no award")