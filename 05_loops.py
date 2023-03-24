
i= 1
while i <= 10:
    print (i)
    i = i + 1
print (" Finished ")

i = 0
while i < 9:
    i = i + 1
    if i==5 or i ==7:
        continue # Back to the while statement
    else :
        print (i)
print (i+1)

movies = [ "The   Addams   Family ", " Ghostbusters ", " Jurassic   Park ",
" Pulp   Fiction ", " Home   Alone ", " The  Matrix "]

i = 0
while i<6:
    print(movies[i])
    i = i + 1

for i in range (0,6):
    print(movies[i])

########################################################################################################################

tv_shows = [ [" Sherlock   Holmes ", " Drama " ,2009] ,
[" Planet   Earth ", " Documentary ", 2006] ,
[" Cosmos ", " Documentary ", 2014] ,
["Dr. Who "," Science   fiction ", 2005] ,
[" Stranger   Things "," Science   fiction ", 2016] ,
[" Game  of  Thrones "," Fantasy ", 2011]
]
print(tv_shows[0][2])

for i in range(5):
    for j in range(3):
        print(tv_shows[i][j])


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
cols = 3
the_sum = 0
for i in range(rows):
    for j in range(cols):
        the_sum += m[i][j]
        print(m[i][j])
print("The sum is: ", the_sum)