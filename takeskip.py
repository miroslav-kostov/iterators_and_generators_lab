class TakeSkip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current_index = 1
        self.result = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index > self.count:
            raise StopIteration
        current_res = self.result
        self.result += self.step
        self.current_index += 1
        return current_res


numbers = TakeSkip(10, 5)
for number in numbers:
    print(number)

numbers = TakeSkip(2, 6)
for number in numbers:
    print(number)

