a = int(input())
for i in range(a) : #a 사용하는 건 이중 for 문 사용하기 
    arr = list(map(str,input()))
    sum = 0 
    c =1 
    for i in arr:
        if i == 'O' : 
            sum += c
            c += 1
        else : 
            c = 1 
    print(sum)

