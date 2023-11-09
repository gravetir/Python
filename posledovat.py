def posledov_index(n):
    index: list=[]
    for i in range(1,len(n)):
        if (n[i] != n[i-1]+1):
            index.append(i)
    return index if index else "Не найдено"

print(posledov_index([-19, -18, -17, -16,  -10, 0, 20]))
