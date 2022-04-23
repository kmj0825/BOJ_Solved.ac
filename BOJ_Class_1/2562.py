arr = []
for i in range(0,9) :
    arr.append(int(input()))

print(max(arr))
index = arr.index(max(arr))
print(index+1)