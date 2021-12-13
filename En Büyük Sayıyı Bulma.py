#EN BÜYÜK SAYIYI EKRANA YAZDIRMA
print("""************************
EN BÜYÜK SAYIYI BULMA PROGRAMI
************************""")

a=int(input("birinci sayı:"))
b=int(input("ikinci sayı:"))
c=int(input("üçüncü sayı:"))

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
    