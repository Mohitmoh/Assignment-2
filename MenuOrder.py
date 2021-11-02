# Name: Assignment2.py
# Author: Mohit
# Date Created: October 31, 2021

# Description:
# This program take required input from user for Food delivery

# Function: userDetails
# Description: will take inputs from user 
# Parameters: 
#          none
# Return value:
#          userDetails: details of user
def userDetails():
    userDetails = []  # list for adding details of user
    userDetails.append(input("Enter your First Name : "))
    userDetails.append(input("Enter your Last Name : "))
    userDetails.append(input("Enter your Street Number : "))
    userDetails.append(input("Enter your Street Name : "))
    userDetails.append(input("Enter your Unit : "))
    userDetails.append(input("Enter your City : "))
    userDetails.append(input("Enter your Province : "))
    userDetails.append(input("Enter your Postal Code : "))
    userDetails.append(input("Enter your Phone Number : "))
    return userDetails

# Function: listItem
# Description: will print list of dinner item
# Parameters: 
#          dinnerItem1 : name of 1st dinner item
#          dinnerItem2 : name of 2nd dinner item
#          costItem1   : cost of 1st dinner item
#          costItem2   : cost of 2nd dinner item 
# Return value:
#           none

def listItem(dinnerItem1, dinnerItem2, costItem1, costItem2):
    print("There are Two types of meals are available : \n{0:<25s}{1:<25s}{2:25s}\n{3:<25s}{4:<25s}${5:<25d}\n{6:<25s}{7:<25s}${8:<25d}".format(
        'Sr. No.', 'Meals', 'Cost', '1', dinnerItem1, costItem1, '2', dinnerItem2, costItem2))

# Function: srNumber
# Description: will take the input of Sr. Number for dinner item
# Parameters: 
#          none 
# Return value:
#           Sr. number 
def srNumber():
    return int(input("which serial number meals you want ? "))

# Function: orderPrint
# Description: will print order details
# Parameters: 
#          srNumber : Sr. number chosed by user
#          dinnerItem1 : name of 1st dinner item
#          dinnerItem2 : name of 2nd dinner item
# Return value:
#           none
def orderPrint(srNumber,dinnerItem1,dinnerItem2):
    print("Your orders is : ", end="")
    if srNumber == 1:
        print(dinnerItem1)
    elif srNumber == 2:
        print(dinnerItem2)

# Function: studentCheck
# Description: will check user is student or not
# Parameters: 
#          None
# Return value:
#          studentCheck : user is student or not
def studentCheck():
    studentCheck = input("you get 10% discount if you are a student. You are a student Y/N ")
    if studentCheck.lower() == 'y' or studentCheck.lower() == 'n':
        return studentCheck
    else:
        print("select the correct option")
        studentCheck()

# Function: itemPrice
# Description: will calculate price of total item
# Parameters: 
#          srNumber : Sr. Number
# Return value:
#          itemPrice: price of total item
def itemPrice(costItem1,costItem2,amount):
    if srNumber == 1:
        itemPrice = costItem1*amount
    elif srNumber == 2:
        itemPrice = costItem2*amount
    return itemPrice

# Function: discount
# Description: will calculate discount if user is student
# Parameters: 
#          studentCheck: check user is student or not
# Return value:
#          discount: discount for student
def discount(studentCheck,itemPrice):
    # 10% discount if user is student
    # Calculation for user is student or not
    if studentCheck.lower() == 'y':
        discount = itemPrice*0.1
    else:
        discount = 0
    return discount


# Function: subTotal
# Description: will calculate sub total
# Parameters: 
#          itemPrice: price of total item
#          discount: discount for student
# Return value:
#          subTotal: sub total
def subTotal(itemPrice,discount):
    subTotal = itemPrice - discount     # Sub Total
    return subTotal

def tax(subTotal):
    # Calculation for 13% Tax
    tax = subTotal*0.13
    return tax

