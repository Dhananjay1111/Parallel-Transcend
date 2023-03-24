movies = [ "The   Addams   Family ", " Ghostbusters ", " Jurassic   Park ", " Pulp   Fiction ", " Home   Alone ", " The  Matrix "]
print(movies[0])

movies.insert(0,'Back to the future')
movies.remove(' Pulp   Fiction ')
print(movies)
print(movies)
print(movies[::-2])


print ("Star   Wars" in movies )
print(" Jurassic   Park " in movies)



movies[0:3] = ['1','2','3']
movies.append('forrest gum')
movies.extend(['vxcvxcv'])
print(movies)
del movies[:]
print(movies)

tv_shows = [ [" Sherlock   Holmes ", " Drama " ,2009] ,
[" Planet   Earth ", " Documentary ", 2006] ,
[" Cosmos ", " Documentary ", 2014] ,
["Dr. Who "," Science   fiction ", 2005] ,
[" Stranger   Things "," Science   fiction ", 2016] ,
[" Game  of  Thrones "," Fantasy ", 2011]]

print(tv_shows[3][1:])

movies = ("The  Addams   Family ", " Ghostbusters ", " Jurassic   Park ",
" Pulp   Fiction ", " Home   Alone ", " The  Matrix ")
print ( movies [2])
movies[2]="star"
print(movies)
