def funk(para1, para2, para3):
    liste = []
    liste.append(float(para1))
    liste.append(float(para2))
    liste.append(float(para3))
    minst = liste[0]
    for e in liste:
        if e < minst:
            minst = e
    return minst

print(funk(2.5, 0.3, 4.2))
