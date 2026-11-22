
def factorial_generator(max_value):
    num = 0
    fact = 1
    while num <= max_value:
        yield fact
        num += 1
        fact = fact * num

max_value = int(input("Enter maximum value: "))
print("Factorial values:")

for value in factorial_generator(max_value):
    print(value)
