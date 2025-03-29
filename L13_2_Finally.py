try: # يجرب ينفذ الأمر التالي
    file = open("data.txt", "r")
    content = file.read()
    print(content)

except FileNotFoundError: # في حالة عدم وجود الملف
    print("Error: File not found!")

finally:  # تنفيذ أمر سواء حدث خطأ أم لم يحدث
    print("Execution completed!")  # تنفيذ هذا الأمر بعد الانتهاء من التنفيذ السابق‍