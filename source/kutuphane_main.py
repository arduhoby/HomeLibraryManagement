# kutuphane_arayuz.py
import logging
import sys
import os
import zipfile
import shutil
import requests
from PySide6.QtWidgets import QMessageBox, QInputDialog
from isbn import getISBN, get_book_cover_url
from kutuphane import *
from paylas import send_email, send_whatsapp_message, encode_password, decode_password
from ui_anasayfa_tab import *
from barcode import *
import time


selected_kitap_id = None
app = QApplication([])
penAna = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(penAna)
tasks = [] # todo için
aranan_kitaplar=[]
arama_dizisi = ()
limit=12
siralama = "desc"
_raf=""
debugging=False


def kitap_kaydet():
    try:      
        if  ui.leKitapAdi.text() != "":
            ad = ui.leKitapAdi.text().title()
            # title() her kelimenin ilk harfini büyük yapar eğer cümlenin ilk harfi olacaksa capitalize() kullan
            yazar = ui.leYazar.text().title()
            yayin_evi = ui.leYayinEvi.text().title()
            basimYili= ui.leBasimYili.text()
            isbn= ui.leISBN.text()
            # sayfa_sayisi = int(ui.leSayfa.text())
            if ui.leSayfa.text() != "":
                sayfa_sayisi = int(ui.leSayfa.text())
            else:
                sayfa_sayisi = 0  # veya başka bir varsayılan değer
            dil=ui.cbTr.isChecked()
            okundu = ui.cbOkundu.isChecked()
            ekitap = ui.cbekitap.isChecked()
            note = ui.teNot.toPlainText()
            etiket = ui.teEtiket.toPlainText()
            raf = _raf
            if raf == "eKitap":
                ekitap=1
            else:
                ekitap=0
            kitap_ekle(ad, yazar, yayin_evi, basimYili, isbn, sayfa_sayisi, dil, okundu, ekitap, note, etiket, raf )
            guncelle_tabloyu_bos()
        else:
            show_message("Kitap adını Boş geçemezsiniz ! ")
     
    except Exception as e:
        if debugging == True:
            logging.error(fullzaman + f'Hata: {str(e)}')
        temizle()
        ui.teNot.setTextColor(QColor(255, 0, 0))
        show_uyari_message("Hatalı Giriş")
        ui.btGuncelle.setEnabled(False)
        ui.btKaydet.setEnabled(False)
        ui.btSil.setEnabled(False)
        ui.btClear.setEnabled(True)

def kitapGuncelle():
    global selected_kitap_id
    global arama_dizisi
    global aranan_kitaplar
    try:       
        if ui.leKitapAdi is not None and ui.leYazar is not None:
            id = selected_kitap_id
            ad = ui.leKitapAdi.text().title()
            yazar = ui.leYazar.text().title()
            yayin_evi = ui.leYayinEvi.text().title()
            basimYili= ui.leBasimYili.text()
            isbn= ui.leISBN.text()
            if ui.leSayfa.text() != "":
                sayfa_sayisi = int(ui.leSayfa.text())
            else:
                sayfa_sayisi = 0  # veya başka bir varsayılan değer
            dil=ui.cbTr.isChecked()
            okundu = ui.cbOkundu.isChecked()
            ekitap = ui.cbekitap.isChecked()
            note = ui.teNot.toPlainText()
            etiket = ui.teEtiket.toPlainText()
            raf = _raf
            kitap_duzenle(ad, yazar, yayin_evi, basimYili, isbn, sayfa_sayisi, dil, okundu, ekitap, note, etiket, raf, id)
            ui.tblKitap.clearSelection()
            if len(aranan_kitaplar)>0:
                isim, yazar, raf, yayinevi, isbn, dil, oku, ekitap, note, etiket=arama_dizisi
                aranan_kitaplar=kitap_ara(isim, yazar, raf, yayinevi, isbn, dil, oku, ekitap, note, etiket)
                guncelle_tabloyu(aranan_kitaplar)
            else:
                guncelle_tabloyu_bos()

                
    except Exception as e:
        if debugging == True:
            logging.error(fullzaman + f'Hata: {str(e)}')
        temizle()
        ui.teNot.setTextColor(QColor(255, 0, 0))
        show_uyari_message(e)
        ui.btGuncelle.setEnabled(False)
        ui.btKaydet.setEnabled(False)
        ui.btSil.setEnabled(False)
        ui.btClear.setEnabled(True)

