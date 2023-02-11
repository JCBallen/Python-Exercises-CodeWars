# ROT13 ("rotate by 13 places", sometimes hyphenated ROT-13)
# is a simple letter substitution cipher that replaces a letter
# with the 13th letter after it in the alphabet.

import string


def rot13(message):
    result = ''
    alph_low = list(string.ascii_lowercase)
    alph_up = list(string.ascii_uppercase)
    for letter in message:
        if letter in alph_up:
            result += alph_up[alph_up.index(letter)-13]
        elif letter in alph_low:
            result += alph_low[alph_low.index(letter)-13]
        else:
            result += letter

    return result


print(rot13("EBG13 rknzcyr."))
