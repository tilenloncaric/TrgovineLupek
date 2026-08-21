import os
from baza import uvoz
from flask import Flask, render_template, request, session
from sql import prijava    # klic funkcije delaš kot prijava.preveri_prijavo()
from sql import osebni_podatki
from sql import moja_poslovalnica
from sql import osebna_evidenca
from sql import racun
from sql import sprememba
from sql import statistika


# ustvarjanje baze
glavna_mapa = os.path.dirname(os.path.abspath(__file__))     # mapa, kjer se nahaja trenutna .py datoteka
pot_do_baze = os.path.join(trenutna_mapa, "baza", "baza.db"

# če baza že obstaja, ne ustvarja nove baze in ne uvaža podatkov
if not os.path.exists(pot_do_baze)):
  uvoz.ustvari_bazo_in_uvozi_podatke(pot_do_baze)



# ustvari flask aplikacijo
app = Flask(__name__)    


@app.route("/")
def stran_prijava_v_aplikacijo():
  '''odpre spletno stran za prijavo uporabnika'''
  return render_template("prijava.html")



@app.route("/prijava", methods=["POST"])     # sem na spletni strani prijava.html, 
def stran_prijava():
  '''zahteva podatke za prijavo'''

  # zahteva vnos uporanika
  uporabniska_stevilka = request.form.get("uporabniska_stevilka")
  geslo = request.form.get("geslo")

  # izvede se SQL poizvedba, ki preveri ali v bazi podatkov obstaja uporabnik z vvnešenim uporabniškim imenom in geslom
  preveri_prijavo = prijava.preveri_prijavo(uporabniska_stevilka, geslo)

  # če je prijava uspešna se odpre začetna stran, sicer se odpre stran, ki javi napako
  if preveri_prijavo:
    session["uporabniska_stevilka"] = uporabniska_stevilka   # da je vnesena uporabniška številka vidna vsem uporabnikom
    return render_template("zacetna_stran.html")
  return render_template("napaka_v_prijavi.html")



@app.route("/osebni_podatki")
def stran_osebni_podatki():
  '''izpis osebnih podatkov na spletni strani osebni_podatki.html'''
  
  uporabniska_stevilka = session.get("uporabniska_stevilka")
  ime, priimek, spol, delovno_mesto, poslovalnica = osebni_podatki.osebni_podatki(uporabniska_stevilka, pot_do_baze)
  
  return render_template("osebni_podatki.html", ime=ime, priimek=priimek, delovno_mesto=delovno_mesto, poslovalnice=poslovalnica)



@app.route("/moja_poslovalnica", methods=["GET", "POST"])
def moja_poslovalnica():

    uporabniska_stevilka = session.get("uporabniska_stevilka")

    if request.method == "POST":
        klik_na_gumb = request.form.get("klik_na_gumb")

        if klik_na_gumb == "podatki_poslovalnice":
            poslovalnica, delovni_cas, naslov, telefon = moja_poslovalnica.moja_poslovalnica(uporabniska_stevilka, pot_do_baze)
            return render_template("moja_poslovalnica.html", poslovalnica=poslovalnica, delovni_cas=delovni_cas, naslov=naslov, telefon=telefon)

        elif klik_na_gumb == "sodelavci":
            poslovodja = moja_poslovalnica.poslovodja(uporabniska_stevilka, pot_do_baze)
            izmenovodje = moja_poslovalnica.izmenovodje(uporabniska_stevilka, pot_do_baze)
            prodajalci = moja_poslovalnica.prodajalci(uporabniska_stevilka, pot_do_baze)
            return render_template("moja_poslovalnica.html", poslovodja=poslovodja, izmenovodje=izmenovodje, prodajalci=prodajalci)

    return render_template("moja_poslovalnica.html")



@app.route("/osebna_evidenca")
def stran_osebna_evidenca():
  uporabniska_stevilka = session.get(session.get())
  return render_template("osebna_evidenca.html")


@app.route("/izpis_racunov")
def stran_izpis_racunov():
  return render_template("izpis_racunov.html")


@app.route("/poslovna_statistika")
def stran_poslovna_statistika():
  return render_template("poslovna_statistika.html")

# zagon strežnika
if __name__ == "__main__":
  app.run(debug=True)

# začetna stran, ki pove dobrodošli v trgovine lupek, potem so zgoaj zavihtki na katere lahko uporabnik stisne

# če stisne zavihek Osebna evdenca - izpiše se osebna evidenca, Statistika - pokaže se možnost izbire kakšna statistika ga zanima

