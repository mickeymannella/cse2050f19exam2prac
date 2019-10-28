class BufferedIterator:
    def __init__(self, i):
        self._i = iter(i)
        self._hasnext = True
        self._buffer = None
        self._advance()

    def peek(self):
        return self._buffer

    def hasnext(self):
        return self._hasnext

    def _advance(self):
        try:
            self._buffer = next(self._i)
        except StopIteration:
            self._buffer = None
            self._hasnext = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.hasnext():
            output = self.peek()
            self._advance()
            return output
        else:
            raise StopIteration