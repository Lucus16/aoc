with open("day9.in", "r") as f:
    disk_map = [(i & 1 != 0, i // 2, int(size)) for i, size in enumerate(f.read().strip())]

total_size = sum(size for empty, i, size in disk_map if not empty)
movable = (i for empty, i, size in reversed(disk_map) if not empty for _ in range(size))
blocks = (next(movable) if empty else i for empty, i, size in disk_map for _ in range(size))
print(sum(pos * i for pos, i in zip(range(total_size), blocks)))

from heapq import *

filepos = dict()
empties = [list() for _ in range(10)]
pos = 0
for empty, i, size in disk_map:
    if empty:
        heappush(empties[size], pos)
    else:
        filepos[i] = pos
    pos += size

checksum = 0
for _empty, i, i_size in disk_map[::-2]:
    options = sorted(
        ((heap, heap_size)
         for heap, heap_size in zip(empties[i_size:], range(i_size, 10))
         if heap and heap[0] < filepos[i]),
        key=lambda h: h[0][0]
    )
    if options:
        heap, heap_size = options[0]
        filepos[i] = heappop(heap)
        heappush(empties[heap_size - i_size], filepos[i] + i_size)
    checksum += sum(pos * i for pos in range(filepos[i], filepos[i] + i_size))
print(checksum)
