try : # يحاول تنفيذ الكود التالي
    number = int(input("Enter a number: ")) # لازم يدخل بيان رقمي غير الصفر
    result = 10 / number
    print("Result:", result)

except ZeroDivisionError: # في حالة القسمة على الصفر
    print("You can't divide by zero!")

except ValueError: # في حالة إدخال قيمة غير رقمية
    print("Please enter a number!")
