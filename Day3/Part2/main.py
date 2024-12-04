import itertools
import re


def readFile():
    file_path = 'Day3/info.txt'
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."


def findAllMulAndDo(content):
    pattern = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
    matches = re.findall(pattern, content)
    return matches


def calculateMul(matches):
    result = 0
    isActive = True
    for match in matches:
        if match[2] == "do()":
            isActive = True
        elif match[3] == "don't()":
            isActive = False

        elif isActive:
            result += int(match[0]) * int(match[1])
    return result 


if __name__ == "__main__":
    content = readFile()
    matches = findAllMulAndDo(content)
    result = calculateMul(matches)
    print(result)
