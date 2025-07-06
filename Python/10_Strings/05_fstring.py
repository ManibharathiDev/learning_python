# String formatting

template = "Dear {}, You are awesome. Take this {}Rs bag"

a = "John"
a1 = 10000
b = "Jack"
b1 = 9000
c = "Marie"
c1 = 3000
s1 = template.format(a,a1)
print(s1)
s2 = template.format(b,b1)
print(s2)
s3 = template.format(c,c1)
print(s3)

print(f"{a} you are awesome and take this {a1}Rs bag")

print(ord('A')) # Ascii code
print(chr(65)) # Normal value