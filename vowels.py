class Vowels:
    vowels = ["a", "y", "u", "o", "e", "i", "A", "Y", "U", "O", "E", "I"]

    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.string):
            raise StopIteration
        current_char = self.string[self.index]
        self.index += 1
        if current_char not in Vowels.vowels:
            return self.__next__()
        return current_char


# def vowels(text):
#     the_vowels = ["a", "y", "u", "o", "e", "i", "A", "Y", "U", "O", "E", "I"]
#     for ch in text:
#         if ch in the_vowels:
#             yield ch

my_string = Vowels('Abcedifuts0 a fAfk;wfjvWMVkaskgapgpwoq;wqlqwefkl;kZCAQPASODjfafdsjlkfjy0o')
for char in my_string:
    print(char)
