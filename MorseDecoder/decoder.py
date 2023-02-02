# from preloaded import MORSE_CODE

def decode_morse(morse_code):
    # Remember - you can use the preloaded MORSE_CODE dictionary:
    # For example: 
    # MORSE_CODE['.-'] = 'A'
    # MORSE_CODE['--...'] = '7'
    # MORSE_CODE['...-..-'] = '$'
    
    morse_code=morse_code.strip() # remove leading and trailing spaces
    morse_code=morse_code.split('   ') # split into words
    print(morse_code)
    morse_code=[word.split(' ') for word in morse_code] # for every "word" in morse_code 
                                                        # return the list that results when splitting that "word" (List Comprehensions)
    result = map(lambda word: ''.join(map(lambda letter: MORSE_CODE[letter], word)), morse_code)
    print(morse_code)
    
decode_morse('.... . -.--   .--- ..- -.. .')