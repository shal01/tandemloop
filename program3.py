
num=int(input("enter a number :"))

for i in range(1,num+1):
  if (i%2!=0):
        for j in range(1, i + 1):
            print(1 + ((j-1) * 2), end=" ")
        print()
        for j in range(1, i + 1):
            print(1 + ((j-1) * 2), end=" ")
        print()
