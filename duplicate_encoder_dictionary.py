def duplicate_encoder(string):
    dictionary = {}
    for character in string:
        character = character.lower()
        if character in dictionary:
            dictionary[character] = ')'
        else:
            dictionary[character] = '('
    assert dictionary != {}
    stringEncoded = ''
    for character in string:
        character = character.lower()
        stringEncoded = stringEncoded + dictionary[character]
    return stringEncoded 
