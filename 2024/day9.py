with open("day9.in", "r") as f:
    disk_map = [(i & 1 != 0, i // 2, int(size)) for i, size in enumerate(f.read().strip())]

total_size = sum(size for empty, i, size in disk_map if not empty)
movable = (i for empty, i, size in reversed(disk_map) if not empty for _ in range(size))
blocks = (next(movable) if empty else i for empty, i, size in disk_map for _ in range(size))
print(sum(pos * i for pos, i in zip(range(total_size), blocks)))
