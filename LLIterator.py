class LLIterator:
    def __init__(self, node):
        self.current = node

    def __next__(self):
        if not self.current:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value