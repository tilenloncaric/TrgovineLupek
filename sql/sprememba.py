import sqlite3



def preveri_vnos(vnesen_id_zaposlenega, pot_do_baze):
    '''preveri, ali je uporabnik vnesel takšno uporabniško številko, ki v bazi podatkov že obstaja'''

    povezava_na_bazo = sqlite3.connect(pot_do_baze)      # ustvari povezavo z bazo
    cursor = povezava_na_bazo.cursor()                   # stvari kazalec za izvajanje SQL poizvedb

    sql =   """ SELECT * FROM zaposleni 
                    WHERE id_zaposlenega = ?
             """

    cursor.execute(sql)
    rezultat = cursor.fetchone()

    povezava_na_bazo.close()         # zapre povezavo z bazo

    return rezultat



def dodaj_sodelavca(vseneno_ime, vnesen_priimek, vnesen_spol, vneseno_delovno_mesto, vnesen_id_poslovalnica, vnesen_id_zaposlenega, vneseno_geslo, pot_do_baze):
    '''dodaj novega sodelavca v bazo podatkov'''

    povezava_na_bazo = sqlite3.connect(pot_do_baze)      # ustvari povezavo z bazo
    cursor = povezava_na_bazo.cursor()                   # stvari kazalec za izvajanje SQL poizvedb

    sql =   """ INSERT INTO zaposleni (ime, priimek, spol, delovno_mesto, id_poslovalnice, id_zaposlenega, geslo)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
             """

    cursor.execute(sql)
    rezultat = cursor.fetchone()

    povezava_na_bazo.close()         # zapre povezavo z bazo

    return rezultat



def odstrani_sodelavca(vnesen_id_zaposlenega, pot_do_baze):
    '''odstrani sodelavca iz baze podatkov'''

    povezava_na_bazo = sqlite3.connect(pot_do_baze)      # ustvari povezavo z bazo
    cursor = povezava_na_bazo.cursor()                   # stvari kazalec za izvajanje SQL poizvedb
    
    sql =   """ DELETE FROM zaposleni 
                    WHERE id_zaposlenega = ?
             """

    cursor.execute(sql)
    rezultat = cursor.fetchone()

    povezava_na_bazo.close()         # zapre povezavo z bazo

    return rezultat



def spremeni_podatke_sodelavca(vseneno_ime, vnesen_priimek, vnesen_spol, vneseno_delovno_mesto, vnesen_id_poslovalnica, vnesen_id_zaposlenega, vneseno_geslo, pot_do_baze):
    '''spremeni podatke o sodelavcu v bazi podatkov'''
    
    povezava_na_bazo = sqlite3.connect(pot_do_baze)      # ustvari povezavo z bazo
    cursor = povezava_na_bazo.cursor()                   # stvari kazalec za izvajanje SQL poizvedb
    
    sql =   """ UPDATE zaposleni 
                    SET ime = ?, priimek = ?, spol = ?, delovno_mesto = ?, id_poslovalnice = ?, geslo = ?
                        WHERE id_zaposlenega = ?
             """

    cursor.execute(sql)
    rezultat = cursor.fetchone()

    povezava_na_bazo.close()         # zapre povezavo z bazo

    return rezultat

