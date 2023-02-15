def getSumOfList(list):
    sum = 0
    for item in list:
        sum += item
    return sum

def getProductOfList(list):
    product = 0
    for item in list:
        if list.index(item) == 0:
            product = item
        else:
            product *= item
    return product

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

def main():
    userList = getListFromUser()
    userListSum = getSumOfList(userList)
    userListProduct = getProductOfList(userList)
    print("--------")
    print("List Sum: ", userListSum)
    print("List Product: ", userListProduct)
    print("--------")

if __name__ == "__main__":
    main()