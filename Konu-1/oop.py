#nesen tabanlı programlama

class Insan:
    def __init__(self,ad,soyad,yas):
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
#artık bir nesne tanımladık
        
personel=Insan("ahmet","usta",45)
print(personel.ad)
        
#insandan miras aldık
class Ogrenci(Insan):
    def __init__(self,id):
        self.id=id

class Ogretmen(Insan):
    def __init__(self,ogretmenId):
        self.ogretmenId=ogretmenId

ali=Ogrenci(23)
ali.ad="ali"
ali.soyad="usta"
ali.yas=4
print(ali.ad)      
