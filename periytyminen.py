# Henkilö-luokka, jossa yleiset ihmiseen liittyvät perusominaisuudet -yliluokka
class Henkilo:
    def __init__(self, etunimi, sukunimi):
        self.etunimi = etunimi
        self.sukunimi = sukunimi

# Asiakas-luokka, joka perii Henkilö-luokan ominaisuudet ja jolla on erillinen asiakasnumero-ominaisuus -aliluokka
class Asiakas(Henkilo):
    def __init__(self, etunimi, sukunimi, asiakasnumero):
        super().__init__(etunimi, sukunimi)
        self.asiakasnumero = asiakasnumero
        
# Myyjä-luokka, perii Henkilöluokan ominaisuudet, erityispiirteenä autoetu -aliluokka
class Myyja(Henkilo):
    def __init__(self, etunimi, sukunimi, autoetu):
        super().__init__(etunimi, sukunimi)
        self.autoetu = autoetu
       
# Luodaan uusi asiakas
asiakas = Asiakas('Herkko', 'Hyväusko', 313)

# Luodaan myyjä
myyja = Myyja('Kalle', 'Keckelberg', True)

# Tulostetaan kaupan tietoja
print(myyja.sukunimi, 'myi käytetyn Bemarin asiakkaalle, jonka asiakasnumero oli', asiakas.asiakasnumero)

