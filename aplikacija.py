import os

# poglej če baza že obstaja, če ne jo ustvari sicer ne neradi nič
glavna_mapa = os.path.dirname(os.path.abspath(__file__))     # mapa, kjer se nahaja trenutna .py datoteka

pot_do_baze = os.path.join(trenutna_mapa, "baza", "baza.db"

# če baza že obstaja, ne ustvarja nove baze in ne uvaža podatkov
if not os.path.exists(pot_do_baze)):
  ustvari_bazo_in_uvozi_podatke(pot_do_baze)

# prijava uporabnika, preveri če obstaja

# ============================================================
# UVOZ KNJIŽNIC
# ============================================================

# Flask
# Skrbi za prikaz HTML strani in komunikacijo med
# brskalnikom in Python programom.
from flask import Flask, render_template, request


# ============================================================
# USTVARJANJE APLIKACIJE
# ============================================================

# Ustvarimo Flask aplikacijo.
#
# Spremenljivka app predstavlja naš spletni strežnik.
app = Flask(__name__)


# ============================================================
# ZAČETNA STRAN
# ============================================================

# Ko uporabnik odpre:
#
# http://127.0.0.1:5000
#
# Flask pokliče spodnjo funkcijo.
@app.route("/")
def prikazi_prijavo():

    # Odpre HTML datoteko:
    #
    # templates/login.html
    #
    # in jo prikaže uporabniku.
    return render_template("login.html")


# ============================================================
# PRIJAVA
# ============================================================

# Ta funkcija se izvede,
# ko uporabnik klikne gumb "Prijava".
#
# methods=["POST"]
#
# pomeni:
# uporabnik pošilja podatke iz obrazca.
@app.route("/prijava", methods=["POST"])
def prijava():

    # ========================================================
    # PREBERI PODATKE IZ HTML OBRAZCA
    # ========================================================

    # Preberemo uporabniško številko.
    #
    # HTML:
    #
    # <input name="uporabnik">
    #
    uporabnik = request.form["uporabnik"]

    # Preberemo geslo.
    #
    # HTML:
    #
    # <input name="geslo">
    #
    geslo = request.form["geslo"]


    # ========================================================
    # SHRANIMO PODATKE
    # ========================================================

    # Za prvo verzijo aplikacije
    # prijavne podatke shranimo v slovar.
    #
    # Kasneje jih lahko shranimo:
    # - v session
    # - v bazo
    # - v dnevnik prijav
    #
    prijavni_podatki = {

        "uporabnik": uporabnik,

        "geslo": geslo

    }


    # ========================================================
    # IZPIS ZA TESTIRANJE
    # ========================================================

    print("------------------------------------------------")
    print("PREJETI PRIJAVNI PODATKI")
    print(prijavni_podatki)
    print("------------------------------------------------")


    # ========================================================
    # SQL PREVERJANJE
    # ========================================================

    try:

        # ----------------------------------------------------
        # ODPIRANJE SQL DATOTEKE
        # ----------------------------------------------------

        with open(
            "sql/preveri_prijavo.sql",
            "r",
            encoding="utf-8"
        ) as datoteka:

            sql_poizvedba = datoteka.read()

        print("SQL datoteka uspešno prebrana.")


        # ----------------------------------------------------
        # IZPIS SQL ZA TEST
        # ----------------------------------------------------

        print("SQL poizvedba:")
        print(sql_poizvedba)


        # ====================================================
        # TUKAJ BO KASNEJE POVEZAVA Z BAZO
        # ====================================================
        #
        # Trenutno samo simuliramo rezultat.
        #
        # Kasneje bo tukaj:
        #
        # rezultat = izvedi_sql(...)
        #
        rezultat = True


        # ====================================================
        # USPEŠNA PRIJAVA
        # ====================================================

        if rezultat:

            print("Prijava uspešna.")

            # Kasneje bova tukaj odprla
            # naslednjo HTML stran.
            #
            # Trenutno samo vrnemo besedilo.
            return "PRIJAVA USPEŠNA"


        # ====================================================
        # NEUSPEŠNA PRIJAVA
        # ====================================================

        else:

            print(
                "Uporabnik ni bil najden "
                "ali nima pravic za dostop."
            )

            # Odpri HTML stran z napako.
            return render_template(
                "napaka_prijava.html"
            )


    # ========================================================
    # NAPAKA PRI SQL IZVEDBI
    # ========================================================

    except Exception as napaka:

        print("NAPAKA PRI IZVEDBI SQL POIZVEDBE")
        print(napaka)

        # Prikažemo stran z napako.
        return render_template(
            "napaka_prijava.html"
        )


# ============================================================
# ZAGON APLIKACIJE
# ============================================================

# Ta del se izvede samo,
# če zaženemo datoteko main.py.
if __name__ == "__main__":

    # debug=True
    #
    # prednosti:
    # - samodejni ponovni zagon ob spremembi kode
    # - podrobni izpisi napak
    #
    app.run(debug=True)

# začetna stran, ki pove dobrodošli v trgovine lupek, potem so zgoaj zavihtki na katere lahko uporabnik stisne

# če stisne zavihek Osebna evdenca - izpiše se osebna evidenca, Statistika - pokaže se možnost izbire kakšna statistika ga zanima

