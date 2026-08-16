import sqlite3


def tabela(izbrano_leto):
    '''vrne ime tabele (kot niz), ki vsebuje podatke o evidenci zaposlenega za izbrano leto'''
    return f'evidenca{izbrano_leto}'


def datum(izbran_mesec, izbrano_leto):
    '''vrne datum (kot niz)'''
    return f'%{izbran_mesec}.{izbrano_leto}'


def oddelane_ure_v_mesecu(vnesen_id_zaposlenega, izbran_mesec, izbrano_leto, pot_do_baze):
    '''sešteje oddelane ure zaposlenega v izbranem mesecu in letu'''

    povezava_na_bazo = sqlite3.connect(pot_do_baze)
    cursor = povezava_na_bazo.cursor()

    sql =  f""" SELECT SUM(strftime('%s', cas_odhoda) - strftime('%s', cas_prihoda)) FROM {tabela(izbrano_leto)}
                    WHERE datum LIKE ?
                            AND 
                        id_zaposlenega = ?
            """
    
    cursor.execute(sql, (datum(izbran_mesec, izbrano_leto), vnesen_id_zaposlenega)) 
    rezultat = cursor.fetchone()

    povezava_na_bazo.close()         # zapre povezavo z bazo

    return rezultat
                            
                            
def oddelane_ure_za_posamezen_dan(vnesen_id_zaposlenega, izbran_mesec, izbrano_leto, pot_do_baze):
    
    povezava_na_bazo = sqlite3.connect(pot_do_baze)
    cursor = povezava_na_bazo.cursor()

    sql =  f""" SELECT datum, (strftime('%s', cas_odhoda) - strftime('%s', cas_prihoda)) FROM {tabela(izbrano_leto)}
                    WHERE datum LIKE ?
                            AND 
                        id_zaposlenega = ?
            """
    
    cursor.execute(sql, (datum(izbran_mesec, izbrano_leto), vnesen_id_zaposlenega))  # potrebna vejica, da se naredi tuple, sicer ne dela?????
    rezultat = cursor.fetchall()

    povezava_na_bazo.close()         # zapre povezavo z bazo

    return rezultat
    

def delovna_obveznost_v_mesecu(vnesen_id_zaposlenega, izbran_mesec, izbrano_leto, pot_do_baze):
    
    povezava_na_bazo = sqlite3.connect(pot_do_baze)
    cursor = povezava_na_bazo.cursor()

    sql =  f""" SELECT SUM(delovna_obveznost) * 3600 FROM {tabela(izbrano_leto)}
                    WHERE datum LIKE ?
                            AND 
                        id_zaposlenega = ?
            """
    
    cursor.execute(sql, (datum(izbran_mesec, izbrano_leto), vnesen_id_zaposlenega))  # potrebna vejica, da se naredi tuple, sicer ne dela?????
    rezultat = cursor.fetchone()

    povezava_na_bazo.close()         # zapre povezavo z bazo

    return rezultat
    

def delovna_obveznost_dan(vnesen_id_zaposlenega, izbran_mesec, izbrano_leto, pot_do_baze):
    
    povezava_na_bazo = sqlite3.connect(pot_do_baze)
    cursor = povezava_na_bazo.cursor()

    sql =  f""" SELECT datum, delovna_obveznost FROM {tabela(izbrano_leto)}
                    WHERE datum LIKE ?
                            AND 
                        id_zaposlenega = ?
            """
    
    cursor.execute(sql, (datum(izbran_mesec, izbrano_leto), vnesen_id_zaposlenega))  # potrebna vejica, da se naredi tuple, sicer ne dela?????
    rezultat = cursor.fetchall()

    povezava_na_bazo.close()         # zapre povezavo z bazo

    return rezultat
    


# to v glavni kodi samo naredi, ne rabiš dvojnega tukaj
def razlika_mesec(vnesen_id_zaposlenega, izbran_mesec, izbrano_leto, pot_do_baze):
    '''izračuna razliko med oddelanimi urami in delovno obveznostjo zaposlenega v izbranem mesecu in letu'''
    return oddelane_ure_v_mesecu(vnesen_id_zaposlenega, izbran_mesec, izbrano_leto, pot_do_baze) - delovna_obveznost_v_mesecu(vnesen_id_zaposlenega, izbran_mesec, izbrano_leto, pot_do_baze)


def razlika_dan(vnesen_id_zaposlenega, izbran_mesec, izbrano_leto, pot_do_baze):
    '''izračuna razliko med oddelanimi urami in delovno obveznostjo zaposlenega v izbranem mesecu in letu'''

    razlika = oddelane_ure_za_posamezen_dan(vnesen_id_zaposlenega, izbran_mesec, izbrano_leto) - delovna_obveznost_dan(vnesen_id_zaposlenega, izbran_mesec, izbrano_leto)
