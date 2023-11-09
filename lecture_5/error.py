def convert_and_divide(a:str, b: str) ->tuple[ int, int]:
    a, b = int(a), int(b)
    return a, b
def divide_ab(a: int|float, b: int| float) -> float:
    if 3 in [a,b]:
        raise Exception('NO THIRD')
    return a/b
while True:
    a, b= input('Введите 2 числа для их суммы').split()
    division_score=None
    try:
        a, b= convert_and_divide(a,b)
        division_score=divide_ab(a,b)
    except(ZeroDivisionError,ValueError) as e:
        print('Ошибка: {e}')
        print('Произошла ошибка')
        print()
        continue
    # except ZeroDivisionError as e:
    #     print('Ошибка: {e}')
    #     print('Ноль zero')
    #     print()
    #     continue
    except AttributeError as ex:
        print('No_ThIRD')
        print('наоборот')
        break
    except Exception as ex:
        print('No zero to errors')
    finally:
        print('Finally it is done')
    ab_sum= a + b
    print(f'Сумма {a} + {b} = {ab_sum}')
    print(f'{a}/{b}={divide_ab}')
    print()