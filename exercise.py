# Pythone Program to calculate Mark  of  student

student_Mark = float(input("Please enter your Mark: "))
if student_Mark == True:
    if student_Mark >= 80 and student_Mark <= 100:
        print("Congratulation,You Mark is A!")
    elif student_Mark >= 60 and student_Mark < 80:
        print("Good,You Mark is B!")
    elif student_Mark >= 40 and student_Mark < 60:
        print("Nice try,You Mark is C!")
    elif student_Mark >= 0 and student_Mark < 40:
        print("Sorry you failed.")
    else:
        print("You have put invalid marks!")            
