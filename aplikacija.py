import os

# poglej če baza že obstaja, če ne jo ustvari sicer ne neradi nič
glavna_mapa = os.path.dirname(os.path.abspath(__file__))     # mapa, kjer se nahaja trenutna .py datoteka

pot_do_baze = os.path.join(trenutna_mapa,, baza "baza.db"

# če baza že obstaja, ne ustvarja nove baze in ne uvaža podatkov
if not os.path.exists(pot_do_baze)):
  
  povezava_na_bazo = sqlite3.connect(os.path.join(trenutna_mapa, "baza.db"))       # ustvari povezavo na SQLite bazo (če ne obstaja, se ustvari nova)
  cursor = povezava_na_bazo.cursor()   

# prijava uporabnika, preveri če obstaja

# začetna stran, ki pove dobrodošli v trgovine lupek, potem so zgoaj zavihtki na katere lahko uporabnik stisne

# če stisne zavihek Osebna evdenca - izpiše se osebna evidenca, Statistika - pokaže se možnost izbire kakšna statistika ga zanima

