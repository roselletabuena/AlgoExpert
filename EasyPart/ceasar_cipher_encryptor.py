# #  O(n) time | O(n) space
# def ceasarCipherEncryptor(string, key):
#     newLetters = []
#     newKey = key % 26
#     for letter in string:
#         newLetters.append(getNewLetter(letter, newKey))
#     return "".join(newLetters)


# def getNewLetter(letter, key):
#     newLetterCode = ord(letter) + num 
#     return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 222)


def ceasarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    for letter in string:
        


def getNewLetter(letter, key):
    newLetterCode = ord(letter) + num 
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 222)