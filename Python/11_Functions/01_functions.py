# a = 4
# b = 2
# c = 1
# average = (a+b+c)/3
# print(average)

# a1 = 5
# b1 = 1
# c1 = 8
# average = (a1+b1+c1)/3
# print(average)

# def keyword to create a function
def average(a,b,c): # Function Defining
    average = (a + b + c)/3
    print(average)

average(10,20,30) # Function calling
average(4,3,5)
o2 = average(4,6,7)
print(o2) # Print none if the function return nothing

def addThreeNumber(a,b,c):
    add = a+b+c
    return add

o3 = addThreeNumber(45,67,89)
print(o3)