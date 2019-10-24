from duplicate_encoder_dictionary import duplicate_encoder

def test_differents():
    assert duplicate_encoder('din') == '((('

def test_alternate():
    assert duplicate_encoder('recede') == '()()()'

def test_mayus_check():
    assert duplicate_encoder('Success') == ')())())'

def test_strange_characters():
    assert duplicate_encoder('(( @') == '))(('