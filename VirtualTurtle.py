def turtle(coord, direction):
    x, y = coord
    while True:
        c = yield x, y
        if c == 'f':
            if direction == 0:
                x += 1
            elif direction == 1:
                y += 1
            elif direction == 2:
                x -= 1
            else:
                y -= 1
        elif c == 'r':
            direction = (4 + direction - 1) % 4
        else:
            direction = (direction + 1) % 4

