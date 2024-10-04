lis = []

n = int(input())

for x in range(n):
    y = int(input())
    lis.append(y)
print("The List Is : " ,lis)

sumList = []
for x in lis :
    sumIs = sum(map(int , str(x)))
    sumList.append(sumIs)

print(sumList)
        