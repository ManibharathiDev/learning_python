marks = [5,4,3,5]
print(marks)
marks.append(56) # This will change the originial list
print(marks)
#marks.pop() # It removes the last element

marks.pop()
print(marks)

marks.insert(0,68)
print(marks)
extra_marks = [56,78,90]
marks.extend(extra_marks)
print(marks)
marks.remove(56)
print(marks)
marks.reverse()
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)