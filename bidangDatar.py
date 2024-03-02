def luasSegitiga(alas,tinggi):
    return alas * tinggi / 2
def luasPersegi(sisi):
    return sisi * sisi
def luasPersegiPanjang(panjang,lebar):
    return panjang * lebar
def luasJajarGenjang(alas,tinggi):
    return alas * tinggi
def luasTrapesium(alasAtas,alasBawah,tinggi):
    alasTrapesium = alasAtas + alasBawah
    return alasTrapesium * tinggi / 2

def luasBelahKetupat(diameterPertama,diameterKedua):
    return diameterPertama * diameterKedua / 2

def luasLayangLayang(diameterPertama,diameterKedua):
    return diameterPertama * diameterKedua / 2

def luasLingkaran(jariJari):
    phi = 22 / 7
    return phi * jariJari ** 2

pilihan = str(input("Masukan nama bangun datar yang ingin di kalkulasikan = "))

if pilihan.lower() == "segitiga":
    x = int(input("Masukkan alas Segita = "))
    z = int(input("Masukkan tinggi Segita = "))
    print(str(luasSegitiga(x, z)) + " m2")

elif pilihan.lower() == "persegi":
    x = int(input("Masukan panjang sisi persegi = "))
    print(str(luasPersegi(x)) + " m2")

elif pilihan.lower().replace("persegi ", "persegi") == "persegipanjang":
    x = int(input("Masukan panjang persegi panjang = "))
    z = int(input("Masukan lebar persegi panjang = "))
    print(str(luasPersegiPanjang(x,z)) + " m2")

elif pilihan.lower().replace("jajar ", "jajar") == "jajargenjang":
    x = int(input("Masukan alas jajar genjang = "))
    z = int(input("Masukan tinggi jajar genjang = "))
    print(str(luasJajarGenjang(x,z)) + " m2")

elif pilihan.lower() == "trapesium" :
    x = int(input("Masukan alas atas trapesium = "))
    y = int(input("Masukan alas bawah trapesium = "))
    z = int(input("Masukan tinggi trapesium = "))
    print(str(luasTrapesium(x,y,z)) + " m2")

elif pilihan.lower().replace("belah ", "belah") == "belahketupat":
    x = int(input("Masukan diameter pertama = "))
    z = int(input("Masukan diameter kedua = "))
    print(str(luasBelahKetupat(x,z)) + " m2")

elif pilihan.lower().replace("layang ", "layang") == "layanglayang":
    x = int(input("Masukan diameter pertama = "))
    z = int(input("Masukan diameter kedua = "))
    print(str(luasLayangLayang(x,z)) + " m2")

elif pilihan.lower() == "lingkaran":
    x = int(input("Masukan jari jari lingkaran = "))
    print(str(luasLingkaran(x)) + " m2")

else :
    print("Maaf pilihan kamu tidak masuk ke dalam bangun ruang ini, jika kamu yakin pilihan kamu termasuk bangun ruang periksa kembali ejaan kamu.")