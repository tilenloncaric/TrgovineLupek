import sqlite3


def moja_poslovalnica(vnesen_id_zaposlenega):
    '''prikaže podatke poslovalnice, kjer je zaposlen uporabnik'''

    sql =   """ SELECT poslovalnice.ime, poslovalnice.delovni_cas, poslovalnice.postna_stevilka, poslovalnice.kraj, poslovalnice.naslov, poslovalnice.telefon FROM poslovalnice 
                    JOIN zaposleni ON zaposleni.id_poslovanice = poslovanice.id_poslovanice
                        WHERE zaposleni.id_zaposlenega = vnesen_id_zaposlenega 
            """


def poslovodja(vnesen_id_zaposlenega):
    '''izpiše ime in priimek poslovodje poslovalnice, kjer je zaposlen uporabnik'''

    sql =   """ SELECT ime, priimek FROM zaposleni 
                    WHERE delovno_mesto = 'Poslovodja'
                        AND
                    id_poslovalnice = (SELECT id_poslovalnice FROM zaposleni 
                                        WHERE id_zaposlenega = vnesen_id_zaposlenega)
            """


def izmenovodje(vnesen_id_zaposlenega):
    '''izpiše ime in priimek izmenovodij poslovalnice, kjer je zaposlen uporabnik'''

    sql =   """ SELECT ime, priimek FROM zaposleni 
                    WHERE delovno_mesto = 'Izmenovodja'
                        AND
                    id_poslovalnice = (SELECT id_poslovalnice FROM zaposleni 
                                        WHERE id_zaposlenega = vnesen_id_zaposlenega)
            """


def sodelavci(vnesen_id_zaposlenega):
    '''izpiše ime in priimek sodelavcev poslovalnice, kjer je zaposlen uporabnik'''

    sql =   """ SELECT ime, priimek FROM zaposleni 
                    WHERE (delovno_mesto = 'Prodajalec' OR delovno_mesto = 'Prodajalka')
                        AND
                    id_poslovalnice = (SELECT id_poslovalnice FROM zaposleni 
                                        WHERE id_zaposlenega = vnesen_id_zaposlenega)
            """
