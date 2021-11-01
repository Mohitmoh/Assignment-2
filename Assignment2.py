# Name: Assignment2.py
# Author: Mohit
# Date Created: October 31, 2021

# Description:
# This program take required input from user for Food delivery

print("-----WELCOME TO ARNOLD'S AMAZING EATS-----")

# taken user and address details from user
firstName = input("Enter your First Name : ")
lastName = input("Enter your Last Name : ")
streetNumber = input("Enter your Street Number : ")
streetName = input("Enter your Street Name : ")
unit = input("Enter your Unit : ")
city = input("Enter your City : ")
province = input("Enter your Province : ")
postalCode = input("Enter your Postal Code : ")
phoneNumber = input("Enter your Phone Number : ")

# taken order from user
dinnerItem1 = "Pizza"       #Dinner Items 
dinnerItem2 = "Bargger"
costItem1 = 10              # Cost of Dinner Item
costItem2 = 8

while True:           #infinte while loop
    while True:

        # printing list of dinner items 
        print("There are Two types of meals are available : \n{0:<25s}{1:<25s}{2:25s}\n{3:<25s}{4:<25s}${5:<25d}\n{6:<25s}{7:<25s}${8:<25d}".format('Sr. No.','Meals','Cost','1',dinnerItem1,costItem1,'2',dinnerItem2,costItem2))
        
        srNumber = int(input("which serial number meals you want ? "))
        
        # checking Sr. No. is correct or not 
        if srNumber == 1 or srNumber == 2:
           amount = int(input("Enter the amount of meals : "))
           break
        else:
           print("Please Enter correct serial no.")

    # priting order of user
    print("Your orders is : ",end ="")
    if srNumber == 1:
        print(dinnerItem1)
    elif srNumber ==2:
        print(dinnerItem2)
    
    # Confrimation from user about order
    confirm = input("Confrim your order Y/N ")
    if confirm.lower() == 'n':
        print("Go through order again")
        continue
    elif confirm.lower() == 'y':
        break


# Checking user is Student or Not 
while True:
    studentCheck = input("you get 10% discount if you are a student. You are a student Y/N ")
    if studentCheck.lower() == 'y' or studentCheck.lower() =='n':
        break
    else:
        print("select the correct option")

# Calculation for placing order
if srNumber == 1:
    itemPrice = costItem1*amount
elif srNumber == 2:
    itemPrice = costItem2*amount

# 10% discount if user is student 
# Calculation for user is student or not
if studentCheck.lower() == 'y':
    discount = itemPrice*0.1
else:
    discount = 0

subTotal = itemPrice - discount     # Sub Total 

# Calculation for 13% Tax 
tax = subTotal*0.13

# total prices 
totalAmount = subTotal - tax

# *********** printing recipts ***********

# printing user information
print("{} {}".format(firstName, lastName))
print("Address: {},{},{}".format(streetNumber, streetName, unit))
print("{:>9s}{},{},{}".format('',city, province, postalCode))
print("{:>40s}{:>20s}".format('Item','Item'))
print("{:<10s}{:>30s}{:>20s}{:>20s}".format('Order', 'Amt', 'Price', 'Total'))
print("{:-^80s}".format(''))

# another method for writing recipts
# print("\n{0} {1}\nAddress: {2},{3},{4}\n{14:>9s}{5},{6},{7}\n{8:>40s}{9:>20s}\n{10:<10s}{11:>30s}{12:>20s}{13:>20s}\n{14:-<10s}{14:->30s}{14:->20s}{14:->20s}".format(firstName,lastName,streetNumber,streetName,unit,city,province,postalCode,'Item','Item','Order','Amt','Price','Total',''))


# printing dinner item that selected by user and also printing some details about prices 
if srNumber == 1:
    print("{:<10s}{:>30d}{:>20s}{:>20s}\n".format(dinnerItem1,amount,'$'+str("{:.2f}".format(costItem1)),'$'+str("{:.2f}".format(itemPrice))))
else:
    print("{:<10s}{:>30d}{:>20s}{:>20s}\n".format(dinnerItem2,amount,'$'+str("{:.2f}".format(costItem2)),'$'+str("{:.2f}".format(itemPrice))))

# printing discount details if user is a student 
if studentCheck.lower() == 'y':
    print("{:<60s}{:>20s}".format('10% student savings','-$'+str("{:.2f}".format(discount))))
else:
    pass

# printing details about tax and total bill price 
print("{:>60s}{:>20s}\n{:>60s}{:>20s}\n{:>80s}\n{:>60s}{:>20s}".format('Sub Total','$'+str("{:.2f}".format(subTotal)),'Tax (13%)','$'+str("{:.2f}".format(tax)),'-------','TOTAL','$'+str("{:.2f}".format(totalAmount))))
