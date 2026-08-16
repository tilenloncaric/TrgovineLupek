import sqlite3


def ime_tabele(leto_izdaje):
      '''vrne ime tabele, ki vsebuje podatke o prodaji v določenem letu''' 
      return f'prodaja{leto_izdaje}' 


def poslovalnica(stevilka_racuna, leto_izdaje, pot_do_baze):
      '''vrne poslovalnico, v kateri je bil izdan račun'''
      
      povezava_na_bazo = sqlite3.connect(pot_do_baze)
      cursor = povezava_na_bazo.cursor()

      prodaja = ime_tabele(leto_izdaje)
      
      sql = f""" SELECT poslovalnice.ime FROM poslovalnice
                  JOIN {prodaja} ON poslovalnice.id_poslovalnice = {prodaja}.id_poslovalnice
                   WHERE {prodaja}.id_racuna = ?  
                    GROUP BY poslovalnice.ime
             """
    
      cursor.execute(sql, (stevilka_racuna))  
      rezultat = cursor.fetchone()

      povezava_na_bazo.close()         # zapre povezavo z bazo

      return rezultat


def skupni_sestevek_prodaje(stevilka_racuna, leto_izdaje, pot_do_baze):
      '''vrne seštevek prodaje za izbran račun'''
      
      povezava_na_bazo = sqlite3.connect(pot_do_baze)
      cursor = povezava_na_bazo.cursor()

      prodaja = ime_tabele(leto_izdaje)

      sql = f""" SELECT SUM({prodaja}.kolicina * izdelki.prodajna_cena) FROM {prodaja} 
                  JOIN izdelki ON {prodaja}.izdelek = izdelki.ime
                   WHERE {prodaja}.id_racuna = ?
             """
    
      cursor.execute(sql, (stevilka_racuna,))  # potrebna vejica, da se naredi tuple, sicer ne dela?????
      rezultat = cursor.fetchone()

      povezava_na_bazo.close()         # zapre povezavo z bazo

      return rezultat


def prodani_izdelki(stevilka_racuna, leto_izdaje, pot_do_baze):
      '''vrne seznam prodanih izdelkov, prodano količino in vmesno ceno posameznega izdelka za izbran račun'''

      povezava_na_bazo = sqlite3.connect(pot_do_baze)
      cursor = povezava_na_bazo.cursor()

      prodaja = ime_tabele(leto_izdaje)

      sql = f""" SELECT {prodaja}.izdelek, {prodaja}.kolicina, {prodaja}.kolicina * izdelki.prodajna_cena) FROM {prodaja}
                  JOIN izdelki ON {prodaja}.izdelek = izdelki.ime
                   WHERE {prodaja}.id_racuna = ?
             """
                   
      cursor.execute(sql, (stevilka_racuna,))  # potrebna vejica, da se naredi tuple, sicer ne dela?????
      rezultat = cursor.fetchall()

      povezava_na_bazo.close()         # zapre povezavo z bazo

      return rezultat
      

def blagajnik(stevilka_racuna, leto_izdaje, pot_do_baze):
      '''vrne ime blagajnika, ki je izdal račun'''
    
      povezava_na_bazo = sqlite3.connect(pot_do_baze)
      cursor = povezava_na_bazo.cursor()
      
      prodaja = ime_tabele(leto_izdaje)
      
      sql = f""" SELECT zaposleni.ime, zaposleni.priimek FROM zaposleni
                  JOIN {prodaja} ON {prodaja}.id_prodajalca = zaposleni.id_zaposlenega
                   WHERE {prodaja}.id_racuna = ?
                    GROUP BY zaposleni.ime
             """
      
      cursor.execute(sql, (stevilka_racuna,))  # potrebna vejica, da se naredi tuple, sicer ne dela?????
      rezultat = cursor.fetchone()
      
      povezava_na_bazo.close()         # zapre povezavo z bazo
      
      return rezultat

    
def datum_izdaje(stevilka_racuna, leto_izdaje, pot_do_baze):
      '''vrne datum izdaje računa'''
      
      povezava_na_bazo = sqlite3.connect(pot_do_baze)
      cursor = povezava_na_bazo.cursor()

      prodaja = ime_tabele(leto_izdaje)

      sql = f""" SELECT datum FROM prodaja
                  WHERE id_racuna = ?
                   GROUP BY datum
             """

      cursor.execute(sql, (stevilka_racuna,))  # potrebna vejica, da se naredi tuple, sicer ne dela?????
      rezultat = cursor.fetchone()

      povezava_na_bazo.close()         # zapre povezavo z bazo

      return rezultat
      
def podatki_poslovalnice(stevilka_racuna, leto_izdaje, pot_do_baze):
      '''vrne podatke o poslovalnici, v kateri je bil izdan račun'''
      
      povezava_na_bazo = sqlite3.connect(pot_do_baze)
      cursor = povezava_na_bazo.cursor()

      prodaja = ime_tabele(leto_izdaje)

      sql = f""" SELECT poslovalnice.ime, poslovalnice.delovni_cas, poslovalnice.postna_stevilka, poslovalnice.kraj, poslovalnice.naslov, poslovalnice.telefon FROM poslovalnice
                  JOIN {prodaja} ON poslovalnice.id_poslovalnice = {prodaja}.id_poslovalnice
                   WHERE {prodaja}.id_racuna = ?
                    GROUP BY poslovalnice.ime
             """
      
      cursor.execute(sql, (stevilka_racuna,))  # potrebna vejica, da se naredi tuple, sicer ne dela?????
      rezultat = cursor.fetchone()

      povezava_na_bazo.close()         # zapre povezavo z bazo


      return rezultat
