print("""*****************
TOPLAM NOT HESAPLAMA
*****************""")

vize1=int(input("birinci vize notunuzu giriniz:"))
vize2=int(input("ikinci vize notunuzu giriniz:"))
final=int(input("final notunuzu giriniz:"))

toplamnot=(vize1*30/100)+(vize2*30/100)+(final*40/100)

if toplamnot>=90:
    print("aa")
elif toplamnot>=80:
    print("ba")
elif toplamnot>=70:
    print("bb")
elif toplamnot>=60:
    print("cb")
elif toplamnot>=50:
    print("cc")
else:
    print("kaldınız!")