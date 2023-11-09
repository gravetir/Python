from typing import TypeAlias

ComplicatedDict: TypeAlias = dict[
    int | str | None, int | str | None | dict[int | str | None, int | str]
]
alphabet: dict[
    int | str | None | float, str | int | float | ComplicatedDict[ComplicatedDict]
] = {
    2: "B",
    3: set([1, 2, 3, 4, 5, 6]),
    4: {1: "A", 2: 3, 3: {"A": 12}},
    10: "Y",
    "Z": 10,
    0.1: "SDA",
    True: "sffsf",
    False: 1314124,
    None: "fsdfsfs",
}
# for_class_a:dict[str,Any]={'A:1','B:2',}
# class A:
#     def __init__(self, **kwargs):
#         for key,value in kwargs:
#             self.key=value
# a=A(**for_class_a)
# print(a.key)
# o_letter=alphabet.get('0',None)
# if not bool (o_letter):
#     print('NO 0')
# for key, value in alphabet.items(): #.keys() .values()
#         print(f'Ключ:{key} Значение:{value}')
print(alphabet.get(4).get(3).get("A"))
