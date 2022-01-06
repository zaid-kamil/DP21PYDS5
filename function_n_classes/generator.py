# old way

def get_cube_old(*args):
    x = []
    for i in args:
        x.append(i**3)
    return x

print(get_cube_old(1,2,3,3,3,3,31,23,132,1))

def get_cube(*args):
    for i in args:
        yield i ** 3

for val in get_cube(11,23,45):
    print(val)