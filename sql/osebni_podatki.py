import sqlite3


def osebni_podatki(vnesen_id_zaposlenega):
    '''prikaže osebne podatke zaposlenega'''

    sql =   """ SELECT zaposleni.ime, zaposleni.priimek, zaposleni.spol, zaposleni.delovno_mesto, poslovalnice.ime FROM zaposleni 
                    JOIN poslovalnice ON zaposleni.id_poslovalnice = poslovalnice.id_poslovalnice
                        WHERE zaposleni.id_zaposlenega = vnesen_id_zaposlenega 
            """
