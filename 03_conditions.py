


def is_even (x):
    return x % 2 == 0
a= is_even (22)
print (a)
b= is_even (21)
print (b)

mark = int( input (" What  is the  mark ? "))
category = ""
if mark >= 55:
    result = " pass "
    if mark < 80:
        category = " average "
    else :
        category = " exceptional "
else:
    result = " fail "
print (result , category )

def day_of_week (n):
    if n == 0:
        print (" Monday ")
    elif n == 1:
        print (" Tuesday ")
    elif n == 2:
        print (" Wednesday ")
    elif n == 3:
        print (" Thursday ")
    elif n == 4:
        print (" Friday ")
    elif n == 5:
        print (" Saturday ")
    elif n == 6:
        print (" Sunday ")
    else :
        print (" value   not  correct ")
a = int( input (" What  is the  day? "))
day_of_week (a)