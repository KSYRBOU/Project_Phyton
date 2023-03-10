l = [1, 2, 3, 5, 8, 15, 23, 38]
result = ()
for i in l:
    if i % 2 == 0:
        result.append(i)
        result.append(i * 2)
print(result)