def kitap_sil():
    try:
        if selected_kitap_id is not None:
            delete_kitap_from_db(selected_kitap_id)
            ui.tblKitap.clearSelection()
            guncelle_tabloyu_bos()
            temizle()
            ui.btKaydet.setEnabled(True)
            ui.btISBN.setEnabled(True)
    except Exception as e:
        if debugging == True:
            logging.error(fullzaman + f'Hata: {str(e)}')
        ui.teNot.setTextColor(QColor(255, 0, 0))
        ui.teNot.setText("Hatalı giriş !")

def kitap_ara_ve_guncelle():
    try:
        global aranan_kitaplar
        global arama_dizisi
        isim = ui.leKitapAdi.text().capitalize() # arama sırasında baş harfleri büyük harfe çevirir.
        yazar = ui.leYazar.text().capitalize()
        yayinevi= ui.leYayinEvi.text().capitalize()
        isbn= ui.leISBN.text()
        dil= ui.cbTr.isChecked()
        oku= ui.cbOkundu.isChecked()
        ekitap = ui.cbekitap.isChecked()
        note= ui.teNot.toPlainText()
        etiket = ui.teEtiket.toPlainText()
        raf=_raf
        aranan_kitaplar = kitap_ara(raf,isim, yazar, yayinevi,  dil, oku, ekitap, note, etiket, isbn)
        arama_dizisi=(raf, isim, yazar, yayinevi, dil, oku, ekitap, note, etiket, isbn)

        if not aranan_kitaplar:  # kitaplar listesi boş ise tabloyu temizleyelim
            temizle()
            show_message("Ama sonucu boş")
        else:
            guncelle_tabloyu(aranan_kitaplar)
            show_message("Ama sonucu "+str(ui.tblKitap.rowCount())+" kıtap bulundu.")
            ui.btGuncelle.setEnabled(False)
    except Exception as e:
        if debugging == True:
            logging.error(fullzaman + f'Hata: {str(e)}')

def tablo_satiri_secildi():
    global selected_kitap_id
    selected_items = ui.tblKitap.selectedItems()
    
    if not selected_items:
        return
    selected_row = selected_items[0].row()
    kitap_id = int(ui.tblKitap.item(selected_row,0).text())
    selected_kitap_id = kitap_id
    formHazirla()
    
    ui.btSil.setEnabled(True)
    ui.btClear.setEnabled(True)
    ui.btKaydet.setEnabled(False)
    ui.btGuncelle.setEnabled(True)
    ui.btAra.setEnabled(False)
    ui.teNot.setTextColor(QColor(255,255,255))
    ui.btISBN.setEnabled(False)

def guncelle_tabloyu(kitaplar):
    ui.tblKitap.clearContents()  # Tablonun içeriğini temizle
    ui.tblKitap.setRowCount(0)   # Tablonun satır sayısını sıfırla
    # isim, yazar, yayinevi, isbn, dil, oku, ekitap, note, etiket=arama_dizisi
    # aranan_kitaplar=kitap_ara(isim, yazar, yayinevi, isbn, dil, oku, ekitap, note, etiket)
    if not kitaplar:
        return  # Arama sonucu boş ise tabloyu güncelleme, çık
    tablo_to_guncelle(kitaplar)
        
def guncelle_tabloyu_bos():
    global limit
    global siralama
    global aranan_kitaplar
    limit=int(ui.leGetSatir.text())
    if ui.cbSiralama.isChecked():
        siralama ="desc"
    else:
        siralama = "asc"
    
    if limit > 0:
        aranan_kitaplar=[]
        kitaplar = kitaplari_getir(siralama, limit)
        tablo_to_guncelle(kitaplar)
    else:
        limit = 12
        kitaplar = kitaplari_getir(limit)
        tablo_to_guncelle(kitaplar)