def totalAmount(subTotal,tax):
    # total prices
    totalAmount = subTotal + tax
    return totalAmount

# Function: userInformation
# Description: will print information of user
# Parameters:
#       firstName: first Name 
#       lastName: last name
#       streetNumber: street number
#       streetName: street name
#       unit: unit
#       city: city
#       province : province
#       postalCode: postal code
def userInformation(userDetails):
    print("{} {}".format(userDetails[0], userDetails[1]))
    print("Address: {},{},{}".format(userDetails[2], userDetails[3], userDetails[4]))
    print("{:>9s}{},{},{}".format('', userDetails[6], userDetails[7], userDetails[8]))
    print("{:>40s}{:>20s}".format('Item', 'Item'))
    print("{:<10s}{:>30s}{:>20s}{:>20s}".format('Order', 'Amt', 'Price', 'Total'))
    print("{:-^80s}".format(''))


print("-----WELCOME TO ARNOLD'S AMAZING EATS-----")

# taken user and address details from user
userDetails = userDetails()

# taken order from user
dinnerItem1 = "Pizza"  # Dinner Items
dinnerItem2 = "Bargger"
costItem1 = 10              # Cost of Dinner Item
costItem2 = 8

while True:  # infinte while loop
    while True:

        # printing list of dinner items
        listItem(dinnerItem1,dinnerItem2,costItem1,costItem2)
        
        # take Sr. Number from user
        srNumber = srNumber()

        # checking Sr. No. is correct or not
        if srNumber == 1 or srNumber == 2:
            amount = int(input("Enter the amount of meals : "))
            break
        else:
            print("Please Enter correct serial no.")

    # priting order of user
    orderPrint(srNumber, dinnerItem1, dinnerItem2)

    # Confrimation from user about order
    confirm = input("Confrim your order Y/N ")
    if confirm.lower() == 'n':
        print("Go through order again")
        continue
    elif confirm.lower() == 'y':
        break


# Checking user is Student or Not
studentCheck = studentCheck()

# Calculation for placing order
itemPrice = itemPrice(costItem1, costItem2, amount)
discount = discount(studentCheck, itemPrice)
subTotal = subTotal(itemPrice, discount)
tax = tax(subTotal)
totalAmount = totalAmount(subTotal,tax)
# *********** printing recipts ***********

# printing user information
userInformation(userDetails)

# another method for writing recipts
# print("\n{0} {1}\nAddress: {2},{3},{4}\n{14:>9s}{5},{6},{7}\n{8:>40s}{9:>20s}\n{10:<10s}{11:>30s}{12:>20s}{13:>20s}\n{14:-<10s}{14:->30s}{14:->20s}{14:->20s}".format(firstName,lastName,streetNumber,streetName,unit,city,province,postalCode,'Item','Item','Order','Amt','Price','Total',''))


# printing dinner item that selected by user and also printing some details about prices
if srNumber == 1:
    print("{:<10s}{:>30d}{:>20s}{:>20s}\n".format(dinnerItem1, amount, '$' +
          str("{:.2f}".format(costItem1)), '$'+str("{:.2f}".format(itemPrice))))
else:
    print("{:<10s}{:>30d}{:>20s}{:>20s}\n".format(dinnerItem2, amount, '$' +
          str("{:.2f}".format(costItem2)), '$'+str("{:.2f}".format(itemPrice))))

# printing discount details if user is a student
if studentCheck.lower() == 'y':
    print("{:<60s}{:>20s}".format('10% student savings',
          '-$'+str("{:.2f}".format(discount))))
else:
    pass

# printing details about tax and total bill price
print("{:>60s}{:>20s}\n{:>60s}{:>20s}\n{:>80s}\n{:>60s}{:>20s}".format('Sub Total', '$'+str("{:.2f}".format(subTotal)),
      'Tax (13%)', '$'+str("{:.2f}".format(tax)), '-------', 'TOTAL', '$'+str("{:.2f}".format(totalAmount))))
