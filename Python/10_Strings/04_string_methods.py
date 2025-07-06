s = "Hello world" # Strings are immutable

# s[0] = "R" # We cannot do this;

# print(s)

# a = len(s) #Find the length fot the given string
# print(a)
# print(s.upper(),s)
# print(s.lower(),s)
# print(s.capitalize(),s) # Convert first character to upper case
# print(s.title(),s) # Convert every first character to uppercase of each word

# text = " hello world "
# print(text.strip()) # "hello world"
# print(text.lstrip()) # "hello world "
# print(text.rstrip()) # " hello world"

# text = "Python is fun"
# print(text.find("is")) # 7
# print(text.replace("fun","awesome"))

# text = "Apples,Bananas,Pineapples"
# print(text.split(","))
# print(text.split(",")[0])
#join

text = "Python123"
print(text.isalpha()) # false -> Check is all characters are alphabet
print(text.isdigit()) # false -> Check is all characters are digits
print(text.isalnum()) # true -> check is ther strings are alphanumeric
print(text.isspace()) # false -> check is the strings contains space