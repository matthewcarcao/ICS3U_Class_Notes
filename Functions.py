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
#
# text = str(input("Write something"))
# def data():
#     print (text*5)
# data()
#
# def data(text):
#     text=text.upper()
#     return text
# data1=str(input("Write something"))
# print(data(data1))

def lottery(num1,num2,num3):
    lot1=random.randint(1,10)
    lot2=random.randint(1,10)
    lot3=random.randint(1,10)
    if num1==lot1 and num2==lot2 and num3==lot3:
        return "You won the lottery!"
    else:
        return "You lost!"
print(lottery(1,6,3))