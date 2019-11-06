a=[1,2,3]
b=[99,98,97]
newlist=[a,b]
print (newlist)
row_sum=int(input("What row would you like the some of?"))
sum = 0
if row_sum==1:
    for i in newlist[0]:
        sum = sum + i
elif row_sum==2:
    for i in newlist[1]:
        sum = sum + i
print(sum)
column_sum=int(input("What column would you like the some of?"))
sum = 0
if column_sum==1:
    for i in newlist:
        sum = sum + i[0]
elif column_sum==2:
    for i in newlist:
        sum = sum + i[0]
print(sum)