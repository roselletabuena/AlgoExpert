# O(n) time | O(n) space - where n is the length of the input string
def runLineEncoding(string):
    encodedStringCharacters = []
    currentRunLength = 1

    for i in range(1, len(string)):
        currentRunLength = string[i]
        previousCharactor = string[i - 1]

        if currentRunLength != previousCharactor or currentRunLength == 9:
            encodedStringCharacters.append(str(currentRunLength))
            encodedStringCharacters.append(previousCharactor)
            currentRunLength = 0

        currentRunLength += 1

    encodedStringCharacters.append(str(currentRunLength))
    encodedStringCharacters.append(string[len(string) - 1])

    return "".join(encodedStringCharacters)