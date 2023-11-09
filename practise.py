numbers: list=[1,2,3,4,5,6,7,8,9,15]
# for n in numbers:
#     print("-", end="")
#     if n%3==0:
#         print(f'Число-{n} кратно 3')
#     if n%3!=0:
#         print(f'Число-{n} не кратно 3')
# for n in numbers:
#     if n%3==0 and n%5==0:
#         print(f"Число-{n} делится и на 3 и на 5")
#     elif n%3==0:
#         print(f"Число-{n} число делится на 3")
#     elif n%5==0:
#         print(f"Число-{n} делится на 5")
#     else:
#         print(f"Число-{n} не делится ни на 5, ни на 7")
# word: str = input('Введите слово')
# vowel='aeiouy'
# vowel_count: int=0
# for ch in word:
#     if ch in vowel:
#         vowel_count+=1
# print(vowel_count)
n: int = int(input('N: '))
# sum_all=0
# for i in range(n+1):
#     if i%3==0 or i%5==0:
#         sum_all+=i 
# print(sum_all)
list_3: list=[]
list_5: list=[]
sum_all=0

for i in range(n+1):
    if i%3==0 and i%5==0:
        list_3.append(i)
    if i%5==0:
        list_5.append(i)
sum_all= sum(list_3) + sum(list_5)
print(sum_all)
