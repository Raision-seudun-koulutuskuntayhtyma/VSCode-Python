# Funktio, jolla on sisäinen (local) muuttuja ympyrän säteen laskemiseksi

def ympyran_pinta_ala(halkaisija):
    sade = halkaisija / 2
    return sade ** 2 * 3.1415

# Palautetaan halkaisijaltaan metrin ympyrän pinta-ala ja säde
print(ympyran_pinta_ala(1)) # Toimii
print(sade) # Ei toimi koska muuttuja käytettävissä vain funktion sisällä