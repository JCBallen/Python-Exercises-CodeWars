
import os

# Clearing the Screen
os.system('cls')


def reverseText(text):

    fText = []
    # nText = list(map(lambda n: n, text))       # separate the string in individual chars (not necesary)

    for index, letter in enumerate(text):        # enumerate saperates it
        # print(list(enumerate(text)))
        # print(index, letter)
        
        fText.insert(-len(fText), letter)        # el 1 va en -1, el 2 va en -2, 3 va en -3 y asi

    return "".join(fText)


text = input('Write something to check if its palindrome: ')
revTex = reverseText(text)
isPalindrome = True if revTex == text else False
print(revTex, isPalindrome)
