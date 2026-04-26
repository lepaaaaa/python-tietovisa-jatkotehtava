# Turvalliset valinnat verkossa – jatkotehtävä

# Tässä jatkotehtävässä sama ohjelma rakennetaan uudelleen selkeämpään muotoon.
# Tavoitteena on oppia käyttämään funktioita, jotta toistuva koodi voidaan koota omiksi osikseen.

# Rakenna ohjelmaa yksi vaihe kerrallaan.
# Testaa ohjelmaa aina jokaisen vaiheen jälkeen ennen kuin siirryt eteenpäin.

# VAIHE 1
# Tee funktio nimeltä kysy_kysymys.
# Funktion tulee saada kolme parametria:
# - kysymys
# - vaihtoehdot
# - oikea_vastaus
#
# Funktion tehtävä:
# 1. tulostaa tyhjä rivi
# 2. tulostaa kysymys
# 3. tulostaa kaikki vaihtoehdot for-silmukan avulla
# 4. kysyä käyttäjän vastaus
# 5. tarkistaa while-silmukalla, että vastaus on A, B tai C
# 6. tarkistaa if-rakenteella, onko vastaus oikea
# 7. palauttaa 1, jos vastaus on oikein, muuten 0

def kysy_kysymys(kysymys, vaihtoehdot, oikea_vastaus):
    # Tulosta tyhjä rivi.

    # Tulosta kysymys.

    # Tulosta kaikki vaihtoehdot for-silmukalla.
    # Vinkki:
    # for vaihtoehto in vaihtoehdot:
    #     print(vaihtoehto)

    # Pyydä käyttäjän vastaus ja tallenna se muuttujaan vastaus.
    vastaus = input("Valitse A, B tai C: ").strip().upper()

    # Tarkista while-silmukalla, että vastaus on A, B tai C.
    # Jos vastaus on jokin muu, pyydä uusi vastaus.
    # Vinkki:
    # while vastaus not in ["A", "B", "C"]:
    #     vastaus = input("Anna vain A, B tai C: ").strip().upper()

    # Kirjoita if-rakenne:
    # jos vastaus on sama kuin oikea_vastaus:
    #     tulosta Oikein!
    #     palauta 1
    # muuten:
    #     tulosta Väärin.
    #     palauta 0
    #
    # Muista sisennys.


# TESTAA TÄSSÄ VAIHEESSA
# Funktion pitäisi olla kirjoitettu ilman virheitä.
# Tässä vaiheessa ohjelma ei vielä tee näkyvästi mitään.
# Tämä vaihe vastaa sitä, että ohjelman toistuva rakenne erotetaan omaksi osakseen.


# VAIHE 2
# Tee funktio nimeltä nayta_lopputulos.
# Funktion tulee saada parametriksi pisteet.
#
# Funktion tehtävä:
# 1. tulostaa teksti: Peli päättyi.
# 2. tulostaa pistemäärä muodossa Sait X/3 pistettä.
# 3. antaa palautetta tuloksen perusteella

def nayta_lopputulos(pisteet):
    # Tulosta tyhjä rivi ja teksti: Peli päättyi.

    # Tulosta pistemäärä.
    # Vinkki:
    # print(f"Sait {pisteet}/3 pistettä.")

    # Kirjoita if-rakenne:
    # jos pisteet ovat 3:
    #     tulosta Loistavaa! Sait kaikki oikein.
    # elif pisteet ovat 2:
    #     tulosta Hyvä! Osasit jo paljon.
    # muuten:
    #     tulosta Harjoittele vielä lisää.


# TESTAA TÄSSÄ VAIHEESSA
# Tarkista, että myös tämä funktio on kirjoitettu ilman virheitä.
# Tämä vaihe vastaa Scratch-ohjelman lopetusruudun logiikkaa.


# VAIHE 3
# Tee funktio nimeltä suorita_peli.
# Tämä funktio vastaa yhdestä kokonaisesta pelikierroksesta.
#
# Funktion tehtävä:
# 1. luoda muuttuja pisteet ja asettaa sen alkuarvoksi 0
# 2. tulostaa ohjelman otsikko
# 3. pyytää käyttäjää painamaan Enteriä aloittaakseen
# 4. kysyä kolme kysymystä kutsumalla kysy_kysymys-funktiota
# 5. kutsua lopuksi nayta_lopputulos-funktiota

def suorita_peli():
    # Luo muuttuja pisteet ja aseta sen alkuarvoksi 0.

    # Tulosta ohjelman otsikko:
    # Tervetuloa visailemaan aiheesta: Turvalliset valinnat verkossa

    # Pyydä käyttäjää painamaan Enteriä aloittaakseen.

    # Kutsu kysy_kysymys-funktiota ensimmäiselle kysymykselle
    # ja lisää sen palauttama arvo pisteisiin.
    # Oikea vastaus on "B".
    #
    # Vinkki:
    # pisteet += kysy_kysymys(
    #     "kysymysteksti",
    #     ["A: ...", "B: ...", "C: ..."],
    #     "B"
    # )

    # Kirjoita tähän ensimmäinen kysymys.


    # Kutsu kysy_kysymys-funktiota toiselle kysymykselle.
    # Oikea vastaus on "B".

    # Kirjoita tähän toinen kysymys.


    # Kutsu kysy_kysymys-funktiota kolmannelle kysymykselle.
    # Oikea vastaus on "C".

    # Kirjoita tähän kolmas kysymys.


    # Kutsu lopuksi nayta_lopputulos-funktiota ja anna sille pisteet parametriksi.


# TESTAA TÄSSÄ VAIHEESSA
# Ohjelman pitäisi nyt pystyä suorittamaan yksi kokonainen pelikierros.
# Tämä vastaa Scratch-ohjelman valmista toteutusta alusta loppuun.


# VAIHE 4
# Tee funktio nimeltä paaohjelma.
# Tämä funktio huolehtii siitä, että peli voidaan aloittaa uudelleen.
#
# Funktion tehtävä:
# 1. suorittaa peli
# 2. kysyä, haluaako käyttäjä pelata uudelleen
# 3. tarkistaa, että käyttäjä syöttää vain k tai e
# 4. lopettaa ohjelman, jos käyttäjä valitsee e

def paaohjelma():
    # Tee while True -silmukka.

        # Kutsu suorita_peli-funktiota.

        # Pyydä käyttäjältä vastaus:
        # Haluatko aloittaa alusta? (k/e)
        # Tallenna vastaus muuttujaan uudelleen.
        # Vinkki:
        # uudelleen = input(...).strip().lower()

        # Tarkista while-silmukalla, että vastaus on joko "k" tai "e".
        # Jos ei ole, pyydä uusi vastaus.

        # Kirjoita if-ehto:
        # jos uudelleen on "e":
        #     tulosta Ohjelma päättyy.
        #     lopeta silmukka break-komennolla

# TESTAA TÄSSÄ VAIHEESSA
# Ohjelman pitäisi nyt pystyä käynnistymään uudelleen.
# Tämä vastaa Scratch-ohjelman "Aloita alusta" -toimintoa.

# VAIHE 5
# Kutsu lopuksi paaohjelma-funktiota, jotta ohjelma käynnistyy.
