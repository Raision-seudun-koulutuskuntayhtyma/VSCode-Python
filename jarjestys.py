# taso-muuttuja, joka ei ole minkään funktion sisällä
taso = 'Global: Muuttujan arvoa ei löydy kummastakaan funktiosta'

# taso-muuttuja on sijoitettu funktion sisälle
def ulompifunktio():
    taso="Enclosed: muuttujan arvo löytyy ulommasta funktiosta"

    # taso-muuttuja sijoitettu funktion sisällä olevaan toiseen funktioon
    def sisempifunktio():
        taso="Local: muuttujan arvo löytyy sisemmästä funktiosta"
        return taso
        
    return sisempifunktio()

# Tulostetaan, tieto siitä, miltä tasolta muuttujan arvo löytyi    
print('Sisemmän funktion näkökulmasta taso-muuttuja on', ulompifunktio())

        