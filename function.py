def sum_numbers(n):
    numbers_set=set()
    for i in range(n+1):
        if i%3==0 or i%5==0:
            numbers_set.add(i)
    return sum(numbers_set)
n=int(input())
res=sum_numbers(n)
print(res)