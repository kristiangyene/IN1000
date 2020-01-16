#a)
def trimZeros(a):
    while(a[0] == 0):
        a.pop(0)
    while(a[-1] == 0):
        a.pop(-1)
    return a


print(trimZeros([0,0,8,0,1,2,0,3,0,0,4,0,0]))


#b)
def telling(string):
    list = []
    for bokstav in string:
        if bokstav not in list:
            list.append(bokstav)
    return len(list)

print(telling("accag"))
