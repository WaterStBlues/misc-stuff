#robustandrun/waterstblues' SS13 genetics solver, version 1

#step 1: clear ss13 logs, then run around scanning nerds with your handy dandy genetics sequence scanner
#step 2: when you're done, copy and paste all of the logs you've amassed into a .txt file
#step 3: put the path to your file in the path var below. Paste the location in between the quotation marks below. Don't mess it up.
#step 4: run it and take most of the guesswork out of genetics


path = r"C:\Foldername\File.txt"
f_handler = open(path)

def comparePair(original, compare): #pass in / return string
    if original == 'X':
        if compare == 'A':
            result = 'T'
        if compare == 'T':
            result = 'A'
        if compare == 'C':
            result = 'G'
        if compare == 'G':
            result = 'C'
    return result


def eval_bottom_top(codeList):
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

    for i in range(len(topList)):
        if topList[i] == 'X':
            if bottomList[i] != 'X':
                topList[i] = comparePair(topList[i], bottomList[i])
        if bottomList[i] == 'X':
            if topList[i] != 'X':
                bottomList[i] = comparePair(bottomList[i],topList[i])

    return [topList, bottomList]

    
        
    #print(topList)
    #print(bottomList)

def compExistingCodes(dictEntry, newEntry): #if it's a dictionary pass in dict[key], should be a list of 2 lists!!!
    top_1 = dictEntry[0]
    bottom_1 = dictEntry[1]
    top_2 = newEntry[0]
    bottom_2 = newEntry[1]

    for i in range(len(top_1)): #compare the top rows and bottom rows
        if top_1[i] == 'X':
            if top_2[i] != 'X':
                top_1[i] = top_2[i]
        if bottom_1[i] == 'X':
            if bottom_2[i] != 'X':
                bottom_1[i] = bottom_2[i]

    #now compare top1 to bottom2 and bottom1 to top2 and make comparisions
    for i in range(len(top_1)):
        if top_1[i] == 'X':
            if bottom_2[i] != 'X':
                top_1[i] = comparePair(top_1[i], bottom_2[i])
        if bottom_1[i] == 'X':
            if top_2[i] != 'X':
                bottom_1[i] = comparePair(bottom_1[i],top_2[i])

    x = [top_1, bottom_1]
    return x

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
    return "Mutation " + str(mutation_id) + "\n" + line1 + "\n" + line2 + "\n" + line3 + "\n"

mutationStrList = []
for line in f_handler:
    if line.startswith("- Mutation"):
        mutationStrList.append(line)

parsedStrList = []
for i in mutationStrList:
    nr = i.rsplit("- Mutation ")
    nv = nr[1].rsplit(" > ") # elem 0 = just number
    splitAtLineBreak = nv[1].rsplit(" \n") #elem 0 = just genetic code
    NewTuple = (nv[0], splitAtLineBreak[0])
    parsedStrList.append(NewTuple)


codeblockList = []
for i in parsedStrList:
    mutationNumber = int(i[0])
    codeblock = i[1].split("-")
    mutation = [mutationNumber, codeblock]
    codeblockList.append(mutation)


mutationDict = {}
for i in range(len(codeblockList)):
    lists_list = eval_bottom_top(codeblockList[i][1])
    #codeblockList.append(codeblockList[i][0], lists_list[0], lists_list[1]) #mutationid, top, bottom
    if codeblockList[i][0] in mutationDict:
        mutationDict[codeblockList[i][0]] = compExistingCodes(mutationDict[codeblockList[i][0]], [lists_list[0],lists_list[1]])
    else:
        mutationDict[codeblockList[i][0]] = [lists_list[0], lists_list[1]]

#print(mutationDict)
sorted_mutationDict = dict(sorted(mutationDict.items()))
#for i in sorted_mutationDict:
#    print(i, sorted_mutationDict[i])
for i in sorted_mutationDict:
    print(printGeneticCode(i, sorted_mutationDict[i][0], sorted_mutationDict[i][1]))
