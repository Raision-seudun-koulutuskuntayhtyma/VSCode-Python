# Määritellään luokka
class Muistutus:
    def __init__(self, numero, viesti):
        self.numero = numero
        self.viesti = viesti
    
    # Oliometodi: käytettävissä vain luokasta johdetusta oliosta käsin, voit muuttaa olion ominaisuuksia
    def kauppalappu(self, kauppa, ostoslista):
        self.kauppa = kauppa
        self.ostoslista = ostoslista
        print('Käy kaupassa', self.kauppa, 'ja osta', self.ostoslista)

    # Staattinen metodi, jolla ei voi muuttaa luokan tai olion ominaisuuksia, huomaa dekoraattori @staticmethod
    @staticmethod
    def vakiomuistutus():
        print('Muista Ulkoilla')

    # Luokkametodi, huomaa dekoraattori @classmethod ja argumentti cls, joka viittaa luokkaan.
    # Voit muuttaa luokan ominaisuuksia, jotka ovat oletusarvoja uuden olion ominaisuuksille.
    @classmethod
    def oletusmuistutus(cls,motto):
        cls.motto = motto
        
# Luodaan olio muistutus1 ja näytetään motto
muistutus1 = Muistutus(1, 'Päivän tärkeät asiat')

# Kutsutaan muistutus1:n kauppalappu()-metodia
muistutus1.kauppalappu('X Marketti', ['Maitoa', 'Leipää', 'Juustoa'])

# Kutustaan staattista metodia vakiomuistutus()
Muistutus.vakiomuistutus()

# Kutsutaan luokkametodia oletusmuistutus() päivittämään luokan motto-ominaisuutta
Muistutus.oletusmuistutus('Älä osta mitään -päivä on joka päivä')

# Katsotaan luokan motto-ominaisuuden arvo
print('Luokan motto-ominaisuutta on muutettu luokkametodilla ja arvo on:', Muistutus.motto,'Se on oletus uusille olioille')

# Luodaan uusi olio ja näytetään luokkametodilla muutettu motto olion ominaisuuksista
muistutus2 = Muistutus(2, 'Käy katosmassa uutta autoa')
print('Luokan ominaisuus motto löytyy myös siitä johdetusta oliosta:',muistutus2.motto)

muistutus2.vakiomuistutus()
muistutus2.oletusmuistutus('Ei haatana')
muistutus2.motto