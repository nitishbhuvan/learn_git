lis=[]
n=int(input("Enter the number of elements: "))
for i in range (n):
    lis.append(int(input("Enter the list: ")))
    
print(lis)
id=1
a=int(input("Enter the element and get its position: "))
for i in lis:
    if(i==a):
        print(f"{a} found at {id}")
    id+=1
print("Indexing starts from 1")