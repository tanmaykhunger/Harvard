#Calculator app

first_number = input("What is your first number? ")
second_number = input("What is your second number?")
add = int(first_number) + int(second_number)
sub = int(first_number) - int(second_number)
question = input("Do you want to add or subtract? ")

if question == "add":
    print(add)


if question == "subtract":
    print(sub)