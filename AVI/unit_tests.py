from functies import *

# test 1: getNumberOfCharacters
if getNumberOfCharacters('aap') == 3:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")

# schrijf zelf nog wat extra testen voor getNumberOfCharacters

if getNumberOfCharacters('ik ben nawfal') == 11:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")

# test 2: getNumberOfSentences
if getNumberOfSentences(getText('easy')) == 14:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")

# # schrijf zelf nog een extra testen voor getNumberOfSentences (gebruik test.txt).

if getNumberOfSentences(getText('data\hallo.txt')) == 6:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")

# test 3: getNumberOfWords

print(getNumberOfWords(getText('data\difficult1.txt')))
if getNumberOfWords(getText('data\difficult1.txt')) == 82:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")

if getNumberOfWords(getText('data\easy1.txt')) == 11:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")

# schrijf zelf nog een extra testen voor getNumberOfWords (gebruik test.txt).

print(getNumberOfWords(getText('data\hallo.txt')))
if getNumberOfWords(getText('data\hallo.txt')) == 32:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")