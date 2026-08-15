import sqlite3


def tabela(izbrano_leto):
    '''vrne ime tabele, ki vsebuje podatke o evidenci zaposlenega za izbrano leto'''

    tabela_s_podatki = f'evidenca{izbrano_leto}'  

    return tabela_s_podatki


def oddelane_ure_v_mesecu(vnesen_id_zaposlenega, izbran_mesec, izbrano_leto):
    '''sešteje oddelane ure zaposlenega v izbranem mesecu in letu'''

    izbran_datum = f'%{izbran_mesec}.{izbrano_leto}'
    evidenca = tabela(izbrano_leto)

    sql =   """ SELECT SUM(strftime('%s', cas_odhoda) - strftime('%s', cas_prihoda)) FROM evidenca
                    WHERE datum LIKE izbran_datum
                            AND 
                        id_zaposlenega = vnesen_id_zaposlenega
            """
    izpisano v sekundah naj pravilno vrača
                            
                            
def oddelane_ure_za_posamezen_dan(vnesen_id_zaposlenega, izbran_mesec, izbrano_leto):

    izbran_datum = f'%{izbran_mesec}.{izbrano_leto}'
    evidenca = tabela(izbrano_leto)

    sql =   """ SELECT datum, (strftime('%s', cas_odhoda) - strftime('%s', cas_prihoda)) FROM evidenca
                    WHERE datum LIKE izbran_datum
                            AND 
                        id_zaposlenega = vnesen_id_zaposlenega
            """


def delovna_obveznost_v_mesecu(vnesen_id_zaposlenega, izbran_mesec, izbrano_leto):

    izbran_datum = f'%{izbran_mesec}.{izbrano_leto}'
    evidenca = tabela(izbrano_leto)

    sql =   """ SELECT SUM(delovna_obveznost) * 3600 FROM evidenca
                    WHERE datum LIKE izbran_datum
                            AND 
                        id_zaposlenega = vnesen_id_zaposlenega
            """


def delovna_obveznost_dan(vnesen_id_zaposlenega, izbran_mesec, izbrano_leto):

    izbran_datum = f'%{izbran_mesec}.{izbrano_leto}'
    evidenca = tabela(izbrano_leto)

    sql =   """ SELECT datum, delovna_obveznost FROM evidenca
                    WHERE datum LIKE izbran_datum
                            AND 
                        id_zaposlenega = vnesen_id_zaposlenega
            """


def razlika_mesec(vnesen_id_zaposlenega, izbran_mesec, izbrano_leto):
    '''izračuna razliko med oddelanimi urami in delovno obveznostjo zaposlenega v izbranem mesecu in letu'''

    razlika = oddelane_ure_v_mesecu(vnesen_id_zaposlenega, izbran_mesec, izbrano_leto) - delovna_obveznost_v_mesecu(vnesen_id_zaposlenega, izbran_mesec, izbrano_leto)


def razlika_dan(vnesen_id_zaposlenega, izbran_mesec, izbrano_leto):
    '''izračuna razliko med oddelanimi urami in delovno obveznostjo zaposlenega v izbranem mesecu in letu'''

    razlika = oddelane_ure_za_posamezen_dan(vnesen_id_zaposlenega, izbran_mesec, izbrano_leto) - delovna_obveznost_dan(vnesen_id_zaposlenega, izbran_mesec, izbrano_leto)
