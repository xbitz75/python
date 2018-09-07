def tah(pole, cislo_pole, zadany_symbol):
    """
    prijme parametry a vykona tah
    """
    return pole[:cislo_pole] + zadany_symbol + pole[cislo_pole + 1:] 
