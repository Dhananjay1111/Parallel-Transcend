agenda = {" Mary ": " 12345678 ", " Emily ": " 87654321 ",
" Steve ": " 56789121 ", " Patrick ": " 78901234 "}
# add four friends to the dictionary . Name as key and the
# phone number as value
print ( agenda )

print(agenda.values())
print(agenda[" Mary "])

j = [1,2,3,4]
k= "lauda"

agenda = {}
agenda [" Mary "]=" 12345678 "
agenda [" Emily "]=" 87654321 "
agenda [" Steve "]=" 56789121 "
agenda [" Patrick "]=" 78901234 "
agenda["payal"] = "914502"
agenda['new'] = j
agenda["new"]= k


print ( agenda )

print(agenda.items())

print(agenda.keys())


agenda.pop('new')
print("after popping", agenda)


new_dict = {"hkjhkjhjk":"dfsdfsdfsdf"}
agenda.update(new_dict) #joining  two dicts
print(agenda)

del agenda["payal"]
print(agenda)

agenda.clear()
print(agenda)

agenda [" Mary "] = [" 12345678 ", " mary . brown@gmail .com"]
agenda [" Emily "] = [" 87654321 ", " emily . andersen@hotmail .com "]
agenda [" Steve "] = [" 56789121 ", " steve . jackson@gmail .com"]
agenda [" Patrick "] = [" 78901234 ", " patrick . smith@gmail .com "]
print ( agenda )

print(agenda[" Mary "][0])

for key in agenda:
    print("key>", agenda[key][:])
    print("key>", agenda[key][0], agenda[key][1])

agenda[" Mary "][0] = "9696876876876"
print(agenda.items())

new_phone= "8093859385983"
agenda[" Emily "].append(new_phone)
print(agenda[" Emily "])

dense_matrix = [ [0 ,0 ,0 ,1 ,0 ,0 ,0 ,4 ,0 ,4] , [0 ,0 ,0 ,0 ,0 ,0 ,0 ,4 ,4 ,0] ,
[0 ,2 ,0 ,0 ,0 ,0 ,4 ,0 ,3 ,0] , [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0] ,
[0 ,0 ,0 ,3 ,0 ,5 ,8 ,2 ,0 ,5] ]

print(dense_matrix)

sparse_matrix = {}
for i in range (5): # we use range because we must loop 5 times
    for j in range (10): #we use range because we must loop 10 times
        if dense_matrix [i][j] != 0:
            key = (i, j)
            value = dense_matrix [i][j]
            sparse_matrix [ key] = value
print ( sparse_matrix )