# вывод корень числа , если он целый
# если корня нету тогда "Трудно"
# def guess(num:int) -> int:
def guess(num: int) -> int | str:
    for i in range(num + 1):
        if num == i**2:
            return i
    return "Слишком сложно, не могу"


print(guess(int(input("Введите число: "))))
# import math
# res=int()
# def guess(num:int) -> int:
#     res=math.sqrt(num)
#     return res
# def guess(num:int) -> int|str:
#     for i in range(1,num):
#          if i**2==num:
#              return(i)
#          else:
#              return("Трудно")
#     print(guess(num))
