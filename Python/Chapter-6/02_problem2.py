'''Write a program to find out whether a student has passed or failed if it requires a total of
40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
input from the user'''

marks1 = int(input("enter the number1: "))
marks2 = int(input("enter the number2: "))
marks3 = int(input("enter the number3: "))
marks4 = int(input("enter the number4: "))

#check for total percentage

total_percentage = (marks1 + marks2 + marks3 + marks4)/400*100
print(total_percentage)

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33 and marks4>=33):
    print("you are passed",total_percentage)

else:
    ("You failed,try again next year",total_percentage)    