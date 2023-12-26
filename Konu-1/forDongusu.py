#for dongusu geneldee sayıs belli olan döngülerde
#while dongusu genelde sonu belli olmayan dongulerde

# liste=["vlkan","ayse","sumeyra"]
# for item in liste:
#     print(item)

#0 dan 20 ye kadar sayları listeye atar
liste=list(range(20))
print(liste)
toplam=0

#sayaç mantığı
for item in liste:
    toplam+=item

print(toplam)
