

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





if __name__ == __name__:
    with open("logs/output_11_29_14_11.txt") as logFile:
        logLines = logFile.readlines()
        findAllUniqueKeys(logLines)
        countUpKeys(logLines)