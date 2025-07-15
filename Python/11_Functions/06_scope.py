# def sum(a,b):
#    a,b and c are local variables
#     c = a+b
#     return c
c = 0
def sum(a,b):
    c = a+b # it creates a local variable called c which is destroyed after this function returns

sum(4,6)
print(c)