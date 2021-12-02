# Pyramid printer
def print_pyramid(height):
    height = height // 2
    r = 1
    for i in range(height):
        print(((height - r)) * ' ' + r * '* ')
        r += 1
    r = height - 1
    for j in range(height):
        print(((height - r)) * ' ' + r * '* ')
        r -= 1
    
print_pyramid(10)