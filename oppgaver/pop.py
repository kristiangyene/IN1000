def trimzeros(a):
    teller = 0
    while a[teller] == 0:
        a.pop(0)
    while a[teller - 1] == 0:
        a.pop(-1)
    return a


liste = [0,0,1,2,0,3,0,0,4,0,0]
print(trimzeros(liste))
