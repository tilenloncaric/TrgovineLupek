import sqlite3
import os


def sestevek_ur(vnesen_id_zaposlenega, izbran_mesec, izbrano_leto):
    '''sešteje oddelane ure zaposlenega v izbranem mesecu in letu'''

    sql =   SELECT
SUM((
    CAST(substr(konec_izmene, 1, 2) AS INTEGER) * 3600 +
    CAST(substr(konec_izmene, 4, 2) AS INTEGER) * 60 +
    CAST(substr(konec_izmene, 7, 2) AS INTEGER)
)
-
(
    CAST(substr(zacetek_izmene, 1, 2) AS INTEGER) * 3600 +
    CAST(substr(zacetek_izmene, 4, 2) AS INTEGER) * 60 +
    CAST(substr(zacetek_izmene, 7, 2) AS INTEGER)
))
FROM evidenca{izbrano_leto} WHERE id_zaposlenega = vnesen_id_zaposlenega
AND datum LIKE '%.{izbran_mesec}.{izbrano_leto}';


def poracun_ur():

    poracun = sestevek_ur(vnesen_id_zaposlenega, izbran_mesec, izbrano_leto) - (f"""SELECT SUM(delovna_obveznost) FROM evidenca{izbrano_leto} WHERE id_zaposlenega = vnesen_id_zaposlenega
                                                                                AND datum LIKE '%.{izbran_mesec}.{izbrano_leto}""")


def izpis_