print("""************************
GEOMETRİK ŞEKİL HESAPLAMA
************************""")

secenek=input("üçgen mi dörtgen mi:")

if secenek == "üçgen":
    print("üçgen hesaplanacak...")
    a=int(input("birinci kenar:"))
    b=int(input("ikinci kenar:"))
    c=int(input("üçüncü kenar:"))
#13.satırda elif kullanırsak satır başından almamız lazım öyle olursa da tanımdan çıkmış olur a,b ve c'nin referansı kaybolur o yüzden yeni bir if bloğu açtık yine aynı satırda.
    if a==b==c:
        print("eşkenar üçgen")
    elif (a==b) or (b==c) or(a==c):
        print("ikizkenar üçgen")
    else:
        print("sıradan üçgen")
if secenek=="dörtgen":
    print("dörtgen hesaplanacak...")
    d = int(input("birinci kenar:"))
    e = int(input("ikinci kenar:"))
    f = int(input("üçüncü kenar:"))
    g=int(input("dördüncü kenar:"))
    if d==f==g==e:
        print("kare")
    elif ((d==f) and (g==e)) or ((d==e) and (g==f)):
        print("dikdörtgen")
    else:
        print("normal dörtgen")









