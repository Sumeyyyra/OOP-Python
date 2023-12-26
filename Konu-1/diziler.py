#diziler

ogrenciler =["volkan","ayse","sumeyra","volkan"]
#   index      0        1       2         4

print("Bu github'in sahibi "+ ogrenciler[2])

#ayseyi sil
ogrenciler.remove("ayse")
print(ogrenciler)

#volkan kaç tane say
print(ogrenciler.count("volkan"))

#istediğim indexe ekle
ogrenciler.insert(0,"mete")
print(ogrenciler)

#0. indexi silme
ogrenciler.pop(0)
print(ogrenciler)

#ogrenciler2ye 1'i kopyalar
ogrenciler2=ogrenciler.copy()
print(ogrenciler2)

#diziyi ekleme
ogrenciler2.extend(ogrenciler)
print(ogrenciler2)