def readFile():
    file_path = 'Day1/info.txt'
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."

def splitIn2Lists(content):
    content = content.split("\n")
    list1 = []
    list2 = []
    for line in content:
        parts = line.split()
        if len(parts) == 2:
            list1.append(int(parts[0]))
            list2.append(int(parts[1]))

    return list1, list2


def calculateSimilarity(list1, list2):
    absoluteCount = 0
    for i in range(len(list1)):
        count = 0
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                count += 1

        absoluteCount += count * list1[i]
    return absoluteCount


if __name__ == "__main__":
    content = readFile()
    list1, list2 = splitIn2Lists(content)
    similarity = calculateSimilarity(list1, list2)
    print(similarity)
