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

    prodaja = ime_tabele(leto_izdaje)

    SELECT prodaja.izdelek, prodaja.kolicina, (prodaja.kolicina * izdelki.prodajna_cena) FROM prodaja
      JOIN izdelki ON prodaja.izdelek = izdelki.ime
        WHERE id_racuna = stevilka_racuna


def blagajnik(stevilka_racuna, leto_izdaje):
    '''vrne blagajnika, ki je izdal račun'''
      prodaja = ime_tabele(leto_izdaje)
      SELECT id_prodajalca FROM prodaja
            WHERE id_racuna = stevilka_racuna
                  GROUP BY id_prodajalca

def datum_izdaje(stevilka_racuna, leto_izdaje):
    '''vrne datum izdaje računa'''
      prodaja = ime_tabele(leto_izdaje)
      SELECT datum FROM prodaja
            WHERE id_racuna = stevilka_racuna
                  GROUP BY datum


def podatki_poslovalnice(stevilka_racuna, leto_izdaje):
     '''vrne podatke o poslovalnici, v kateri je bil izdan račun'''
       prodaja = ime_tabele(leto_izdaje)
      SELECT poslovalnice.ime, poslovalnice.delovni_cas, poslovalnice.postna_stevilka, poslovalnice.kraj, poslovalnice.naslov, poslovalnice.telefon FROM poslovalnice
            JOIN prodaja ON poslovalnice.id_poslovalnice = prodaja.id_poslovalnice
                  WHERE prodaja.id_racuna = stevilka_racuna
      
