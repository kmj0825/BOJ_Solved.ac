t = int(input())
for i in range(0,t) :
    r,s = input().split()
    r = int(r)
    for j in s : 
        print(j * r, end = '')
    print()