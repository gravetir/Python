a:  list[int]= [1,2,3,3,5]
b: list[int]=[0,0,1,0,1]
def mask_list(array: list[int], mask: list[int]) -> list[int]:
    assert type(array)==list
    return[val*mask[i] *.5 for i, val in enumerate(array)]

def test_mask_list():
    print('Проверка')
    assert test_mask_list([1,2,3],[0,1,0]==[0,2,0])

answer=mask_list(array=a, mask=b)
print(answer)

# answer_1 = [val*b[i] for i, val in enumerate(a)] # вариант 1
# print(answer_1)
# answer_2=[val*b[i] for i, val in enumerate(a)]
# for i,val in enumerate(a):
#     answer_2.append(val*b[i])
# print(answer_2)         # вариант 2
# for i, val in enumerate(a):
#     print(f'index {a}')