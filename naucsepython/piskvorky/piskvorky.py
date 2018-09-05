import random

def vyhodnot(pole):
    """
    vyhodnoti pole a vypise vysledek
    """
    if "xxx" in pole:
        vysledek = "x"
    elif "ooo" in pole:
        vysledek = "o"
    elif "-" not in pole:
        vysledek = "!"
    else:
        vysledek = "-"
    return vysledek

def tah(pole, cislo_pole, zadany_symbol):
    """
    prijme parametry a vykona tah
    """
    return pole[:cislo_pole] + zadany_symbol + pole[cislo_pole + 1:] 

def tah_hrace(pole):
    """
    prijme input a preda ho funkci tah
    """
    spravny_input = False
    while spravny_input == False:
        pozice = input("Na jakou pozici chcete hrat?: ")
        try:
            pozice = int(pozice)
            if pozice >= 0 and pozice <= 19 and pole[pozice] != "x" and pole[pozice] != "o":
                spravny_input = True
            else:
                print("\n Spatna pozice, zkus to znovu \n")
        except ValueError:
            print("Nebylo mozne vytvorit integer")
    pole = tah(pole, pozice, "x")
    print(pole + "\n")
    return pole
    
def tah_pocitace(pole):
    """
    vygeneruje tah pocitace a preda funckci tah
    """
    spravny_input = False
    while spravny_input == False:
        rng = random.randint(0, 19)
        if pole[rng] == "-":
            spravny_input = True
    pole = tah(pole, rng, "o")
    print(pole + "\n")
    return pole

def piskvorky1d():
    pole = "--------------------"
    vyhodnot(pole)
    while vyhodnot(pole) == "-":
        pole = tah_pocitace(pole)
        if vyhodnot(pole) == "o":
            print("pc vyhral")
            break
        if vyhodnot(pole) == "!":
            print("remiza")
            break
        pole = tah_hrace(pole)
        if vyhodnot(pole) == "x":
            print("vyhrals")
            break
        if vyhodnot(pole) == "!":
            print("remiza")
            break

piskvorky1d()