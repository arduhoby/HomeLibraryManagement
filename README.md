# HomeLibraryManagement

Ev Kütüphanesinin yönetimi için oluşturuldu.

ana ppp = kutuphane_main.py

kullanılan Pypi kütüphaneleri:
pyside6, logging, sys, os, zipfile, shutil, requests, 
opencv-python (barcode  okumak için), zxingcpp (barcode için )
sqlite3, pandas, locale
smtplib, pywhatkit ( whatsapp mesajı için ),base64



setup içindeki email adresini ve şifresini düzelttikten sonra emal atar 

whatsapp için uygulamanın web de çalışabilir olması gerekli ve whatsapp.py dosyası içine kendi telefon numaranızı girmeniz gerekli 

raf düzeninizi kendinize göre setup sekmesinden ayarlayabilirsiniz 

program çalıştıktan sonra kutuphane.db dosyası oluşacaktır. 

bu app evde şahsi bilgisayarda kullanılacağı için güvenlik endişesi duyulmamaktadır. 

dbkolonekleme.py    veri tabaına yeni kolon eklemek gerektiğinde kullaıldı. Gereksiz ama tool olarak bıraktım. 

ben surface pro kullanıyorum 2 kamerası var arka kamera ile barcode okuma yapılabiliyor, etknik olarak laptop ön kameraları da bu işe yarasa da konumlandırma zor ama bir eklenti kullanmak isterseniz 0 ve 1 seçerek kendi kameranızı ayarlayabilirsiniz. 
