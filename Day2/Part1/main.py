def readFile():
    file_path = 'Day2/info.txt'
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."

def splitInListsOfReports(content):
    content = content.split("\n")
    listOfReports = []
    for line in content:
        listOfLevels = []
        listOfLevels = line.split()
        listOfLevels = [int(level) for level in listOfLevels]
        listOfReports.append(listOfLevels)
    return listOfReports


def checkValidReports(listOfReports):
    count = 0
    for i in range(len(listOfReports)):
        if listOfReports[i] == sorted(listOfReports[i]) or listOfReports[i] == sorted(listOfReports[i], reverse=True):
            
            isValid = True
            for j in range(len(listOfReports[i]) - 1):
                if abs(listOfReports[i][j] - listOfReports[i][j+1]) < 1 or abs(listOfReports[i][j] - listOfReports[i][j+1]) > 3:
                    isValid = False
                    break
            if isValid:
                count += 1
    return count


if __name__ == "__main__":
    content = readFile()
    listOfReports = splitInListsOfReports(content)
    validReports = checkValidReports(listOfReports)
    print(validReports)
