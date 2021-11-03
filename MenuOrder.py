# Name: Assignment2.py
# Author: Mohit
# Date Created: October 31, 2021

# Description:
# This program take required input from user for Food delivery

# Function: check
# Description: will check user input is valid or not
# Parameters: 
#          none
# Return value:
#          userIn : input from user
def check():
    while True:
        userIn = input()
        if len(userIn) > 0:
            return userIn
        else:
            print("Sorry, Your Input is wrong.\nPlease Enter again ")

# Function: userDetailsFun
# Description: will take inputs from user 
# Parameters: 
#          none
# Return value:
#          userDetails: details of user
def userDetailsFun():
    userDetails = []  # list for adding details of user
    print("Enter your First Name : ",end="")
    userDetails.append(check())
    print("Enter your Last Name : ",end="")
    userDetails.append(check())
    print("Enter your Street Number : ",end="")
    userDetails.append(check())
    print("Enter your Street Name : ",end="")
    userDetails.append(check())
    print("Enter your Unit : ",end="")
    userDetails.append(check())
    print("Enter your City : ",end="")
    userDetails.append(check())
    print("Enter your Province : ",end="")
    userDetails.append(check())
    print("Enter your Postal Code : ",end="")
    userDetails.append(check())
    print("Enter your Phone Number : ",end="")
    userDetails.append(check())
    return userDetails

# Function: deliveryFun
# Description: will take input for delivery
# Parameters: 
#          none
# Return value:
#          delivery: delivery
def deliveryFun():
    delivery = input("Do you want Delivery Dinner at Your Address(y/n) : ")
    if delivery.lower() == 'y' or delivery.lower() == 'n':
        return delivery
    else:
        print("Please Enter correct detials")
        deliveryFun()
    
# Function: itemListFun
# Description: will create list for dinner item
# Parameters: 
#          none
# Return value:
#          itemList: list of dinner item
def itemListFun():
    itemList = {
        "1":"Chicken",
        "2":"Salmon",
        "3":"Zucchini",
        "4":"Pasta",
        "5":"Cauliflower",
        "6":"Pizza"
    }
    return itemList

# Function: costListFun
# Description: will create list for cost of dinner item
# Parameters: 
#          none
# Return value:
#          costList: list of cost 
def costListFun():
    costList = [15,20,18,10,13,15]
    return costList

# Function: listItem
# Description: will print list of dinner item
# Parameters: 
#          itemList : list of dinner item
#          costList : list of dinner item's cost
# Return value:
#           none

def listItem(itemList,costList):
    print("{0:<25s}{1:<25s}{2:25s}".format('Sr. No.', 'Meals','Cost'))
    index = 0 # for printig price list
    for key in itemList:
        print("{:<25s}{:<25s}${:<25d}".format(key,itemList[key],costList[index]))
        index = index + 1
# Function: srNumberFun
# Description: will take the input of Sr. Number for dinner item
# Parameters: 
#          none 
# Return value:
#           Sr. number 
def srNumberFun():
    return int(input("which serial number meals you want ? "))

# Function: orderPrintFun
# Description: will print order details
# Parameters: 
#          srNumber : Sr. number chosed by user
#          itemList: list of dinner item
# Return value:
#           none
def orderPrintFun(srNumber,itemList):
    print("Your orders is : ", itemList[str(srNumber)])
    

# Function: studentCheckFun
# Description: will check user is student or not
# Parameters: 
#          None
# Return value:
#          studentCheck : user is student or not
def studentCheckFun():
    studentCheck = input("you get 10% discount if you are a student. You are a student Y/N ")
    if studentCheck.lower() == 'y' or studentCheck.lower() == 'n':
        return studentCheck
    else:
        print("select the correct option")
        studentCheckFun()

# Function: tipFun
# Description: will take tip amount from user
# Parameters: 
#          None
# Return value:
#          tip : tip 
def tipFun():
    while True:
        tip = int(input("Enter amount of Tip from 10, 15 or 20% "))
        if tip in [10,15,20]:
            return tip
        else:
            print("Enter correct Input")
            tipFun()
