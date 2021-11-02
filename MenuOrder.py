# Name: Assignment2.py
# Author: Mohit
# Date Created: October 31, 2021

# Description:
# This program take required input from user for Food delivery

# Function: userDetailsFun
# Description: will take inputs from user 
# Parameters: 
#          none
# Return value:
#          userDetails: details of user
def userDetailsFun():
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

# Function: calculationFun
# Description: will calculate total amount
# Parameters: 
#          costList: list of dinner item's cost
#           amount: amount of dinner
# Return value:
#          calculation: list of all calculation steps
def calculationFun(costList,amount):
    calculation = []
    calculation.append(costList[srNumber-1]*amount) #itemPrice
    if studentCheck.lower() == 'y':
        calculation.append(calculation[0]*0.1)  #discount
    else:
        calculation.append(0)
    calculation.append(calculation[0] - calculation[1])  #subTotal
    calculation.append(calculation[2]*0.13)  #tax
    calculation.append(calculation[2] + calculation[3]) #totalAmount
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

# Calculation for placing order
calculation = calculationFun(costList,amount)

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
print("{:>60s}{:>20s}\n{:>60s}{:>20s}\n{:>80s}\n{:>60s}{:>20s}".format('Sub Total', '$'+str("{:.2f}".format(calculation[2])),
      'Tax (13%)', '$'+str("{:.2f}".format(calculation[3])), '-------', 'TOTAL', '$'+str("{:.2f}".format(calculation[4]))))
