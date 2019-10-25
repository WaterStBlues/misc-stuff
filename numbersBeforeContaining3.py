# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:29:52 2019

The digit '3' appears in virtually all numbers (this is true of any arbitrary digit)
From 0-9, 10% of integers contain atleast one 3
from 0-99, it appears 19 times, or 19%
from 0-999, 271 times, or 27.1%
At which integer do 50% of the values contain at least one 3?
>> the number 333 counts as one, not 3
"""

masterList = [[0, False, 0]]
currentInt = 1 #we skippin 0
foundYet = False #this is lazy
def contains_three(num): #evaluate true or false whether number contains a 3
    
    listOfDigits = [int(digit) for digit in str(num)]
    # 133 becomes [1, 3, 3]
    
    for digit in listOfDigits:
        if digit == 3:
            return True
            break
    return False

def find_percentage_before(mList):
    numbersContainingThree = 0
    for i in range(0,len(mList)):
        if mList[i][1] == True:
            numbersContainingThree+=1
    return (numbersContainingThree/len(mList)) * 100


# main loop
while foundYet == False: #no bullying please
    #currentIntList will be set up as such:
    #[number, contains 3, % of numbers behind it containing 3]
    #e.g. [5, True, 20%]
    currentIntList = [currentInt, contains_three(currentInt), find_percentage_before(masterList)]
    print(currentIntList)
    if currentIntList[2] >= 50:
        print("50% of the numbers preceding " + str(currentIntList[0]) + " contain the digit '3'")
        foundYet = True #i'm genuinely sorry for this
        break
    else:
        masterList.append(currentIntList)
        currentInt+=1
    
