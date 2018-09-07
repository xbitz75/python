import util
import random

def tah_pocitace(pole):
    """
    vygeneruje tah pocitace a preda funckci tah
    """
    spravny_input = False
    while spravny_input == False:
        rng = random.randint(0, 19)
        if pole[rng] == "-":
            spravny_input = True
    pole = util.tah(pole, rng, "o")
    print(pole + "\n")
    return pole
