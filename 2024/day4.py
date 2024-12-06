with open("day4.in", "r") as f:
    horizontal = f.read()

width = horizontal.index('\n') + 1
vertical = [horizontal[i::width] for i in range(width)]
diag_l = [horizontal[i::width - 1] for i in range(width - 1)]
diag_r = [horizontal[i::width + 1] for i in range(width + 1)]
lines = [horizontal] + vertical + diag_l + diag_r

print(sum(line.count("XMAS") + line.count("SAMX") for line in lines))

def is_x_mas(i):
    diag_l = horizontal[i - width + 1:i + width:width - 1]
    diag_r = horizontal[i - width - 1:i + width + 2:width + 1]
    return diag_l in ["MAS", "SAM"] and diag_r in ["MAS", "SAM"]

print(sum(1 for i in range(width + 1, len(horizontal) - width - 2) if is_x_mas(i)))
