from module import greet
x=42
z=13
def outer():
    print(f'y before: {"y" in locals()}')
    y=12
    print(f'y in outer after assging:{"y" in locals()}')
    def answer(x):
        adssad=12+y+x
        print(f'y in other after assging:{"y" in locals()}')
        print(locals())
        print(globals())
        return x
    return answer(y)
if __name__=='__main__':
    x=42
    print(f'y dhddhdh in locals:{"y" in locals()}')
    outer()
# print(greet('Vova'))