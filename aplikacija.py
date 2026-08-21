import os

# poglej če baza že obstaja, če ne jo ustvari sicer ne neradi nič
glavna_mapa = os.path.dirname(os.path.abspath(__file__))     # mapa, kjer se nahaja trenutna .py datoteka

pot_do_baze = os.path.join(trenutna_mapa, "baza", "baza.db"

# če baza že obstaja, ne ustvarja nove baze in ne uvaža podatkov
if not os.path.exists(pot_do_baze)):
  ustvari_bazo_in_uvozi_podatke(pot_do_baze)

# prijava uporabnika, preveri če obstaja

# Uvozimo Flask knjižnico.
# Flask skrbi za prikaz HTML strani in komunikacijo med brskalnikom in Pythonom.
from flask import Flask, render_template, request


# Ustvarimo Flask aplikacijo.
# Spremenljivka app predstavlja naš spletni strežnik.
app = Flask(__name__)


# ============================================================
# PRVI KORAK
# Prikažemo prijavno stran.
# ============================================================

# Ko uporabnik odpre:
#
# http://127.0.0.1:5000
#
# Flask izvede spodnjo funkcijo.
@app.route("/")
def prikazi_prijavo():

    # Poišče datoteko:
    # templates/login.html
    #
    # in jo prikaže uporabniku.
    return render_template("login.html")


# ============================================================
# DRUGI KORAK
# Obdelava prijave.
# ============================================================

# Ta funkcija se izvede, ko uporabnik klikne:
#
# "Prijava"
#
# methods=["POST"]
#
# pomeni:
# uporabnik pošilja podatke Python programu.
@app.route("/prijava", methods=["POST"])
def prijava():

    # --------------------------------------------------------
    # PREBERI PODATKE IZ HTML OBRAZCA
    # --------------------------------------------------------

    # Preberemo vrednost iz polja:
    #
    # <input name="uporabnik">
    #
    uporabnik = request.form["uporabnik"]

    # Preberemo vrednost iz polja:
    #
    # <input name="geslo">
    #
    geslo = request.form["geslo"]


    # --------------------------------------------------------
    # SHRANIMO PODATKE
    # --------------------------------------------------------

    # Za prvo verzijo aplikacije ju shranimo
    # v običajen Python slovar.
    #
    # Kasneje jih lahko shranimo:
    # - v session
    # - v bazo
    # - v uporabniški profil
    #
    prijavni_podatki = {

        "uporabnik": uporabnik,

        "geslo": geslo

    }


    # Izpis v terminal.
    #
    # To je koristno za testiranje.
    #
    # Primer:
    #
    # {
    #   'uporabnik': '12345',
    #   'geslo': 'abcdef'
    # }
    #
    print(prijavni_podatki)


    # --------------------------------------------------------
    # POSKUSI IZVESTI SQL PREVERJANJE
    # --------------------------------------------------------

    try:

        # Odpri SQL datoteko.

        with open(
            "sql/preveri_prijavo.sql",
            "r",
            encoding="utf-8"
        ) as datoteka:

            # Preberi celotno SQL poizvedbo.

            sql_poizvedba = datoteka.read()


        # ----------------------------------------------------
        # TUKAJ BO KASNEJE POVEZAVA Z BAZO
        # ----------------------------------------------------
        #
        # Trenutno baze še nimamo.
        #
        # Zato samo simuliramo uspešen rezultat.
        #
        rezultat = True


        # ----------------------------------------------------
        # ČE JE PRIJAVA USPEŠNA
        # ----------------------------------------------------

        if rezultat:

            # Kasneje bomo tukaj odprli
            # naslednjo HTML stran.
            #
            # Zaenkrat samo vrnemo besedilo.
            #
            return "PRIJAVA USPEŠNA"


        # ----------------------------------------------------
        # ČE PRIJAVA NI USPEŠNA
        # ----------------------------------------------------

        else:

            return "NAPAČNO UPORABNIŠKO IME ALI GESLO"


    # --------------------------------------------------------
    # ČE PRIDE DO NAPAKE
    # --------------------------------------------------------

    except Exception as napaka:

        # Izpišemo opis napake.
        #
        # Primer:
        #
        # SQL datoteka ne obstaja
        # Baza ni dosegljiva
        # Napaka v SQL stavku
        #
        return f"NAPAKA: {napaka}"


# ============================================================
# ZAGON PROGRAMA
# ============================================================

# Ta del se izvede samo,
# če zaženemo main.py.

if __name__ == "__main__":

    # debug=True
    #
    # pomeni:
    #
    # - ob spremembi kode se program sam ponovno zažene
    # - v primeru napake vidimo podroben opis
    #
    app.run(debug=True)

# začetna stran, ki pove dobrodošli v trgovine lupek, potem so zgoaj zavihtki na katere lahko uporabnik stisne

# če stisne zavihek Osebna evdenca - izpiše se osebna evidenca, Statistika - pokaže se možnost izbire kakšna statistika ga zanima

