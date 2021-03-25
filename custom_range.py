class CustomRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.value = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > self.end:
            raise StopIteration
        current_value = self.value
        self.value += 1
        return current_value


one_to_ten = CustomRange(1, 10)
for num in one_to_ten:
    print(num)
