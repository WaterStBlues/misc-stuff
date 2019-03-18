#robustandrun/waterstblues' genetics solver, version 1
#reeeeeeeeeeeeeeeeeeee

#step 1: clear ss13 logs, then run around scanning nerds with your handy dandy genetics sequence scanner
#step 2: when you're done, copy and paste all of the logs you've amassed into a .txt file. save it.
#step 3: put the path to your file in the path var below. Paste the location in between the quotation marks below. Don't fuck it up.
#step 4: run it and take most of the guesswork out of genetics


path = r"C:\Users\You\Desktop\EXAMPLE.txt"
f_handler = open(path)

def getBottomTop(codeList):
    topList = []
    bottomList = []
    for i in range(0,4):
        currentList = list(codeList[i])
        for j in range(0,8):
            if j == 0 or j%2 == 0:
                topList.append(currentList[j])
            else:
                bottomList.append(currentList[j])
        bottomList.append("  ")
        topList.append("  ")
        
    #print(topList)
    #print(bottomList)

    for i in range(len(topList)):
        if topList[i] == 'X':
            if bottomList[i] == 'A':
                topList[i] = 'T'
            if bottomList[i] == 'T':
                topList[i] = 'A'
            if bottomList[i] == 'C':
                topList[i] = 'G'
            if bottomList[i] == 'G':
                topList[i] = 'C'
        
    for i in range(len(bottomList)):
        if bottomList[i] == 'X':
            if topList[i] == 'A':
                bottomList[i] = 'T'
            if topList[i] == 'T':
                bottomList[i] = 'A'
            if topList[i] == 'C':
                bottomList[i] = 'G'
            if topList[i] == 'G':
                bottomList[i] = 'C'

    return [topList, bottomList]

def printGeneticCode(mutation_id, top_list, bottom_list):
    line1 = ""
    line2 = ""
    line3 = ""
    for i in range(len(top_list)):
        line1 += top_list[i] + "  "
        if top_list[i] != "  " and bottom_list[i] != "  ":
            line2 +=  "|  "
        else:
            line2 += "--  "
        line3 += bottom_list[i] + "  "
    return "Mutation " + mutation_id + "\n" + line1 + "\n" + line2 + "\n" + line3 + "\n"



mutationStrList = []
parsedStrList = []
codeblockList = []
for line in f_handler:
    if line.startswith("- Mutation"):
        mutationStrList.append(line)

for i in mutationStrList:
    nr = i.rsplit("- Mutation ")
    nv = nr[1].rsplit(" > ") # elem 0 = just number
    splitAtLineBreak = nv[1].rsplit(" \n") #elem 0 = just genetic code
    NewTuple = (nv[0], splitAtLineBreak[0])
    parsedStrList.append(NewTuple)

for i in parsedStrList:
    mutationNumber = int(i[0])
    codeblock = i[1].split("-")
    mutation = [str(mutationNumber), codeblock]
    codeblockList.append(mutation)

    
for i in range(len(codeblockList)):
    lists_list = getBottomTop(codeblockList[i][1])
    print(printGeneticCode(codeblockList[i][0], lists_list[0], lists_list[1]))