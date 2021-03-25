class ReverseIter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = len(self.iterable)

    def __iter__(self):
        return self

    def __reversed__(self):
        return self.iterable

    def __next__(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        current_value = self.iterable[self.index]
        return current_value

reversed_list = ReverseIter([1, 2, 3, 4])
for item in reversed_list:
    print(item)