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