def checkbox_changed_state(state):
    if state == 2:  # Seçili durum
        ui.cbSiralama.setText("Son")
        ui.leGetSatir.setText("12")
    else:
        ui.cbSiralama.setText("Baş")
        ui.leGetSatir.setText("12")

def tabloGetir():
    ui.tblKitap.setColumnCount(13)
    ui.tblKitap.setHorizontalHeaderLabels(
            ["ID", "Raf","Ad", "Yazar", "Yayın Evi", "Basım Yılı", "Sayfa", "Oku",
             "Dil", "ekitap","not", "etiket",  "ISBN"])
    #ui.tblKitap.horizontalHeader().setMinimumSectionSize(15) # min 15 width
    ui.tblKitap.horizontalHeader().setMaximumSectionSize(150) # max 150 width
    ui.tblKitap.horizontalHeader().setSectionResizeMode(10, QHeaderView.ResizeMode.Stretch)
    ui.tblKitap.setColumnWidth(0, 40)
    ui.tblKitap.setColumnWidth(1, 120)
    ui.tblKitap.setColumnWidth(2, 120)
    ui.tblKitap.setColumnWidth(3, 30)
    ui.tblKitap.setColumnWidth(4, 20)
    ui.tblKitap.setColumnWidth(5, 120)

    ui.tblKitap.horizontalHeader().hideSection(0) # sütun gizlemek için
    ui.tblKitap.horizontalHeader().hideSection(5)
    ui.tblKitap.horizontalHeader().hideSection(6)
    ui.tblKitap.horizontalHeader().hideSection(7)
    ui.tblKitap.horizontalHeader().hideSection(8)
    ui.tblKitap.horizontalHeader().hideSection(9)
    ui.tblKitap.horizontalHeader().hideSection(12)
    # tabloHaz()
    ui.tblKitap.itemSelectionChanged.connect(tablo_satiri_secildi)

def tablo_to_guncelle(kitaplar):
    try:
        ui.tblKitap.setRowCount(len(kitaplar))
        for row_index, (id, raf, ad, yazar, yayin_evi, basimYili, sayfa_sayisi, dil, okundu, ekitap, note,
                        etiket, isbn) in enumerate(kitaplar):
            ui.tblKitap.setItem(row_index, 0, QTableWidgetItem(str(id)))
            ui.tblKitap.setItem(row_index, 1, QTableWidgetItem(raf))
            ui.tblKitap.setItem(row_index, 2, QTableWidgetItem(ad))
            ui.tblKitap.setItem(row_index, 3, QTableWidgetItem(yazar))
            ui.tblKitap.setItem(row_index, 4, QTableWidgetItem(yayin_evi))
            ui.tblKitap.setItem(row_index, 5, QTableWidgetItem(basimYili))
            ui.tblKitap.setItem(row_index, 6, QTableWidgetItem(str(sayfa_sayisi)))
            ui.tblKitap.setItem(row_index, 7, QTableWidgetItem("Tr" if dil else "En"))
            ui.tblKitap.setItem(row_index, 8, QTableWidgetItem("X" if okundu else "-"))
            ui.tblKitap.setItem(row_index, 9, QTableWidgetItem("X" if ekitap else "-"))
            ui.tblKitap.setItem(row_index, 10, QTableWidgetItem(note)) 
            ui.tblKitap.setItem(row_index, 11, QTableWidgetItem(etiket))
            ui.tblKitap.setItem(row_index, 12, QTableWidgetItem(isbn))

            ui.lbRowCount_2.setText("Tabloda "+str(ui.tblKitap.rowCount())+".")
            
            temizle()
            ui.btKaydet.setEnabled(True)
    except Exception as e:
        if debugging == True:
            logging.error(fullzaman + f'Hata: {str(e)}')

