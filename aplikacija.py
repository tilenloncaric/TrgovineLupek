import os

# poglej če baza že obstaja, če ne jo ustvari sicer ne neradi nič
glavna_mapa = os.path.dirname(os.path.abspath(__file__))     # mapa, kjer se nahaja trenutna .py datoteka

pot_do_baze = os.path.join(trenutna_mapa, "baza", "baza.db"

# če baza že obstaja, ne ustvarja nove baze in ne uvaža podatkov
if not os.path.exists(pot_do_baze)):
  ustvari_bazo_in_uvozi_podatke(pot_do_baze)

# prijava uporabnika, preveri če obstaja

# =====================================================
# UVOZ KNJIŽNIC
# =====================================================

# Flask skrbi za prikaz HTML strani in obdelavo zahtevkov
from flask import Flask, render_template, request

# Uvozimo funkcijo za prijavo iz mape sql
from sql import prijava    # klic funkcije delaš kot prijava.preveri_prijavo()
from sql import osebni_podatki
from sql import moja_poslovalnica
from sql import osebna_evidenca
from sql import racun
from sql import sprememba
from sql import statistika


# ustvari flask aplikacijo
app = Flask(__name__)    


@app.route("/")
def prikazi_prijavo():
  '''odpre spletno stran za prijavo uporabnika'''
  return render_template("prijava.html")


@app.route("/prijava", methods=["POST"])
def prijava():
  '''zahteva podatke za prijavo'''

  # zahteva vnos uporanika
  uporabniska_stevilka = request.form.get("uporabniska_stevilka")
  geslo = request.form.get("geslo")

  # izvede se SQL poizvedba
  uspesna_prijava = preveri_prijavo(uporabniska_stevilka, geslo)

  # če je prijava uspešna se odpre začetna stran, sicer se odpre stran, ki javi napako
  if uspesna_prijava:
    return render_template("zacetna_stran.html")
  else:
    return render_template("napaka_v_prijavi.html")


@app.route("/osebni_podatki")
def osebni_podatki():
  return render_template("osebni_podatki.html")


@app.route("/moja_poslovalnica")
def moja_poslovalnica():
  return render_template("moja_poslovalnica.html")


@app.route("/osebna_evidenca")
def osebna_evidenca():
  return render_template("osebna_evidenca.html")


@app.route("/izpis_racunov")
def izpis_racunov():
  return render_template("izpis_racunov.html")


@app.route("/poslovna_statistika")
def poslovna_statistika():
  return render_template("poslovna_statistika.html")

# zagon strežnika
if __name__ == "__main__":
  app.run(debug=True)

# začetna stran, ki pove dobrodošli v trgovine lupek, potem so zgoaj zavihtki na katere lahko uporabnik stisne

# če stisne zavihek Osebna evdenca - izpiše se osebna evidenca, Statistika - pokaže se možnost izbire kakšna statistika ga zanima

