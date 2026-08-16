import sqlite3


def preveri_prijavo(vnesen_id_zaposlenega, vneseno_geslo, pot_do_baze):
    '''preveri, ali je uporabnik vnesel pravilne podatke za prijavo'''

    povezava_na_bazo = sqlite3.connect(pot_do_baze)
    cursor = povezava_na_bazo.cursor() 

    sql = """ SELECT * FROM zaposleni 
                WHERE id_zaposlenega = ? 
                        AND 
                      geslo = ? 
          """

    
    cursor.execute(sql, (vnesen_id_zaposlenega, vneseno_geslo))
    rezultat = cursor.fetchone()

    povezava_na_bazo.close()         # zapre povezavo z bazo


    return rezultat