def formHazirla():
    temizle()
    global selected_kitap_id
    try:
        if selected_kitap_id is not None:
            liste=doldur_form_from_db(selected_kitap_id) 
            ui.leKitapAdi.setText(liste[0][1])
            ui.leYazar.setText(liste[0][2])
            ui.leYayinEvi.setText(liste[0][3])
            ui.leISBN.setText(liste[0][4])
            ui.leSayfa.setText(str(liste[0][5]))
            if liste[0][6]>0:
                ui.cbTr.setChecked(True)
            else :
                ui.cbTr.setChecked(False)
            if liste[0][7]>0:
                ui.cbOkundu.setChecked(True)
            else :
                ui.cbekitap.setChecked(False)
            if liste[0][8]>0:
                ui.cbekitap.setChecked(True)
            else :
                ui.cbekitap.setChecked(False)

            ui.teNot.setText(liste[0][9])
            ui.leBasimYili.setText(liste[0][10])
            ui.teEtiket.setText(liste[0][11])
            
            url = get_book_cover_url(str(liste[0][4]))
            if url == "bos":
                url="https://image.freepik.com/free-vector/books-stack-realistic_1284-4735.jpg"
            ui.cboxRaf.setCurrentText(liste[0][12])
            load_image(url)
            ui.btClear.setEnabled(True)
    except Exception as e:
        if debugging == True:
            logging.error(fullzaman + f'Hata: {str(e)}')
        return

def temizle():
    global _raf
    ui.teNot.setTextColor(QColor(255,255,255))
    ui.tblKitap.resizeColumnsToContents()
    ui.leKitapAdi.setText("")
    ui.leYazar.setText("")
    ui.leYayinEvi.setText("")
    ui.leBasimYili.setText("")
    ui.leISBN.setText("")
    ui.leSayfa.setText("0")
    ui.cbTr.setChecked(False)
    ui.cbOkundu.setChecked(False)
    ui.cbekitap.setChecked(False)
    ui.teNot.setText("")
    ui.teEtiket.setText("")
    ui.btClear.setEnabled(False)
    ui.btSil.setEnabled(False)
    ui.btKaydet.setEnabled(True)
    ui.btAra.setEnabled(True)
    ui.btISBN.setEnabled(True)
    ui.cboxRaf.setCurrentIndex(0)
    ui.lbImg.clear()
    _raf=""
    get_kutuphane_img()
    ui.lbRowCount.setText("Top.Kitap : " +str(kitap_sayisini_getir()[0]))
    ui.tblKitap.clearSelection()

def isbnGetir(isbn):
    try:    
        if ui.leISBN is not None:
            isbn=ui.leISBN.text()
            book_info = getISBN(isbn)
            if 'error' in book_info:
                hata=f"Hata: {book_info['error']}"
                show_message(hata)
                ui.btClear.setEnabled(True)
            else:
                temizle()
                ui.leKitapAdi.setText(f"{book_info['title']}")
                ui.leYazar.setText(f"{', '.join(book_info['authors'])}")
                ui.leYayinEvi.setText(f"{book_info['publisher']}")
                ui.leBasimYili.setText(f"{book_info['publication_date']}")
                ui.leSayfa.setText(f"{book_info['page_count']}")
                ui.leISBN.setText(isbn)
                ui.btGuncelle.setEnabled(False)
                ui.btClear.setEnabled(True)
                # print(f"{book_info['language']}")
                if (f"{book_info['language']}")=="tr":
                    ui.cbTr.setChecked(True)
                else :
                    ui.cbTr.setChecked(False)
                ui.teNot.setText(f"{book_info['description']}")
                
                load_image(get_book_cover_url(isbn))
    except Exception as e:
        if debugging == True:
            logging.error(fullzaman + f'Hata: {str(e)}')
        if ui.leKitapAdi.text() !="" and ui.leYazar.text() !="":
            return
        else:
            show_message("ISBN Hatalı")

def show_message(mesaj):
    # Mesaj kutusu nesnesi oluşturun
    msg = QMessageBox()

    # Mesaj kutusunun başlığını, metnini ve simgesini ayarlayın
    msg.setWindowTitle("Sorun Mesaj Kutusu")
    msg.setText(mesaj)
    msg.setIcon(QMessageBox.Information)

    # Mesaj kutusunu gösterin
    msg.exec()

