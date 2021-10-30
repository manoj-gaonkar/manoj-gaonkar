def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print()
p=int(input("enter the num"))
pattern(p)

output:
1
12
123
1234
12345

2.Triangle pattern:
    
for i in range(5):
    for j in range(i):
        print("*",end="")
    print()
for i in range(5):
    for j in range(j):
        print("*",end="")
    print()
    
output:

*
**
***
****
***
**
*
  
