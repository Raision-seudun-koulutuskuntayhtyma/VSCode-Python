# Erittäin yksinkertainen luokka, jossa on vain oletusmuodostin

# Määritellään luokka henkilo, jossa on kaksi ominaisuutta (property)
class Henkilo:
    etunimi = 'Erkki'
    sukunimi = 'Esimerkki'

# Luodaan luokasta olio ja muutetaan sen sukunimi-ominaisuuden arvoa
henkilo1 = Henkilo()
henkilo1.sukunimi = 'Turtiainen'

print('Tämän henkilön etunimi on', henkilo1.etunimi, 'ja sukunimi on', henkilo1.sukunimi)

# Luokka, johon on rakennettu muodostin ja metodi

class Koodari:
    # Olionmuodostin, argumentteina etu- ja sukunimi, self viittaa luokasta luotavaan olioon
    def __init__(self, etunimi, sukunimi):
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    # Metodi joka tulostaa ruudulle viestin
    def oma_kehu(self):
        print('Mä oon', self.etunimi, 'ja oon kova Python-koodari')

# Luodaan koodari1-olio muodostimella
koodari1 = Koodari('Jonne', 'Janttari')

# Kutsutaan koodari1:n oma_kehu-metodia
koodari1.oma_kehu()

        