# Function: calculationFun
# Description: will calculate total amount
# Parameters: 
#          costList: list of dinner item's cost
#           amount: amount of dinner
# Return value:
#          calculation: list of all calculation steps


def calculationFun(costList, amount, tip, delivery):
    calculation = []
    calculation.append(costList[srNumber-1]*amount) #itemPrice
    if studentCheck.lower() == 'y':
        calculation.append(calculation[0]*0.1)  #discount
    else:
        calculation.append(0)
    calculation.append(calculation[0] - calculation[1])  #subTotal
    calculation.append(calculation[2]*0.13)  #tax  [3]
    calculation.append(calculation[2]*tip*0.01) #tip [4]
    if delivery.lower() == 'y' and calculation[2] >= 30: 
        calculation.append(5)      #[5]
    else:
        calculation.append(0)
    calculation.append(calculation[2] + calculation[3] + calculation[4] + calculation[5])  # totalAmount   [6]
    return calculation

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
def userInformationFun(userDetails):
    print("{} {}".format(userDetails[0], userDetails[1]))
    print("Address: {},{},{}".format(userDetails[2], userDetails[3], userDetails[4]))
    print("{:>9s}{},{},{}".format('', userDetails[6], userDetails[7], userDetails[8]))
    print("{:>40s}{:>20s}".format('Item', 'Item'))
    print("{:<10s}{:>30s}{:>20s}{:>20s}".format('Order', 'Amt', 'Price', 'Total'))
    print("{:-^80s}".format(''))


print("-----WELCOME TO ARNOLD'S AMAZING EATS-----")

# taken user and address details from user
userDetails = userDetailsFun()

# taken from user for delivery
delivery = deliveryFun()

# taken order from user
itemList = itemListFun() # list of dinner item
costList = costListFun() # list of dinner's cost

while True:  # infinte while loop
    while True:

        # printing list of dinner items
        listItem(itemList,costList)
        
        # take Sr. Number from user
        srNumber = srNumberFun()

        # checking Sr. No. is correct or not
        if srNumber in [1,2,3,4,5,6]:
            amount = int(input("Enter the amount of meals : "))
            break
        else:
            print("Please Enter correct serial no.")

    # priting order of user
    orderPrintFun(srNumber, itemList)

    # Confrimation from user about order
    confirm = input("Confrim your order Y/N ")
    if confirm.lower() == 'n':
        print("Go through order again")
        continue
    elif confirm.lower() == 'y':
        break


# Checking user is Student or Not
studentCheck = studentCheckFun()

#taken input from user for tip
if delivery.lower() == 'y':
    tip = tipFun()
else:
    tip = 0

# Calculation for placing order
calculation = calculationFun(costList,amount,tip,delivery)

# *********** printing recipts ***********

# printing user information
userInformationFun(userDetails)

# printing dinner item that selected by user and also printing some details about prices
print("{:<10s}{:>30d}{:>20s}{:>20s}\n".format(itemList[str(srNumber)], amount, '$' + str("{:.2f}".format(costList[srNumber-1])), '$'+str("{:.2f}".format(calculation[0]))))


# printing discount details if user is a student
if studentCheck.lower() == 'y':
    print("{:<60s}{:>20s}".format('10% student savings',
          '-$'+str("{:.2f}".format(calculation[1]))))
else:
    pass


# printing details about tax and total bill price
print("{:>60s}{:>20s}".format('Sub Total', '$'+str("{:.2f}".format(calculation[2]))))
if delivery.lower() == 'y':
    print("{:<60s}{:>20s}".format('Delivery Charges are','$'+str("{:.2f}".format(calculation[5]))))
    print("{:<60s}{:>20s}".format('Tip for Delivery Boy '+str(tip)+'% of Sub Total','$'+str("{:.2f}".format(calculation[4]))))
print("{:>60s}{:>20s}\n{:>80s}\n{:>60s}{:>20s}".format('Tax (13%)', '$' +
      str("{:.2f}".format(calculation[3])), '-------', 'TOTAL', '$'+str("{:.2f}".format(calculation[6]))))
