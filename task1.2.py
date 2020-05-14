letters = 'SAUMesh'
l2 = []
l3 = []
for i in letters:
    if i.islower():
        l2.append(i)
    else:
        l3.append(i)

p = l2 + l3
s = ''
s = s.join(p)
print(s)
        