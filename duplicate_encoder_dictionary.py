def duplicate_encoder(string):
    dictionary = {}
    string = string.lower()
    for character in string:
        if character in dictionary:
            dictionary[character] = ')'
        else:
            dictionary[character] = '('
    assert dictionary != {}
    stringEncoded = ''
    for character in string:
        stringEncoded = stringEncoded + dictionary[character]
    return stringEncoded 