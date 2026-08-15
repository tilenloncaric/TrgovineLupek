import os               # delo s datotekami in mapami

def pot_do_mape():
    '''funkcija, ki vrne absolutno pot mape TrgovineLupek, pot v kateri se nahaja naša datoteka'''
    
    return os.path.dirname(os.path.abspath(__file__))
