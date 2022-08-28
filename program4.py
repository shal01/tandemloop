
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())

    lst.append(ele)

print(lst)
dict1={}
for i in range(1,10):
    count=0
    for j in lst:
        if j%i==0:
            count+=1
    dict1[i]=count
    # print(i,":",count )
print(dict1)