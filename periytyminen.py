# Henkilö-luokka, jossa yleiset ihmiseen liittyvät perusominaisuudet (yliluokka, parent, super class)
class Henkilo:
    def __init__(self, etunimi, sukunimi):
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def nauru(self):
        print('Minkä tahansa henkilön nauru kuulostaa tältä: hah, hah, haa')


# Asiakas-luokka, joka perii Henkilö-luokan ominaisuudet ja jolla on erillinen asiakasnumero-ominaisuus (aliluokka, child sub class)
class Asiakas(Henkilo):
    def __init__(self, etunimi, sukunimi, asiakasnumero):
        super().__init__(etunimi, sukunimi)
        self.asiakasnumero = asiakasnumero

# Myyjä-luokka, perii Henkilöluokan ominaisuudet, erityispiirteenä autoetu (aliluokka, child, sub class)


class Myyja(Henkilo):
    def __init__(self, etunimi, sukunimi, autoetu):
        super().__init__(etunimi, sukunimi)
        self.autoetu = autoetu

    def nauru(self):
        print('Automyyjän nauru kuulostaa ilkeältä: aha, aha, aha')


# Luodaan uusi asiakas
asiakas = Asiakas('Herkko', 'Hyväusko', 313)

# Luodaan myyjä
myyja = Myyja('Kalle', 'Keckelberg', True)

# Tulostetaan kaupan tietoja
print(myyja.sukunimi, 'myi käytetyn Bemarin asiakkaalle, jonka asiakasnumero oli',
      asiakas.asiakasnumero)

# Nauratetaan asiakasta, joka perii nauru()-metodin Henkilöluokalta
asiakas.nauru()

# Nauratetaan myyjää, Myyjä-luokassa nauru()-metodi on kirjoitettu uudelleen (ylikirjoitettu)
myyja.nauru()

