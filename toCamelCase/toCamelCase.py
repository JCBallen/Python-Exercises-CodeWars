# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case).

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

import re

def to_camel_case(text):
    texts = re.split('-|_|\*',text) # Splitting a String with multiple delimiters: re.split( ' del1 | del2 | del3 | del4 | ' , string )
    mapped=list(map(lambda a : a.capitalize(),texts[1:len(texts)]))
    x="".join(mapped)
    x=texts[0]+x
    return x

print(to_camel_case("A-cat_was-kaw*aii"))
print(to_camel_case("The_stealth_warrior"))


# Other Option variation , without the import
def to_camel_case2(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])
