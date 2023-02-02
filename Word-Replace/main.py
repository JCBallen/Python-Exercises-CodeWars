# Para ver en funcionamiento el metodo de strings ".replace"
# .replace(palabra o letra del string a reemplazar, nuevo reemplazo, cantidad de reemplazos)

def replace_word():
    sentence = 'Hola mundo, soy Juan y gracias por leerme'
    print(sentence)
    word_to_replace = input('Enter the word to replace: ')
    word_replacement = input('Enter the word replacement: ')
    print(sentence.replace(word_to_replace,word_replacement))


replace_word()