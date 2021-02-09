# 10-järestelmän luvut eli desimaaliluvut 8 bittiä on tavu
tavu = 255

# Tulostetaan tavu binäärimuodossa (0b11111111)
print(bin(tavu))

#Tulostetaan tavu heksadesimaalimuodossa (0xff)
print(hex(tavu))

toinen_tavu = 0b0010

# Tulostettaessa binääriluvut muutetaan automaattisesti 10-järjestelmään, int()-funktiota ei tarvita
print(toinen_tavu)