import sqlite3
from pot import pot_do_mape


pot_glavne_mape = pot_do_mape()                

povezava_na_bazo = sqlite3.connect(f"{pot_glavne_mape}/baza/baza.db")      # ustvari povezavo z bazo
kazalec = povezava_na_bazo.cursor()                                        # stvari kazalec za izvajanje SQL poizvedb


def preveri_prijavo(vnesen_id_zaposlenega, vneseno_geslo):
    '''preveri, ali je uporabnik vnesel pravilne podatke za prijavo'''

    sql =   f""" SELECT * FROM zaposleni 
                    WHERE id_zaposlenega = {vnesen_id_zaposlenega} 
                        AND 
                    geslo = '{vneseno_geslo}' 
             """

    kazalec.execute(sql)
    rezultat = kazalec.fetchone()

    return rezultat


povezava_na_bazo.close()         # zapre povezavo z bazo
