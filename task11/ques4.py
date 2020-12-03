numbers= [3,4,1,25,89,6,34]
def filterOddNum(num):  
    if(num % 2) == 0:
        return False
    else:
        return True
oddfilter = filter(filterOddNum, numbers)
print("The odd numbers in the list are: ", list(oddfilter))
