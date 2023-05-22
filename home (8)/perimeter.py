import sys


# INSERT YOUR OWN FUNCTIONS

filename = input('Which data file do you want to use? ')
try:
    with open(filename) as file:
        rectangle = []
        for line in file:
            x1, y1, x2, y2 = map(int, line.strip().split())
            rectangle.append((x1, y1, x2, y2))
        # REPLACE PASS ABOVE WITH YOUR CODE
except FileNotFoundError:
    print('Could not open a file named', filename)
    print('Giving up...')
    sys.exit()

def perimeter(rectangle):
    minx = min(r[0] for r in rectangle)
    maxx = max(r[2] for r in rectangle)
    miny = min(r[1] for r in rectangle)
    maxy = max(r[3] for r in rectangle)
    
    width = maxx - minx + 1
    height = maxy - miny + 1
    cover = [[False] * width for _ in range(height)]
    

    for _ in rectangle:
        x1, y1, x2, y2 = _[0],_[1],_[2],_[3]
        for i in range(y1 - miny, y2 - miny):
            for j in range(x1 - minx, x2 - minx):
                cover[i][j] = True
    
    
    peri = 0
    for i in range(height):
        for j in range(width):
            if cover[i][j]:
                if i == 0 or not cover[i-1][j]:
                    peri += 1
                if i == height - 1 or not cover[i+1][j]:
                    peri += 1
                if j == 0 or not cover[i][j-1]:
                    peri += 1
                if j == width - 1 or not cover[i][j+1]:
                    peri += 1
    return peri

a=perimeter(rectangle)
print("The perimeter is:",a)