def load_image(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            image_data = response.content
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            ui.lbImg.setPixmap(pixmap)
            ui.lbImg.setScaledContents(True)
        else:
            ui.lbImg.clear()
            show_message("URL Hatalı")
    except Exception as e:
        if debugging == True:
            logging.error(fullzaman + f'Hata: {str(e)}')

def get_kutuphane_img():
    pixmap = QPixmap('img/kutuphane.png')
    # QLabel'in pixmap özelliğini ayarla
    ui.lbImg.setPixmap(pixmap)
    # Pencereyi resim boyutuna göre yeniden boyutlandır
    # ui.lbImg.resize(pixmap.width(), pixmap.height())
    ui.lbImg.setScaledContents(True)

def emailGonder():
    if ui.leKitapAdi.text() == "":
        show_message("Kitap ismi yok\nOlmadan göndermenin bir anlamı yok")
        return
    else:
        isim = ui.leKitapAdi.text()
    
    if ui.leYazar.text() != "":
        yazar = ui.leYazar.text()
    else:
        yazar = "Bilinmiyor"
    
    if ui.leISBN.text() != "":
        ISBN = ui.leISBN.text()
        link = "https://isbnsearch.org/isbn/" + ISBN
    else:
        ISBN = "Bilinmiyor"
        link = "Bilinmiyor"
    
    message = f"Kitap Önerisi:\nİsim: {isim}\nYazar: {yazar}\nISBN: {ISBN}\nLink: {link}"
    emailinfo = ui.leSetupEmailAdresi.text()
    passwordinfo = decode_password(ui.leSetupEmailPassword.text())
    email, ok = QInputDialog.getText(ui.centralwidget, 'E-posta Adresi', 'E-posta adresinizi girin:')
    
    if ok:
        send_email(emailinfo, passwordinfo, "Kitap Önerisi", message, email)
        show_uyari_message("Mail Gönderiliyor")

def show_uyari_message(message):
    QMessageBox.warning(ui.centralwidget, 'Uyarı', message)

def wahsappGonder():
    if ui.leKitapAdi.text() == "":
        show_message("Kitap ismi yok\nOlamadan göndermenin bir anlamı yok")
        return
    else:
        isim = ui.leKitapAdi.text()
    
    if ui.leYazar.text() != "":
        yazar = ui.leYazar.text()
    else:
        yazar = "Bilinmiyor"
    
    if ui.leISBN.text() != "":
        ISBN = ui.leISBN.text()
        link = "https://isbnsearch.org/isbn/" + ISBN
    else:
        ISBN = "Bilinmiyor"
        link = "Bilinmiyor"
    message = f"Kitap Önerisi:\nİsim: {isim}\nYazar: {yazar}\nISBN: {ISBN}\nLink: {link}"

    message_hours = datetime.now().hour #   Gönderim saati (24 saat formatında)
    message_minutes = datetime.now().minute   # Gönderim dakikası

    telefon, ok = QInputDialog.getText(ui.centralwidget, 'Telefon', 'Telefon No örnek 532xxxxxxx girin:')
    telefon="+90"+telefon
    if ok:
        send_whatsapp_message(telefon, message, message_hours, message_minutes)
        show_uyari_message("Mesaj Gönderilecek")

def toggle_frame_visibility(frame):
    if frame.isVisible():
        frame.setVisible(False)
    else:
        frame.setVisible(True)

def combobox_changed(cBoxSecim):
    try:        
        global _raf
        # Seçilen öğenin değeri "text" parametresi olarak bu fonksiyona iletilir
        _raf =cBoxSecim
    except Exception as e:
        if debugging == True:
            logging.error(fullzaman + f'Hata: {str(e)}')
def barcode_getir():
    show_message("Netleştiğinde lütfen \n   S   \n tuşuna basın ")
    barcodeYakala()
    time.sleep(5)
    ui.leISBN.setText(barcodeOku())

def comboBoxDoldur():
    try:
        ui.cboxRaf.clear()
        with open("setup/veriler.txt", "r") as file:
            for line in file:
                item = line.strip()  # Her satırın sonundaki boşlukları kaldırın
                ui.cboxRaf.addItem(item)  # ComboBox'a öğeyi ekleyin
    except FileNotFoundError:
        # Dosya bulunamadıysa, yeni bir dosya oluşturun ve "Item : A - 1" satırını ekleyin
        with open("setup/veriler.txt", "w") as file:
            file.write("RAF \nA - 1\nA - 2\nA - 3\nA - 4\nA - 5\nA - 6\nB - 1\nB - 2\nB - 3\nB - 4\nB - 5\nHHouse\neKitap\n")

def paylasBt():
    if ui.btPaylas.text() == "Paylaş  >":
        ui.btPaylas.setText("Paylaş  <")
    else:
        ui.btPaylas.setText("Paylaş  >")

    toggle_frame_visibility(ui.frmPaylas)

#setup_tab_raf listview sistemi
def setup_listViewDoldur():
    try:
        # Dosyadan verileri okuyup ListView'e ekle
        if os.path.exists('setup/veriler.txt'):
            with open("setup/veriler.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    ui.lvRafDuzenle.addItem(line.strip())  # Satır sonundaki boşlukları temizler
    except Exception as e:
        if debugging == True:
            logging.error(fullzaman + f'Hata: {str(e)}')

    ui.lvRafDuzenle.itemClicked.connect(setup_on_item_clicked)

def setup_on_item_clicked(item):
    try:
        selected_text = item.text()
        ui.leRafekle.setText(selected_text)
    except Exception as e:
        if debugging == True:
            logging.error(fullzaman + f'Hata: {str(e)}')

def setup_remove_selected_item():
    try:
        selected_item = ui.lvRafDuzenle.currentItem()
        if selected_item:
            ui.lvRafDuzenle.takeItem(ui.lvRafDuzenle.row(selected_item))
            ui.leRafekle.clear()
        setup_save_to_file()
        comboBoxDoldur()
    except Exception as e:
        if debugging == True:
            logging.error(fullzaman + f'Hata: {str(e)}')

def setup_save_to_file():
    try:
        with open("setup/veriler.txt", "w") as file:
            for row in range(ui.lvRafDuzenle.count()):
                item = ui.lvRafDuzenle.item(row)
                text = item.text()
                file.write(text + "\n")
    except Exception as e:
        if debugging == True:
            logging.error(fullzaman + f'Hata: {str(e)}')

def setup_add_line():
    new_line = ui.leRafekle.text()
    if new_line:
        ui.lvRafDuzenle.addItem(new_line)
        ui.leRafekle.clear()
    setup_save_to_file()
    comboBoxDoldur()

def setup_rafSetupFrmGosterKapa():
    if ui.frRafSetup.isVisible():
        ui.frRafSetup.setVisible(False)
    else:
        ui.frRafSetup.setVisible(True)

def setup_vt_yedekle_ve_kopyala():
    try:
        # Dosyayı yedek dizinine kopyala
        shutil.copy("kutuphane.db", "backup/kutuphane.bak")

        show_message(f"kutuphane.db dosyası backup/kutuphane.bakdizinine başarıyla kopyalandı.")
    except FileNotFoundError:
        if debugging == True:
            logging.error(f"kutuphane.db dosyası bulunamadı.")
    except Exception as e:
        if debugging == True:
            logging.error(fullzaman + f'Hata: {str(e)}')

def setup_vt_geri_yukle():
    try:
        # Yedek dosyayı hedef dosya olarak taşı
        shutil.move("backup/kutuphane.bak", "kutuphane.db")
        show_message(f"veritabanı başarıyla restore edildi.")
    except FileNotFoundError:
        if debugging == True:
            logging.error(f"kutuphane.bak dosyası bulunamadı.")
    except Exception as e:
        if debugging == True:
            logging.error(fullzaman + f'Hata: {str(e)}')

def setup_vt_ziple():
    file_name = "kutuphane.db"
    # zip dosyasının adını ve modunu belirle
    zip_name = "backup/kutuphane.zip"
    zip_mode = "w"
    # zip dosyasını oluştur ve aç
    with zipfile.ZipFile(zip_name, zip_mode) as zip_file:
        # sıkıştırılacak dosyayı zip dosyasına ekle
        zip_file.write(file_name)
        # zip dosyasını kapat
        zip_file.close()

def setup_email_ac_kapa():
    if ui.frSetupEmailBilgi.isVisible():
        ui.frSetupEmailBilgi.setVisible(False)
    else:
        ui.frSetupEmailBilgi.setVisible(True)

def setup_email_password_encode():
    enc_pass = encode_password(ui.leSetupEmailPassword.text())
    ui.leSetupEmailPassword.setText(enc_pass)
    setup_save_mail_info()
    ui.btEmailEncode.setEnabled(False)

def setup_save_mail_info():
    email_info=ui.leSetupEmailAdresi.text()
    password_info=ui.leSetupEmailPassword.text()
    with open('setup/email.txt', 'w') as file:
        file.write(f'{email_info},{password_info}')

def setup_mail_info_Doldur():
    try:
        with open('setup/email.txt', 'r') as file:
            email_password = file.read().strip().split(',')
            if len(email_password) == 2:
                email_info = email_password[0]
                password_info = email_password[1]
                ui.leSetupEmailAdresi.setText(email_info)
                ui.leSetupEmailPassword.setText(password_info)
            if ui.leSetupEmailPassword.text()!="":
                ui.btEmailEncode.setEnabled(False)
            else:
                ui.btEmailEncode.setEnabled(True)

    except FileNotFoundError:
        # Eğer dosya bulunamazsa veya okuma sırasında hata olursa işlem hatasız devam etmesi için bir hata mesajı görüntülemek isteyebilirsiniz.
        show_message("Email dosyası bulunamadı veya okunurken bir hata oluştu.")
    except Exception as e:
        if debugging == True:
            logging.error(fullzaman + f'Hata: {str(e)}')
def setup_email_info_sil():
    ui.leSetupEmailPassword.clear()
    ui.leSetupEmailAdresi.clear()
    ui.btEmailEncode.setEnabled(True)
    setup_save_mail_info()




#Planlama todo uygulaması için
def todo_tablo_hazirla():
    ui.lvTodo.setColumnCount(3)
    ui.lvTodo.setHorizontalHeaderLabels(['Tarih', 'Yapılacaklar', 'Durum'])
    ui.lvTodo.setColumnWidth(0,70)
    ui.lvTodo.setColumnWidth(1,415)
    ui.lvTodo.setColumnWidth(2,310)

def todo_save_tasks():
    global tasks
    with open('setup/todo.txt', 'w') as file:
        for tarih, task, done in tasks:
            file.write(f'{tarih},{task},{done}\n')

def todo_load_tasks(): #başlangıç için
    if os.path.exists('setup/todo.txt'):
        with open('setup/todo.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                date, task, done = line.strip().split(',', 2)
                tasks.append((date, task, done))
                row_position = ui.lvTodo.rowCount()
                ui.lvTodo.insertRow(row_position)
                ui.lvTodo.setItem(row_position, 0, QTableWidgetItem(date))
                ui.lvTodo.setItem(row_position, 1, QTableWidgetItem(task))
                ui.lvTodo.setItem(row_position, 2, QTableWidgetItem(done))
                ui.lvTodo.setFont(QFont("Arial", 8))

def todo_add_task():
    global tasks
    task = ui.leTodoSatir.text()
    if task:
        date=fullGunAyYil
        durum=""
        tasks.append((date, task, durum))
        row_position = ui.lvTodo.rowCount()
        ui.lvTodo.insertRow(row_position)
        ui.lvTodo.setItem(row_position, 0, QTableWidgetItem(date))
        ui.lvTodo.setItem(row_position, 1, QTableWidgetItem(task))
        ui.lvTodo.setItem(row_position, 2, QTableWidgetItem(''))
        todo_save_tasks()
        ui.leTodoSatir.clear()
    else:
        QMessageBox.warning( 'Boş Görev', 'Lütfen bir görev girin.')

def todo_delete_task(self):
    global tasks
    selected_row = ui.lvTodo.currentRow()
    if selected_row >= 0:
        ui.lvTodo.removeRow(selected_row)
        del tasks[selected_row]
    todo_save_tasks()

def todo_task_state_changed(item):
    # "Durum" değiştiğinde çalışır
    if item.column() == 2:
        row = item.row()
        status_text = item.text()  # Durum metinini al
        tasks[row] = (tasks[row][0], tasks[row][1], status_text)
        todo_save_tasks()  # Durum değiştiğinde dosyaya kaydet

def todo_get_selected_task():
    selected_row = ui.lvTodo.currentRow()
    if selected_row >= 0:
        return tasks[selected_row]
    else:
        return None
def todo_email_gonder():
    subject = fullzaman
    tarih1, mesajana, durum= todo_get_selected_task()
    mesaj = tarih1+ " \n "+mesajana + " \n "+durum
    emailinfo=ui.leSetupEmailAdresi.text()
    passwordinfo=decode_password(ui.leSetupEmailPassword.text())
    email, ok = QInputDialog.getText(ui.centralwidget, 'E-posta Adresi', 'E-posta adresinizi girin:')

    if ok:
        send_email(emailinfo, passwordinfo,subject, mesaj, email)
        show_uyari_message("Mail Gönderiliyor")



# signal_slots
ui.btKaydet.clicked.connect(kitap_kaydet)
ui.btSil.clicked.connect(kitap_sil)
ui.tblKitap.itemSelectionChanged.connect(tablo_satiri_secildi)
ui.btGuncelle.clicked.connect(kitapGuncelle)
ui.btClear.clicked.connect(temizle)
ui.btAra.clicked.connect(kitap_ara_ve_guncelle) 
ui.btISBN.clicked.connect(isbnGetir)
ui.btExcel.clicked.connect(excelAktar)
ui.btSon.clicked.connect(guncelle_tabloyu_bos)
ui.btEmail.clicked.connect(emailGonder)
ui.btWhatsap.clicked.connect(wahsappGonder)
ui.cbSiralama.stateChanged.connect(checkbox_changed_state)
#ui.btPaylas.clicked.connect(lambda: toggle_frame_visibility(ui.frmPaylas))
ui.btPaylas.clicked.connect(paylasBt)
ui.cboxRaf.currentTextChanged.connect(combobox_changed)
ui.btBarcode.clicked.connect(barcode_getir)
ui.btRafEkle.clicked.connect(setup_add_line)
ui.btSecRafSil.clicked.connect(setup_remove_selected_item)
ui.btTodoEkle.clicked.connect(todo_add_task)
ui.btTodoSil.clicked.connect(todo_delete_task)
# ui.leKitapAdi.textChanged.connect(lineedit_text_changed)
# ui.btKaydet.setStyleSheet(open("stil2.qss", "r").read())
ui.lvTodo.itemChanged.connect(todo_task_state_changed)  # todo Hücre değişikliği algılandığında işlem yap
ui.btRafSetupAc.clicked.connect(setup_rafSetupFrmGosterKapa)
ui.btVeritabaniYedekle.clicked.connect(setup_vt_yedekle_ve_kopyala)
ui.btVeritabaniRestore.clicked.connect(setup_vt_geri_yukle)
ui.btVeritabaniZiple.clicked.connect(setup_vt_ziple)
ui.btTodoEmailGonder.clicked.connect(todo_email_gonder)
ui.btEmailEncode.clicked.connect(setup_email_password_encode)
ui.btSetupEmailAyar.clicked.connect(setup_email_ac_kapa)
ui.lvRafDuzenle.itemClicked.connect(setup_on_item_clicked)
ui.btSetupEmailAyarSil.clicked.connect(setup_email_info_sil)


def baslangicta_calisaak_komutlar():
    global limit
    todo_tablo_hazirla()
    setup_listViewDoldur()
    ui.frRafSetup.setVisible(False)
    ui.frSetupEmailBilgi.setVisible(False)
    comboBoxDoldur()
    todo_load_tasks()
    setup_mail_info_Doldur()
    create_table()
    tabloGetir()
    ui.frmPaylas.hide()
    kitaplar = kitaplari_getir(siralama, limit)
    guncelle_tabloyu(kitaplar)  # kitaplar listesini guncelle_tabloyu'na argüman olarak veriyoruz
    ui.btAra.setToolTip("Boş form ile ara butonunu kullanırsanız \n bütün kitapları getirir.")
    ui.btExcel.setToolTip("Bütün kitapları \n Excel dosyası olarak kaydeder.")
    ui.cbSiralama.setText("Son")
    ui.btGuncelle.setEnabled(False)
    ui.cbekitap.setVisible(False)

def main():
    baslangicta_calisaak_komutlar()
    penAna.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()