import  math
x = 'How many charactor do i have?'
n = str(len(x))
print(n + ' - '+ x)
print(len(x))

def wonder_print(s):
    n= str(len(s))
    print(n + ' - ' + s)

wonder_print('yoyoy')

def print_with_bracket(name):
    print([[[   name   ]]])
def print_3_names(name1,name2,name3):
    print_with_bracket(name1)
    print_with_bracket(name2)
    print_with_bracket(name3)

print_3_names('mj', 'sdfg','sdffsdfg')

print_with_bracket(" gfm ")


def area_of_circle(radius):
    def squared(x):
        return x**2
    return squared(radius*math.pi)
print(area_of_circle(5))
print ( area_of_circle . __doc__ )