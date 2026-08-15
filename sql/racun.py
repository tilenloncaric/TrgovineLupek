import sqlite3


def ime_tabele(leto_izdaje):
      '''vrne ime tabele, ki vsebuje podatke o prodaji v določenem letu'''

      tabela_s_podatki = f'prodaja{leto_izdaje}'  

      return tabela_s_podatki


def poslovalnica(stevilka_racuna, leto_izdaje):
    '''vrne poslovalnico, v kateri je bil izdan račun'''

    sql =   SELECT poslovalnice.ime FROM poslovalnice
                JOIN tabela_s_podatki ON poslovalnice.id_poslovalnice = tabela_s_podatki.id_poslovalnice
                    WHERE tabela_s_podatki.id_poslovalnice = stevilka_racuna    


def skupni_sestevek_prodaje(stevilka_racuna, leto_izdaje):
    '''vrne seštevek prodaje za izbran račun'''

prodaja = ime_tabele(leto_izdaje)

sql = SELECT SUM(prodaja.kolicina * izdelki.prodajna_cena) FROM prodaja 
      JOIN izdelki ON prodaja.izdelek = izdelki.ime
      WHERE prodaja.id_racuna = stevilka_racuna


def prodani_izdelki(stevilka_racuna, leto_izdaje):
    '''vrne seznam prodanih izdelkov in prodano količino posameznega izdelka za izbran račun'''

    tabela = ime_tabele(leto_izdaje)

    sql =   SELECT izdelek, kolicina FROM tabela
        WHERE id_racuna = stevilka_racuna


def blagajnik(stevilka_racuna, leto_izdaje):
    '''vrne blagajnika, ki je izdal račun'''

def datum_izdaje(stevilka_racuna, leto_izdaje):
    '''vrne datum izdaje računa'''


def podatki_poslovalnice(stevilka_racuna, leto_izdaje):
     '''vrne podatke o poslovalnici, v kateri je bil izdan račun'''
