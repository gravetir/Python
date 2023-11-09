def my_personal_sum(#обявляем ф-цию
                    #переменная  x с типом int или float
                    x:int | float,
                    #переменная  y с типом int или float
                    y: int|float,) -> int: #вернёт int или float
    answer=x/y
# def my_personal_sum(**args,**kwargs) -> int|float:
#     for num in args:
#         answer+=num
#     return answer
_list1: list=[1,2,3]
_list2: list[2,4,6]
print(my_personal_sum(_list1))
# print(sum([3,5]))
    