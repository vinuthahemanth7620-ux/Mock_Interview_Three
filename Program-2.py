
maximum = int(input("Enter the maximum number: "))

class EvenNumbers:
    def __init__(self, maximum):
        self.maximum = maximum
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.maximum:
            number = self.current
            self.current += 2
            return number
        else:
            raise StopIteration

even = EvenNumbers(maximum)

print("Even numbers:")

for num in even:
    print(num)
