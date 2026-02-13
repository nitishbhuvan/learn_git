lis=[]
n=int(input("Enter the number of elements: "))
for i in range (n):
    lis.append(int(input("Enter the list: ")))
    
print(lis)
lis.sort()
print("Sorted list: ",lis)
a=int(input("Enter the element and get its position: "))
high=n-1
low=0
while (low<=high):
    mid=(low+high)//2
    if (lis[mid]==a):
        print(f"{a} found at {mid+1}")
        break
    elif (lis[mid]>a):
        high=mid-1
    else:
        low=mid+1
print("Indexing starts from 1")