from flask import Flask,render_template

#name değişkenine sahipse app çalışır
app=Flask(__name__)

@app.route("/")
def index():
	urunler=[
	{"id":"1","urun":"saat","fiyat":"1850 tl"},
	{"id":"2","urun":"Pc","fiyat":"18050 tl"},
	]
	return render_template("index.html",urunler=urunler)

#sayfalar arası geçiş gibi 
@app.route("/listele")

def listeleme():
	sayi=5
	return render_template("ogrenciler.html",sayim=sayi)

@app.route("/sum")

def sum():
	return render_template("sablon.html")

@app.route("/satinal/<string:id>")

def satinal(id):
	return "gelen id:" + id

app.run(debug=True)

