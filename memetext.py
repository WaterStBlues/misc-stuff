# a e s t h e t i c
def aesth(userInput):
    return ' '.join(userInput)


#"hey you guys have fun, i'm not drinking tonight" "iM nOt DrInKiNg ToNiGhT"
def mock(userInput):
    rawList = list(userInput)
    mockList = []
    count = 1
    for item in rawList:
        if count % 2 == 0:
            item = (str(item)).upper()
            mockList.append(item)
            count+=1
        elif count % 2 != 0:
            item = (str(item)).lower()
            mockList.append(item)
            count+=1
    return ''.join(mockList)
