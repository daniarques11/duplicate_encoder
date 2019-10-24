def duplicate_encoder(word):
    word = word.lower()
    palabra = ""
    for caracter in word:
        if word.count(caracter) > 1:
            palabra += ')'
        else:
            palabra += '('
    return palabra

print (duplicate_encoder('pasapalabra'))