print("""********************
KULLANICI GİRİŞİ
********************""")

sys_kullanıcıadı="hhamza"
sys_parola="123456"

a=input("kullanıcı adı:")
b=input("parola:")

if sys_kullanıcıadı!=a and sys_parola==b:
    print("kullanıcı adı hatalı")
elif sys_kullanıcıadı==a and sys_parola!=b:
    print("parola hatalı")
elif sys_kullanıcıadı!=a and sys_parola!=b:
    print("kullanıcı adı ve parola hatalı")
else:
    print("kullanıcı girişi başarılı")