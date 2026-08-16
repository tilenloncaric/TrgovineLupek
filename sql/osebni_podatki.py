import sqlite3


def osebni_podatki(vnesen_id_zaposlenega, pot_do_baze):
    '''prikaže osebne podatke zaposlenega'''

    povezava_na_bazo = sqlite3.connect(pot_do_baze)
    cursor = povezava_na_bazo.cursor()

    sql =   """ SELECT zaposleni.ime, zaposleni.priimek, zaposleni.spol, zaposleni.delovno_mesto, poslovalnice.ime FROM zaposleni 
                    JOIN poslovalnice ON zaposleni.id_poslovalnice = poslovalnice.id_poslovalnice
                        WHERE zaposleni.id_zaposlenega = ? 
            """

    
    cursor.execute(sql, (vnesen_id_zaposlenega,))  # potrebna vejica, da se naredi tuple, sicer ne dela?????
    rezultat = cursor.fetchone()

    povezava_na_bazo.close()         # zapre povezavo z bazo


    return rezultat
