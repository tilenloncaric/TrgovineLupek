def tabela(izbrano_leto):
  return f'prodaja{izbrano_leto}'

def poslovalnica_uporabnika(vpisan_id_uporabnika, pot_do_baze):
  povezava_na_bazo = sqlite3.connect(pot_do_baze)
    cursor = povezava_na_bazo.cursor()

  sql = f"""SELECT id_poslovalnice FROM zaposleni
    WHERE id_zaposlenega = vpisan_id_uporabnika
"""

cursor.execute(sql, (stevilka_racuna))  
      rezultat = cursor.fetchone()

      povezava_na_bazo.close()         # zapre povezavo z bazo

      return rezultat
poslovalnica = poslovalnica_uporabnika(vpisan_id_uporabnika)
    
def sestevek_letne_prodaje(poslovalnica, izbrano_leto, pot_do_baze):
  povezava_na_bazo = sqlite3.connect(pot_do_baze)
    cursor = povezava_na_bazo.cursor()

  prodaja = tabela(izbrano_leto)
  
  sql = f"""SELECT SUM(prodaja.kolicina * izdelki.prodajna_cena) FROM prodaja
    JOIN izdelki ON izdelki.ime = prodaja.izdelek
      WHERE prodaja.id_poslovalnice = poslovalnica
"""

cursor.execute(sql, (stevilka_racuna))  
      rezultat = cursor.fetchone()

      povezava_na_bazo.close()         # zapre povezavo z bazo

      return rezultat
def top10(poslovalnica, izbrano_leto, pot_do_baze):
  povezava_na_bazo = sqlite3.connect(pot_do_baze)
    cursor = povezava_na_bazo.cursor()

  prodaja = tabela(izbrano_leto)
  sql = f"""SELECT izdelek, SUM(kolicina) FROM prodaja
    WHERE id_poslovalnice = poslovalnica
      GROUP BY izdelek
        ORDER BY SUM(kolicina) DESC
          LIMIT 10
"""
cursor.execute(sql, (stevilka_racuna))  
      rezultat = cursor.fetchone()

      povezava_na_bazo.close()         # zapre povezavo z bazo

      return rezultat

def najslabsih10(poslovalnica, izbrano_leto, pot_do_baze):
  povezava_na_bazo = sqlite3.connect(pot_do_baze)
    cursor = povezava_na_bazo.cursor()

  prodaja = tabela(izbrano_leto)
  sql = f"""SELECT izdelek, SUM(kolicina) FROM prodaja
    WHERE id_poslovalnice = poslovalnica
      GROUP BY izdelek
        ORDER BY SUM(kolicina) ASC
          LIMIT 10
"""

cursor.execute(sql, (stevilka_racuna))  
      rezultat = cursor.fetchone()

      povezava_na_bazo.close()         # zapre povezavo z bazo

      return rezultat
def mesecna_prodaja_v_izbranem_letu(poslovalnica, izbrano_leto, pot_do_baze):     
  TREBA ŠE POPRAVIT
povezava_na_bazo = sqlite3.connect(pot_do_baze)
    cursor = povezava_na_bazo.cursor()

  prodaja = tabela(izbrano_leto)
  sql = f"""SELECT datum, SUM(prodaja.kolicina * izdelki.prodajna_cena) FROM prodaja
    JOIN izdelki ON izdelki.ime = prodaja.izdelek
      WHERE prodaja.id_poslovalnice = poslovalnica
  """

cursor.execute(sql, (stevilka_racuna))  
      rezultat = cursor.fetchone()

      povezava_na_bazo.close()         # zapre povezavo z bazo

      return rezultat

