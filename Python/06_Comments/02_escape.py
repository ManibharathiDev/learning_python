#Escape characters in Python
print("Hey how are you\nI am good\\What about you?")

print("Hello \"World\"")  # This will correctly print: Hello "World"

print('Hello \'World\'',"How are you")  # This will correctly print: Hello 'World'

print("Hello \"World\"")  # This will correctly print: Hello "World"

print("Hello Wordld","Manibharathi",35)

print("Hello World", "Manibharathi", 35, sep=",")  # This will print: Hello World,Manibharathi,35

print("Hello World", "Manibharathi", 35, sep=", ", end="!")  # This will print: Hello World, Manibharathi, 35!

print("Hey May you god bless you.",end="!...")  # This will print: Hey May you god bless you.!...