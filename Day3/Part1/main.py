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


def findAllMul(content):
    pattern = r'mul\((\d+)\,(\d+)\)'
    matches = re.findall(pattern, content)
    return matches


def calculateMul(matches):
    result = 0
    for match in matches:
        result += int(match[0]) * int(match[1])
    return result 


if __name__ == "__main__":
    content = readFile()
    matches = findAllMul(content)
    result = calculateMul(matches)
    print(result)
