import math, random
def generate_route(start, end, priority):
    steps = 30 if priority == "Low" else 20 if priority == "Medium" else 12
    sx, sy = start
    ex, ey = end
    route = []
    for i in range(steps + 1):
        t = i / steps
        t2 = t * t * (3 - 2 * t)
        x = sx + (ex - sx) * t2
        y = sy + (ey - sy) * t2
        wobble = 0.5 if priority != "High" else 0.2
        x += (random.random() - 0.5) * wobble
        y += (random.random() - 0.5) * wobble
        x = max(0, min(100, x))
        y = max(0, min(100, y))
        route.append({ "x": round(x, 2), "y": round(y, 2) })
    return route
