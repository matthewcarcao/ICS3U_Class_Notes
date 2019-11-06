# for x in range(20,0,-2):
#      print("spooookyy")
#      print(x)
#
# for x in range(1,14):
#      print(x)
#
# for x in range(100,601,27):
#      print(x)
#
# for x in range(10,0,-1):
#      print(x)


input=int(input("pick a number"))
print ("Are we there yet?\n"*input)

variable=0
for x in range(0,5):
    variable=int(input("Pick a number"))+variable
print(variable/5)