def nabavna_cena_v_letu((poslovalnica, izbrano_leto, pot_do_baze):
  povezava_na_bazo = sqlite3.connect(pot_do_baze)
    cursor = povezava_na_bazo.cursor()

  prodaja = tabela(izbrano_leto)
  sql = f"""SELECT SUM(prodaja.kolicina * izdelki.nabavna_cena) FROM prodaja
    JOIN izdelki ON izdelki.ime = prodaja.izdelek
      WHERE prodaja.id_poslovalnice = poslovalnica
"""

cursor.execute(sql, (stevilka_racuna))  
      rezultat = cursor.fetchone()

      povezava_na_bazo.close()         # zapre povezavo z bazo

      return rezultat

def ustvarjen_profit(poslovalnica, izbrano_leto):
  return sestevek_letne_prodaje(poslovalnica, izbrano_leto) - nabavna_cena_v_letu((poslovalnica, izbrano_leto)

def najboljsi_dan_prodaje(poslovalnica, izbrano_leto, pot_do_baze):
  povezava_na_bazo = sqlite3.connect(pot_do_baze)
    cursor = povezava_na_bazo.cursor()

  prodaja = tabela(izbrano_leto)
  sql = f"""SELECT datum, SUM(prodaja.kolicina * izdelki.prodajna_cena) AS dnevni_prihodek FROM prodaja
    JOIN izdelki ON izdelki.ime = prodaja.izdelek
      WHERE prodaja.id_poslovalnice = poslovalnica
        GROUP BY datum
          ORDER BY dnevni_prihodek DESC
            LIMIT 1
"""

cursor.execute(sql, (stevilka_racuna))  
      rezultat = cursor.fetchone()

      povezava_na_bazo.close()         # zapre povezavo z bazo

      return rezultat
def najslabsi_dan_prodaje(poslovalnica, izbrano_leto, pot_do_baze):
  
  povezava_na_bazo = sqlite3.connect(pot_do_baze)
    cursor = povezava_na_bazo.cursor()

  prodaja = tabela(izbrano_leto)
  sql = f"""SELECT datum, SUM(prodaja.kolicina * izdelki.prodajna_cena) AS dnevni_prihodek FROM prodaja
    JOIN izdelki ON izdelki.ime = prodaja.izdelek
      WHERE prodaja.id_poslovalnice = poslovalnica
        GROUP BY datum
          ORDER BY dnevni_prihodek ASC
            LIMIT 1
"""

cursor.execute(sql, (stevilka_racuna))  
      rezultat = cursor.fetchone()

      povezava_na_bazo.close()         # zapre povezavo z bazo

      return rezultat

def stevilo_prodaj(poslovalnica, izbrano_leto, pot_do_baze):  group by se je potrebno
povezava_na_bazo = sqlite3.connect(pot_do_baze)
    cursor = povezava_na_bazo.cursor()

  prodaja = tabela(izbrano_leto)
  sql = f"""SELECT COUNT(DISTINCT id_racuna) FROM prodaja
    WHERE id_poslovalnice = poslovalnica
"""

cursor.execute(sql, (stevilka_racuna))  
      rezultat = cursor.fetchone()

      povezava_na_bazo.close()         # zapre povezavo z bazo

      return rezultat
def napoved_prodaje(poslovalnica, izbran_izdelek, pot_do_baze):     
  DODATI JE ŠE TREBA V KATERI POSLOVALNICI NAJ GLEDA
povezava_na_bazo = sqlite3.connect(pot_do_baze)
    cursor = povezava_na_bazo.cursor()

 sql =f""" WITH leto2024 AS (SELECT SUM(kolicina) AS kolicina2024 FROM prodaja2024
                      WHERE izdelek = izbran_izdelek),
       leto2025 AS (SELECT SUM(kolicina) AS kolicina2025 FROM prodaja2025
                      WHERE izdelek = izbran_izdelek)
  SELECT kolicina2024, kolicina2025, (kolicina2025 * (1 + (kolicina2025 - kolicina2024) / kolicina2024)) FROM leto2024
    CROSS JOIN leto2025
  """

cursor.execute(sql, (stevilka_racuna))  
      rezultat = cursor.fetchone()

      povezava_na_bazo.close()         # zapre povezavo z bazo

      return rezultat
