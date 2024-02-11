def f(curr,end):
    if curr>end:
        return 0
    elif curr==end:
        return 1
    else:
        return  f(curr+2,end)+f(curr*2,end)+f(curr*3,end)
print(f(2,6)*f(6,28))