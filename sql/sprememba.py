import sqlite3


pot_glavne_mape = pot_do_mape()                

povezava_na_bazo = sqlite3.connect(f"{pot_glavne_mape}/baza/baza.db")      # ustvari povezavo z bazo
kazalec = povezava_na_bazo.cursor()                                        # stvari kazalec za izvajanje SQL poizvedb



def preveri_vnos(vnesen_id_zaposlenega):
    '''preveri, ali je uporabnik vnesel takšno uporabniško številko, ki v bazi podatkov že obstaja'''

    sql =   f""" SELECT * FROM zaposleni 
                    WHERE id_zaposlenega = {vnesen_id_zaposlenega}
             """

    kazalec.execute(sql)
    rezultat = kazalec.fetchone()

    return rezultat



def dodaj_sodelavca(vseneno_ime, vnesen_priimek, vnesen_spol, vneseno_delovno_mesto, vnesen_id_poslovalnica, vnesen_id_zaposlenega, vneseno_geslo):
    '''dodaj novega sodelavca v bazo podatkov'''

    sql =   f""" INSERT INTO zaposleni (ime, priimek, spol, delovno_mesto, id_poslovalnice, id_zaposlenega, geslo)
                    VALUES ({vseneno_ime}, {vnesen_priimek}, {vnesen_spol}, {vneseno_delovno_mesto}, {vnesen_id_poslovalnica}, {vnesen_id_zaposlenega}, {vneseno_geslo})
             """

    kazalec.execute(sql)
    rezultat = kazalec.fetchone()

    return rezultat



def odstrani_sodelavca(vnesen_id_zaposlenega):
    '''odstrani sodelavca iz baze podatkov'''
    sql =   f""" DELETE FROM zaposleni 
                    WHERE id_zaposlenega = {vnesen_id_zaposlenega}
             """

    kazalec.execute(sql)
    rezultat = kazalec.fetchone()

    return rezultat



def spremeni_podatke_sodelavca(vseneno_ime, vnesen_priimek, vnesen_spol, vneseno_delovno_mesto, vnesen_id_poslovalnica, vnesen_id_zaposlenega, vneseno_geslo):
    '''spremeni podatke o sodelavcu v bazi podatkov'''

    sql =   f""" UPDATE zaposleni 
                    SET ime = {vseneno_ime}, priimek = {vnesen_priimek}, spol = {vnesen_spol}, delovno_mesto = {vneseno_delovno_mesto}, id_poslovalnice = {vnesen_id_poslovalnica}, geslo = {vneseno_geslo}
                        WHERE id_zaposlenega = {vnesen_id_zaposlenega}
             """

    kazalec.execute(sql)
    rezultat = kazalec.fetchone()

    return rezultat


povezava_na_bazo.close()         # zapre povezavo z bazo