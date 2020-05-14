def Outer_func(a,b):
    def Inner_func():
        var = a + b
        return var
    var2 = Inner_func()
    var3 = var2 + 5
    return var3

add = Outer_func(5,5)
print(add)