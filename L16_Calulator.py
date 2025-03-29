def Calculator():
    print ("Welcome to the Calculator")
    while True:
        num1 = float(input("Enter the First Number: ")) # إدخال الرقم الأول من نوع عشري

        Operation = input("Choose operation ( + , - , * , / ) Or (Exit) to quit: ") # إدخال العملية المطلوبة أو يخرج من البرنامج
        
        if Operation.lower() == "exit": # إذا كانت العملية خروج
            print ( "                                        ")
            print ("Exiting the Calculator")
            print ( "                                        ")
            print ( "                                        ")
            break # يخرج من البرنامج
        
        num2 = float(input("Enter the Second Number: ")) # إدخال الرقم الثاني من نوع عشري

        if Operation == "+": # إذا كانت العملية جمع
            result = num1 + num2 # اجمع الرقمين

        elif Operation == "-": # إذا كانت العملية طرح
            result = num1 - num2 # اطرح الرقم الثاني من الأول

        elif Operation == "*": # إذا كانت العملية ضرب
            result = num1 * num2 # اضرب الرقمين

        elif Operation == "/": # إذا كانت العملية قسمة
            result = num1 / num2  if num2 != 0 else "Error! Division by Zero"  # اقسم الرقم الأول على الثاني

        else: # إذا كانت العملية غير معروفة
            result = "Invalid Operation" # رسالة خطأ
        
        print ( "                                        ")
        print ("The result is: ", result)
        print ( "                                        ")
        print ( "                                        ")

Calculator() # استدعاء الدالة     