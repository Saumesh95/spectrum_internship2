s1 = {1,2,3,4,5,6,7,8,9}
s2 = {1,3,4,6,8,11,22,34,51,67}

for i in list(s1):
    for j in list(s2):
        if i==j:
            s1.remove(i)
            l = set(s1)

print(l)
