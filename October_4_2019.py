input_date = input("What is your birthday?")
input_month = input("What is your birth month?")
input_year = input("What is your birth year")

input_name = input("What is your name?")
print("Hello " +  input_name)

if 4<3:
    print("4 is not less than 3")

input_num = int (input("Pick a number"))
if input_num>10:
    print("this number is greater than 10")

input_word = str(input("Pick a word"))
if len(input_word)<5:
    print("This word has less than 5 characters")
if len(input_word)>5:
    print("This word has more than 5 characters")
if len(input_word)==5:
    print("This word has 5 characters")

input_course1 = int(input("What mark did you get on your first course"))
input_course2 = int(input("What mark did you get on your second course"))
input_course3 = int(input("What mark did you get on your third course"))
input_course4 = int(input("What mark did you get on your fourth course"))
if (input_course1+input_course2+input_course3+input_course4)/4 >80:
    print("You gor above an 80")
if (input_course1+input_course2+input_course3+input_course4)/4 <50:
    print("you did not pass")