from functools import total_ordering


@total_ordering
class Number:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


print(Number(10) > Number(5))
print(Number(5) < Number(10))
print(Number(5) >= Number(5))
print(Number(10) <= Number(5))