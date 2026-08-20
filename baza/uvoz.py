import pandas as pd     # delo s CSV datotekami
import sqlite3          # delo s SQLite bazo
import os               # delo s datotekami


def ustvari_bazo_in_uvozi_podatke():
    """ustvari SQLite bazo in uvozi podatke iz CSV datotek v tabele baze. Če baza že obstaja, ne ustvarja nove baze in ne uvaža podatkov"""

    trenutna_mapa = os.path.dirname(os.path.abspath(__file__))                       # mapa, kjer se nahaja trenutna .py datoteka
    glavna_mapa = os.path.dirname(trenutna_mapa)                                     # pot do glavne mape projekta (ena mapa nad trenutno mapo)

    # če baza že obstaja, ne ustvarja nove baze in ne uvaža podatkov
    if not os.path.exists(os.path.join(trenutna_mapa, "baza.db")):
        povezava_na_bazo = sqlite3.connect(os.path.join(trenutna_mapa, "baza.db"))       # ustvari povezavo na SQLite bazo (če ne obstaja, se ustvari nova)
        cursor = povezava_na_bazo.cursor()                                               # kazalec oziroma orodje za izvajanje SQL ukazov


        # ustvari tabelo z imenom "evidenca2024" z določenimi stolpci in omejitvami
        # stolpec id_zaposlenega v tabeli evidenca2024 mora vsebovati samo številke zaposlenih, ki že obstajajo v tabeli zaposleni
        cursor.execute("""
        CREATE TABLE evidenca (
            id INTEGER PRIMARY KEY,
            id_zaposlenega INTEGER NOT NULL,
            datum TEXT NOT NULL,
            cas_prihoda TEXT NOT NULL,
            cas_odhoda TEXT NOT NULL,
            delovna_obveznost INTEGER NOT NULL CHECK (delovna_obveznost > 0),

            FOREIGN KEY (id_zaposlenega)
                REFERENCES zaposleni(id_zaposlenega)
        );
        """)

        # ustvari tabelo z imenom "izdelki" z določenimi stolpci in omejitvami
        cursor.execute("""
        CREATE TABLE izdelki (
            id INTEGER PRIMARY KEY,
            ime TEXT UNIQUE NOT NULL,
            nabavna_cena REAL NOT NULL,
            prodajna_cena REAL NOT NULL,
            drzava_porekla TEXT NOT NULL,
            dobavitelj TEXT NOT NULL,
            id_izdelka INTEGER UNIQUE NOT NULL
        );
        """)

        # ustvari tabelo z imenom "poslovalnice" z določenimi stolpci in omejitvami
        cursor.execute("""
        CREATE TABLE poslovalnice (
            id INTEGER PRIMARY KEY,
            ime TEXT UNIQUE NOT NULL,
            id_poslovalnice INTEGER UNIQUE NOT NULL,
            delovni_cas TEXT NOT NULL,
            kraj TEXT NOT NULL,
            naslov TEXT NOT NULL,
            postna_stevilka TEXT NOT NULL,
            telefon TEXT NOT NULL
        );
        """)

        # ustvari tabelo z imenom "prodaja2024" z določenimi stolpci in omejitvami
        cursor.execute("""
        CREATE TABLE prodaja (
            id INTEGER PRIMARY KEY,
            id_racuna INTEGER NOT NULL,
            izdelek TEXT NOT NULL,
            datum TEXT NOT NULL,
            id_prodajalca INTEGER NOT NULL,
            id_poslovalnice INTEGER NOT NULL,
            kolicina INTEGER NOT NULL CHECK (kolicina > 0),

            FOREIGN KEY (izdelek)
                REFERENCES izdelki(ime),

            FOREIGN KEY (id_prodajalca)
                REFERENCES zaposleni(id_zaposlenega),

            FOREIGN KEY (id_poslovalnice)
                REFERENCES poslovalnice(id_poslovalnice)
        );
        """)

        # ustvari tabelo z imenom "zaposleni" z določenimi stolpci in omejitvami
        cursor.execute("""
        CREATE TABLE zaposleni (
            id INTEGER PRIMARY KEY,
            ime TEXT NOT NULL,
            priimek TEXT NOT NULL,
            spol TEXT NOT NULL CHECK (spol IN ('Moški', 'Ženski')),
            delovno_mesto TEXT NOT NULL CHECK (delovno_mesto IN ('Poslovodja', 'Izmenovodja', 'Prodajalec', 'Prodajalka')),
            id_poslovalnice INTEGER NOT NULL,
            id_zaposlenega INTEGER UNIQUE NOT NULL,
            geslo INTEGER NOT NULL,

            FOREIGN KEY (id_poslovalnice)
                REFERENCES poslovalnice(id_poslovalnice)
        );
        """)


        # branje CSV datotek, ki se nahajajo v mapi "podatki" znotraj glavne mape projekta
        evidenca = pd.read_csv(os.path.join(glavna_mapa, "podatki", "evidenca.csv"), sep=",", encoding="utf-8")
        izdelki = pd.read_csv(os.path.join(glavna_mapa, "podatki", "izdelki.csv"), sep=",", encoding="utf-8")
        poslovalnice = pd.read_csv(os.path.join(glavna_mapa, "podatki", "poslovalnice.csv"), sep=",", encoding="utf-8")
        prodaja = pd.read_csv(os.path.join(glavna_mapa, "podatki", "prodaja.csv"), sep=",", encoding="utf-8")
        zaposleni = pd.read_csv(os.path.join(glavna_mapa, "podatki", "zaposleni.csv"), sep=",", encoding="utf-8")


        # vnos podatkov v tabele
        # vrstni red je pomemben, ker so nekatere tabele povezane z drugimi tabelami preko tujih ključev (FOREIGN KEY)
        # najprej morajo biti v bazi poslovalnice, izdelki in zaposleni, šele nato lahko vstavimo evidence in prodajo
        poslovalnice.to_sql("poslovalnice", povezava_na_bazo, if_exists="append", index=False)
        izdelki.to_sql("izdelki", povezava_na_bazo, if_exists="append", index=False)
        zaposleni.to_sql("zaposleni", povezava_na_bazo, if_exists="append", index=False)
        evidenca.to_sql("evidenca2024", povezava_na_bazo, if_exists="append", index=False)
        prodaja.to_sql("prodaja2024", povezava_na_bazo, if_exists="append", index=False)


        povezava_na_bazo.commit()      # shrani vse spremembe v bazo
        povezava_na_bazo.close()       # zapri povezavo na bazo
