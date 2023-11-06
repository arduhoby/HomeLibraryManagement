# kutuphane.py
import sqlite3
import pandas as pd
from datetime import datetime, time
import locale

def create_table():
    connection = sqlite3.connect("kutuphane.db")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS kitaplar (
            id INTEGER PRIMARY KEY,
            ad TEXT,
            yazar TEXT,
            yayin_evi TEXT,
            isbn TEXT,
            sayfa_sayisi INTEGER,
            dil INTEGER,
            okundu INTEGER,
            ekitap INTEGER,
            note TEXT,
            basimYili TEXT,
            etiket TEXT,
            raf TEXT
        )
    ''')

    connection.commit()
    connection.close()

def kitap_ekle(ad, yazar, yayin_evi, basimYili, isbn, sayfa_sayisi, dil, okundu, ekitap, note, etiket, raf):
    connection = sqlite3.connect("kutuphane.db")
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO kitaplar (ad, yazar, yayin_evi, basimYili, isbn, sayfa_sayisi, dil, okundu, ekitap, note, etiket, raf)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (ad, yazar, yayin_evi, basimYili, isbn, sayfa_sayisi, dil, okundu, ekitap, note, etiket, raf))


    connection.commit()
    connection.close()

def kitap_duzenle(ad, yazar, yayin_evi, basimYili, isbn, sayfa_sayisi, dil, okundu, ekitap, note, etiket, raf, id):
    connection = sqlite3.connect("kutuphane.db")
    cursor = connection.cursor()


    cursor.execute('''
        UPDATE kitaplar 
        SET ad=?, yazar=?, yayin_evi=?, basimYili=?, isbn=?, sayfa_sayisi=?, dil=?, okundu=?, ekitap=?, note=?, etiket=?, raf=?
        WHERE id=?
    ''', (ad, yazar, yayin_evi, basimYili, isbn, sayfa_sayisi, dil, okundu, ekitap, note, etiket, raf, id))

    connection.commit()
    connection.close()

def kitaplari_getir(sirala, limit):
    connection = sqlite3.connect("kutuphane.db")
    cursor = connection.cursor()

    # Sorgu oluşturma
    try:
        if sirala == "asc":
            sorgu = 'SELECT id, raf, ad, yazar, yayin_evi, basimYili,  sayfa_sayisi, dil, okundu, ekitap, note, etiket, isbn FROM kitaplar ORDER BY id ASC LIMIT ?'
        elif sirala == "desc":
            sorgu = 'SELECT id, raf, ad, yazar, yayin_evi, basimYili, sayfa_sayisi, dil, okundu, ekitap, note, etiket, isbn  FROM kitaplar ORDER BY id DESC LIMIT ?'
        else:
            raise ValueError("Geçersiz sıralama türü: 'asc' veya 'desc' kullanmalısınız.")

        cursor.execute(sorgu, (limit,))
        kitaplar = cursor.fetchall()
        connection.close()
        return kitaplar 
    except Exception as e:
        print(f'Hata: {e}')



def delete_kitap_from_db(ID):
    connection = sqlite3.connect("kutuphane.db")
    cursor = connection.cursor()
    cursor.execute('DELETE FROM kitaplar WHERE id = ?', (ID,))
    connection.commit()
    connection.close()

def doldur_form_from_db(ID):
    connection = sqlite3.connect("kutuphane.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM kitaplar WHERE id = ?', (ID,))
    formVeri = cursor.fetchall()
    connection.commit()
    connection.close()
    return formVeri

def kitap_ara(raf=None, isim=None, yazar=None, yayin_evi=None, dil=None, okundu=None, ekitap=None, note=None, etiket=None, isbn=None):
    connection = sqlite3.connect("kutuphane.db")
    cursor = connection.cursor()

    query = 'SELECT id, raf, ad, yazar, yayin_evi, basimYili, sayfa_sayisi, dil, okundu, ekitap, note, etiket, isbn FROM kitaplar WHERE 1=1 '
    parameters = []
    
    if raf:
        query += 'AND raf LIKE ? '
        parameters.append('%' + raf + '%') 

    if isim:
        query += 'AND ad LIKE ? '
        parameters.append('%' + isim + '%')

    if yazar:
        query += 'AND yazar LIKE ? '
        parameters.append('%' + yazar + '%')

    if yayin_evi:
        query += 'AND yayin_evi LIKE ? '
        parameters.append('%' + yayin_evi + '%')  

    if dil:
        query += 'AND dil = ? '
        parameters.append(1)
    
    if okundu:
        query += 'AND okundu = ? '
        parameters.append(1)
    
    if ekitap:
        query += 'AND ekitap = ? '
        parameters.append(1)

    if note:
        query += 'AND note LIKE ? '
        parameters.append('%' + note + '%') 

    if etiket:
        query += 'AND etiket LIKE ? '
        parameters.append('%' + etiket + '%') 

    if raf:
        query += 'AND raf LIKE ? '
        parameters.append('%' + raf + '%') 

    if isbn:
        query += 'AND isbn  LIKE ? '
        parameters.append(isbn)

    

    cursor.execute(query, tuple(parameters))
    kitaplar = cursor.fetchall()

    connection.close()

    return kitaplar

# SELECT COUNT(column_name) FROM table_name;
def kitap_sayisini_getir():
    connection = sqlite3.connect("kutuphane.db")
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(id) FROM kitaplar')
    kitapSayi = cursor.fetchall()
    connection.close()
    return kitapSayi[0]


locale.setlocale(locale.LC_ALL, '')

# Tarih bölümü


gun1 = datetime.strftime(datetime.now(), '%A')

tarihgun = datetime.strftime(datetime.now(), '%d')
tarihay = datetime.strftime(datetime.now(), '%m')
tarihyil = datetime.strftime(datetime.now(), '%Y')

saatH = datetime.strftime(datetime.now(), '%H')
saatD = datetime.strftime(datetime.now(), '%M')
saatS = datetime.strftime(datetime.now(), '%S')
saat = saatH+":"+saatD
fullsaat = saatH+saatD+saatS
fullzaman = tarihgun+"/"+tarihay+"/"+tarihyil+" - "+fullsaat
fullGunAyYil =tarihgun+"/"+tarihay+"/"+tarihyil
def excelAktar():
    # SQLite veritabanı bağlantısını oluşturun
    conn = sqlite3.connect('kutuphane.db')

    # SQL sorgusu ile verileri alın
    query = "SELECT * FROM kitaplar"  # 'tablo_adi' kısmını kendi tablonuzun adıyla değiştirin
    df = pd.read_sql_query(query, conn)

    # Excel dosyasına yazın
    excel_dosyası = tarihyil + tarihay+tarihgun + '_'+fullsaat +'_kitaplarVT'+'.xlsx'
    df.to_excel(excel_dosyası, index=False, engine='openpyxl')

    # Bağlantıyı kapatın
    conn.close()



    
# # Bu fonksiyon sayfa yapısı yapıldığında kullnaılacak 
# def load_data():
#     page_number = 1  # Sayfa numarasını buradan başlatın
#     rows_per_page = 12
#     offset = (page_number - 1) * rows_per_page
#     connection = sqlite3.connect("kutuphane.db")
#     cursor = connection.cursor()
#     cursor.execute(f"SELECT data FROM your_table LIMIT {rows_per_page} OFFSET {offset}")
#     kitaplar = cursor.fetchall()
#     return kitaplar

