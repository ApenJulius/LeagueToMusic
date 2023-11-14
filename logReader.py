from pprint import pprint

def findAllUniqueKeys(fileLines):
    uniqueKeys = []
    for line in fileLines:
        key = line.split(" ")[1].replace("'", '')
        if key not in uniqueKeys:
            uniqueKeys.append(key)
    print(uniqueKeys)
    return uniqueKeys



def findUpKey(fileLines):
    if fileLines[0].split(" ")[0] != "Down":
        return
    downKey = fileLines[0].split(" ")[1].replace("'", '')
    print(downKey)
    for key in fileLines:
        if key == downKey:
            print(key, " match")

def countUpKeys(fileLines):
    count = 0
    for line in fileLines:
        if line.split(" ")[0] == "Up":
            count += 1
    
    print(count, " up keys counted")
    return count

def pairDownUpKeys(fileLines):
    pairedKeys = []
    for downLine in fileLines:
        downLineArray = downLine.split(" ")
        if downLineArray[0] != "Down":
            continue
        for upLine in fileLines:
            upLineArray = upLine.split(" ")
            if upLineArray[0] == "Up" and upLineArray[1] == downLineArray[1]:
                pairedKeys.append((downLine, upLine))
                break
    pprint(pairedKeys)
    return pairedKeys




if __name__ == __name__:
    with open("logs/output_16_45_14_11.txt") as logFile:
        logLines = logFile.readlines()
        findAllUniqueKeys(logLines)
        pairDownUpKeys(logLines)
