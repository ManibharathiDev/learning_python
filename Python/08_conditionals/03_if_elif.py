age = input("Enter your age: ")
age = int(age)
if age > 18:
    print("You are an adult.")
    if age >= 21:
        print("You are now eligible to drink alcohol.")
elif age == 18:
    print("You just became an adult.")
else:
    print("You are a minor.")
print("This is the end of the program.")