import re
import os
os.system('cls')

# You need to write regex that will validate a password to make sure it meets the following criteria:

# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a digit
# only contains alphanumeric characters (note that '_' is not alphanumeric)


myAttempt = r'[[a-z]+[A-Z]+\d+]{6,}'

# ! You need to use lookaheads:
# ? Explanation:

# ^               # start of input 
# (?=.*?[A-Z])    # Lookahead to make sure there is at least one upper case letter
# (?=.*?[a-z])    # Lookahead to make sure there is at least one lower case letter
# (?=.*?[0-9])    # Lookahead to make sure there is at least one number
# [A-Za-z0-9]{6,} # Make sure there are at least 6 characters of [A-Za-z0-9]
# $               # end of input

internet_Search='^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])[A-Za-z0-9]{6,}$'


# regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


text = 'fjd3IR9'


print(re.findall(internet_Search, text))
