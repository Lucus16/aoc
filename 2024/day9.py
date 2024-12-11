with open("day9.in", "r") as f:
    disk_map = [(i & 1 != 0, i // 2, int(size)) for i, size in enumerate(f.read().strip())]

total_size = sum(size for empty, i, size in disk_map if not empty)
movable = (i for empty, i, size in reversed(disk_map) if not empty for _ in range(size))
blocks = (next(movable) if empty else i for empty, i, size in disk_map for _ in range(size))
print(sum(pos * i for pos, i in zip(range(total_size), blocks)))

from dataclasses import dataclass

@dataclass
class Chunk:
    position: int
    size: int

    def range(self):
        return range(self.position, self.position + self.size)

def get_chunks(sizes):
    position = 0
    for size in sizes:
        yield Chunk(position, size)
        position += size

with open("day9.in", "r") as f:
    chunks = list(get_chunks(int(size) for size in f.read().strip()))
    files = chunks[::2]
    spaces = chunks[1::2]

def get_spaces(size):
    for space in spaces:
        while space.size >= size:
            position = space.position
            space.size -= size
            space.position += size
            yield position

allocators = {size: get_spaces(size) for size in range(1, 10)}
for file in reversed(files):
    file.position = min(file.position, next(allocators[file.size], file.position))

print(sum(pos * file_id for file_id, file in enumerate(files) for pos in file.range()))
