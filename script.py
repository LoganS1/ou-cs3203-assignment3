#Sums every element in a list
def getSumOfList(list):
    sum = 0
    for item in list:
        sum += item
    return sum

#Multiplies every element in a list
def getProductOfList(list):
    #Returns 0 if list is empty
    product = 0
    for item in list:
        if list.index(item) == 0:
            product = item
        else:
            product *= item
    return product

#Gets a list of numbers from the user through command line
def getListFromUser():
    userList = []
    print("Please supply a list of integers. Type 'stop' to stop:\n")
    userInput = input("Next integer ('stop' to stop): ")
    while(userInput != "stop"):
        userList.append(int(userInput))
        userInput = input("Next integer: ")
    return userList

def reverseList(list):
    reversedList = list
    reversedList.reverse()
    return reversedList

#Main - Start Here
def main():
    #Get needed information
    userList = getListFromUser()
    userListSum = getSumOfList(userList)
    userListProduct = getProductOfList(userList)
    reversedUserList = reverseList(userList)
    #Print out information to user
    print("--------")
    print("List Sum: ", userListSum)
    print("List Product: ", userListProduct)
    print("Reversed List: ", reversedUserList)
    print("--------")

if __name__ == "__main__":
    main()
