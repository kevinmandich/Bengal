## grid_walk.py
## Challenge #60

def sum_digits(num):

    sum_ = 0
    while num:
        sum_, num = sum_ + num%10, num/10
    return sum_

def is_walkable(a, b):

    return sum_digits(abs(a)) + sum_digits(abs(b)) <= 19

def is_connected(x,y):

    global walkable    
    try:
        c = walkable[y-1][x]
        return 1
    except:
        return 0

walkable = {}
walkable[0] = {0:1}
stillWalkable = True
layer = 1
total = 0

while stillWalkable:
    walkable[layer] = {}
    connected = []

    ## look for connections to inner layer first
    for x in range(0, layer):
        if is_connected(x, layer) and is_walkable(x, layer):
            if x == 0:
                walkable[layer][x] = 0.5
            else:
                walkable[layer][x] = 1
            connected.append((x, layer))

    ## take care of adjacent squares
    for pair in connected:
        x, y = pair
        ## go left
        i = x - 1
        while i > 0:
            if is_walkable(i, layer):
                if i == layer or i == 0:
                    walkable[layer][i] = 0.5
                else:
                    walkable[layer][i] = 1
            else:
                break
            i -= 1
        ## go right
        i = x + 1
        while i <= layer:
            if is_walkable(i, layer):
                if i == layer or i == 0:
                    walkable[layer][i] = 0.5
                else:
                    walkable[layer][i] = 1
            else:
                break
            i += 1
            
    if len(connected) == 0:
        stillWalkable = False

    for key in walkable[layer]:
        total += walkable[layer][key]

    del walkable[layer-1]
    layer += 1

print int(total*8 + 1)










