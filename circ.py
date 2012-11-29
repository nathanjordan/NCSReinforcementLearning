import math
vals= []
for x in range(1,150):
    vals.append(math.sqrt(1.-((float(x)/150)**2)))

x = vals[::-1]

vals[:0] = x

print vals
print len(vals)
f = open("stim.txt", 'w')
for i in range(100):
    for col in range(100):
        f.write(".08 ")
    f.write('\n')
for p in vals:
    for j in range(100):
        f.write(str(p) + ' ')
    f.write('\n')
for i in range(101):
    for j in range(100):
        f.write(".08 ")
    f.write('\n')
f.close