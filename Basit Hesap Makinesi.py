print("""******************************
HESAP MAKİNESİ PROGRAMI
İşlemler;
1=Toplama işlemi
2=Çıkarma işlemi
3=Çarpma işlemi
4=Bölme işlemi
*******************************""")

a=int(input("birinci sayı:"))
b=int(input("ikinci sayı:"))
işlem=input("işlem numarası:")

if işlem=="1":
    print("{} ile {} sayısının toplamı {}'dır.".format(a,b,a+b))
elif işlem=="2":
    print("{} ile {} sayısının farkı {}'dır.".format(a,b,a-b))
elif işlem=="3":
    print("{} ile {} sayısının çarpımı {}'dır.".format(a,b,a*b))
elif işlem=="4":
    print("{} ile {} sayısının bölümü {}'dır.".format(a,b,a/b))
else:
    print("lütfen geçerli bir işlem numarası girin!")



