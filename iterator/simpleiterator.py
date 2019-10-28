class SimpleIterator:
    def __init__(self):
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._count < 10:
            self._count += 1
            return self._count
        else:
            raise StopIteration

iterator1 = SimpleIterator()
for x in iterator1:
    print(x)

iterator2 = SimpleIterator()
L = [2 * x for x in iterator2]