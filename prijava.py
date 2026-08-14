import sqlite3
import os


def preveri_prijavo(vnesen_id_zaposlenega, vneseno_geslo):
    '''preveri, ali je uporabnik vnesel pravilne podatke za prijavo'''

    sql =   """ SELECT * FROM zaposleni 
                    WHERE id_zaposlenega = vnesen_id_zaposlenega 
                        AND 
                    geslo = vneseno_geslo 
            """

    