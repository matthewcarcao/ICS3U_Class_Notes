import random
# def area_of_triangle(base, height):
#     area = (base * height)/2
#     return area
# triangle_area = area_of_triangle(4,3)
#
# def area_of_square(length):
#     area = length*length
#     return area
# length=float(input("Low me a length ahlie"))
# square = area_of_square(length)
# print(int(square))

# text = str(input("Write something"))
# def data():
#     print (text*5)
# data()

# def data(text):
#     text=text.upper()
#     return text
# data1=str(input("Write something"))
# print(data(data1))

def lottery(num1,num2,num3):
    lot1=random.randint(1,10)
    return lot1
    lot2=random.randint(1,10)
    return lot2
    lot3=random.randint(1,10)
    return lot3
guess1=int(input("Pick a number from 1-10"))
guess2=int(input("Pick another number from 1-10"))
guess3=int(input("Pick your final number from 1-10"))
if guess1==lotran1(0) and guess2==lotran2(1) and guess3==lotran3(2):
    print("You won the lottery!")