from pymongo import MongoClient

host ="localhost"
port = 27017
db="personeller"
connection = MongoClient(host,port)

db=connection[db]
print("Veritabanı bağlantısı başarılı")


collection = db['personeller']

#Listeleme
def menu():
    print("""
                  MENU
          ------------------
          1-Listele
          2-Ekle
          3-Ara
          4-Sil
          5-Güncelle
          6-Çikis
          
          -------------------
          """)

def listele():
    print("Personeller listeleniyor...")
    #find arama yapar
    sonuc=collection.find() 
    for item in sonuc:
        print(item["ad"],item["soyad"],item["personelNo"])

def ekle():
    personelNo= int(input("Personel No: "))
    ad = input("Ad: ")
    soyad = input("Soyad: ")
    #ekleme yapıyoruz
    kayit=collection.insert_one({"personelNo":personelNo,"ad":ad,"soyad":soyad})
    listele()

def ara():
    no =int(input("Aranacak personel no: "))
    sonuc=collection.find({"personelNo":no})
    for item in sonuc:
        print(item["personelNo"],item["soyad"],item["ad"])

def sil():
    no =int(input("Silinecek personel no: "))
    collection.delete_one({"personelNo":no})
    listele()
menu()
def guncelle():
    no =int(input("Güncellenecek personel no: "))
    ad = input("Ad: ")
    soyad = input("Soyad: ")
    collection.update_one({"personelNo":no},{"$set":{"ad":ad,"soyad":soyad}})
    listele()

while True:
    secim = input("Seçiminiz: ")
    if secim=="1":
        listele()
        continue
    elif secim=="2":
        ekle()
        continue
    elif secim=="3":
        ara()
        continue
    elif secim=="4":
        sil()
        continue
    elif secim=="5":
        guncelle()
        continue
    elif secim=="6":
        print("Çıkış yapılıyor...")
        break  
