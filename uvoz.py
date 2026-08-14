import pandas as pd     # delo s CSV datotekami
import sqlite3          # delo s SQLite bazo
import os               # delo s datotekami in mapami


trenutna_pot = os.path.abspath(__file__)                               # poišče absolutno pot mape, kjer se nahaja datoteka uvoz.py
pozicija = trenutna_pot.find("TrgovineLupek")                          # vrne število znakov, ki jih je potrebno prešteti, da pridemo do začetka besedila "TrgovineLupek" v absolutni poti
pot = trenutna_pot[:pozicija + len("TrgovineLupek")]                   # absolutna pot, kjer se nahaja mapa "TrgovineLupek" (vključno z njo) 


povezava_na_bazo = sqlite3.connect(f"{pot}/baza/baza.db")              # povezava na bazo z imenom 'baza.db'


# branje CSV datotek
evidenca2024 = pd.read_csv(f"{pot}/podatki/evidenca2024.csv", sep=",", encoding="utf-8")
evidenca2025 = pd.read_csv(f"{pot}/podatki/evidenca2025.csv", sep=",", encoding="utf-8")
izdelki = pd.read_csv(f"{pot}/podatki/izdelki.csv", sep=",", encoding="utf-8")
poslovalnice = pd.read_csv(f"{pot}/podatki/poslovalnice.csv", sep=",", encoding="utf-8")
prodaja2024 = pd.read_csv(f"{pot}/podatki/prodaja2024.csv", sep=",", encoding="utf-8")
prodaja2025 = pd.read_csv(f"{pot}/podatki/prodaja2025.csv", sep=",", encoding="utf-8")
zaloga = pd.read_csv(f"{pot}/podatki/zaloga.csv", sep=",", encoding="utf-8")
zaposleni = pd.read_csv(f"{pot}/podatki/zaposleni.csv", sep=",", encoding="utf-8")


# uvoz podatkov iz CSV datotek v SQL tabele
# ob vsakem zagonu izbriše staro tabelo in jo ponovno ustvari
# ne dodaja dodatnih indeksov, saj jih bo SQL tabela ustvarila sama (to že zapisani v CSV datotekah)
evidenca2024.to_sql("evidenca2024", povezava_na_bazo, if_exists="replace", index=False)
evidenca2025.to_sql("evidenca2025", povezava_na_bazo, if_exists="replace", index=False)
izdelki.to_sql("izdelki", povezava_na_bazo, if_exists="replace", index=False)
poslovalnice.to_sql("poslovalnice", povezava_na_bazo, if_exists="replace", index=False)
prodaja2024.to_sql("prodaja2024", povezava_na_bazo, if_exists="replace", index=False)
prodaja2025.to_sql("prodaja2025", povezava_na_bazo, if_exists="replace", index=False)
zaloga.to_sql("zaloga", povezava_na_bazo, if_exists="replace", index=False)
zaposleni.to_sql("zaposleni", povezava_na_bazo, if_exists="replace", index=False)
evidenca2024.to_sql("evidenca2024", povezava_na_bazo, if_exists="replace", index=False)


povezava_na_bazo.commit()   # zapiše spremembe v bazo
povezava_na_bazo.close()    # zapre povezavo z bazo