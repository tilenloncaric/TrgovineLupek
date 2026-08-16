import sqlite3


def moja_poslovalnica(vnesen_id_zaposlenega, pot_do_baze):
    '''prikaže podatke poslovalnice, kjer je zaposlen uporabnik'''

    povezava_na_bazo = sqlite3.connect(pot_do_baze)
    cursor = povezava_na_bazo.cursor() 

    sql =   """ SELECT poslovalnice.ime, poslovalnice.delovni_cas, poslovalnice.postna_stevilka, poslovalnice.kraj, poslovalnice.naslov, poslovalnice.telefon FROM poslovalnice 
                    JOIN zaposleni ON zaposleni.id_poslovalnice = poslovalnice.id_poslovalnice
                        WHERE zaposleni.id_zaposlenega = ? 
            """

    cursor.execute(sql, (vnesen_id_zaposlenega))
    rezultat = cursor.fetchone()

    povezava_na_bazo.close()         # zapre povezavo z bazo

    return rezultat


def poslovodja(vnesen_id_zaposlenega, pot_do_baze):
    '''izpiše ime in priimek poslovodje poslovalnice, kjer je zaposlen uporabnik'''

    povezava_na_bazo = sqlite3.connect(pot_do_baze)
    cursor = povezava_na_bazo.cursor() 

    sql =   """ SELECT ime, priimek FROM zaposleni 
                    WHERE delovno_mesto = 'Poslovodja'
                            AND
                          id_poslovalnice = (SELECT id_poslovalnice FROM zaposleni 
                                                WHERE id_zaposlenega = ?)
            """

    cursor.execute(sql, (vnesen_id_zaposlenega))
    rezultat = cursor.fetchone()

    povezava_na_bazo.close()         # zapre povezavo z bazo

    return rezultat


def izmenovodje(vnesen_id_zaposlenega, pot_do_baze):
    '''izpiše ime in priimek izmenovodij poslovalnice, kjer je zaposlen uporabnik'''

    povezava_na_bazo = sqlite3.connect(pot_do_baze)
    cursor = povezava_na_bazo.cursor() 

    sql =   """ SELECT ime, priimek FROM zaposleni 
                    WHERE delovno_mesto = 'Izmenovodja'
                            AND
                          id_poslovalnice = (SELECT id_poslovalnice FROM zaposleni 
                                                WHERE id_zaposlenega = ?)
            """
   
    cursor.execute(sql, (vnesen_id_zaposlenega))
    rezultat = cursor.fetchall()                          # .fetchall() je za več vrstic

    povezava_na_bazo.close()         # zapre povezavo z bazo

    return rezultat
    

def prodajalci(vnesen_id_zaposlenega, pot_do_baze):
    '''izpiše ime in priimek sodelavcev poslovalnice, kjer je zaposlen uporabnik'''

    povezava_na_bazo = sqlite3.connect(pot_do_baze)
    cursor = povezava_na_bazo.cursor() 

    sql =   """ SELECT ime, priimek FROM zaposleni 
                    WHERE (delovno_mesto = 'Prodajalec' OR delovno_mesto = 'Prodajalka')
                            AND
                           id_poslovalnice = (SELECT id_poslovalnice FROM zaposleni 
                                                WHERE id_zaposlenega = ?)
            """
    
    cursor.execute(sql, (vnesen_id_zaposlenega))
    rezultat = cursor.fetchall()

    povezava_na_bazo.close()         # zapre povezavo z bazo

    return rezultat
    
