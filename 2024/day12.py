with open("day12.in", "r") as f:
    plots = {x + y * 1j: plant for y, row in enumerate(f) for x, plant in enumerate(row.strip())}

regions = []
while plots:
    plot, plant = plots.popitem()
    region = {plot}
    todo = [plot]
    while todo:
        plot = todo.pop()
        for d in [1, 1j, -1, -1j]:
            if plots.get(plot + d) == plant:
                todo.append(plot + d)
                del plots[plot + d]
                region.add(plot + d)
    regions.append(region)

def price(plots, discount):
    area = len(plots)
    perimeter = 0
    for up in [1, 1j, -1, -1j]:
        left = up * 1j
        for plot in plots:
            top_fence = plot + up not in plots
            left_top_fence = plot + left in plots and plot + left + up not in plots
            perimeter += top_fence and not (discount and left_top_fence)
    return area * perimeter

print(sum(price(region, False) for region in regions))
print(sum(price(region, True) for region in regions))
