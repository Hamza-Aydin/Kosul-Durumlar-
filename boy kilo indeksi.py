#Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın
print("""***************************** 
OBEZİTE HESAPLAMA
*****************************""")

k=int(input("kilonuzu giriniz:"))
b=float(input("boyunuzu giriniz:"))

bedenkitleindeksi=k/b**2

if bedenkitleindeksi <18.5:
    print("zayıf")
elif 18.5<bedenkitleindeksi<25:
    print("normal")
elif 25<bedenkitleindeksi<30:
    print("fazla kilolu")
else:
    print("obez")