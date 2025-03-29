# طباعة الأعداد الزوجية من 1 إلى 10
for i in range(2, 11, 2):
    print(i)

print("=====================================")
i = 2
while i <= 10:
    print(i)
    i += 2
print("=====================================")

# السماح بتسجيل الدخول للمستخدمين الذين يمتلكون اسم المستخدم وكلمة المرور الصحيحة
username = "admin"
password = "1234"
while True:
    user = input("Enter username: ")
    passw = input("Enter password: ")
    if user == username and passw == password:
        print("Welcome")
        break #لإيقاف التكرار
    else:
        print("Try again")