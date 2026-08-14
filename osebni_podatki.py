import sqlite3
import os


def osebni_podatki(vnesen_id_zaposlenega):
    '''prikaže osebne podatke zaposlenega'''

    sql =   """ SELECT zaposleni.ime, zaposleni.priimek, zaposleni.spol, zaposleni.delovno_mesto, poslovalnice.ime FROM zaposleni 
                    JOIN poslovanice ON zaposleni.id_poslovanice = poslovanice.id_poslovanice
                        WHERE zaposleni.id_zaposlenega = vnesen_id_zaposlenega 
            """