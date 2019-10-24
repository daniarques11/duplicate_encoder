from duplicate_encoder_count import duplicate_encoder

def duplicate_encoder_differents():
    assert duplicate_encoder('din') == '((('

def duplicate_encoder_alternate():
    assert duplicate_encoder('recede') == '()()()'

def duplicate_encoder_mayus_check():
    assert duplicate_encoder('Success') == ')())())'
def duplicate_encoder():
    assert duplicate_encoder('(( @') == '))(('