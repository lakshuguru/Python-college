print('lakshanaa-20bit066')
n=int(input("Enter a size of a list:"))
L1=[]
L2=[]
for i in range(0,n,1):
    L3=int(input())
    if(L3%2==0):
        L1.append(L3)
    else:
        L2.append(L3)
print(L1)
print(L2)
L5=L1.sort()
L4=L2.sort()
print("The highest odd number is :",L1[-1])
print("The highest even number is :",L2[-1])
