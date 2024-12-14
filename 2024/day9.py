from itertools import accumulate

class Chunk:
    def __init__(self, position, size):
        self.position = position
        self.size = size

    def __iter__(self):
        return iter(range(self.position, self.position + self.size))

with open("day9.in", "r") as f:
    sizes = [int(size) for size in f.read().strip()]
    chunks = [Chunk(pos, size) for pos, size in zip(accumulate(sizes, initial=0), sizes)]
    files = chunks[::2]
    spaces = chunks[1::2]

empty_blocks = (pos for space in spaces for pos in space)
file_blocks = [(pos, i) for i, file in enumerate(files) for pos in file]
print(sum(min(pos, next(empty_blocks, pos)) * i for pos, i in reversed(file_blocks)))

def get_spaces(size):
    for space in spaces:
        while space.size >= size:
            space.size -= size
            space.position += size
            yield space.position - size

allocators = [get_spaces(size) for size in range(10)]
for file in reversed(files):
    file.position = min(file.position, next(allocators[file.size], file.position))
print(sum(pos * file_id for file_id, file in enumerate(files) for pos in file))
