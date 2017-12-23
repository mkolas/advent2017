a = 1
d, e, f, g, h = 0, 0, 0, 0, 0
b = 93
c = b

if a == 1:
    b *= 100
    b += 100000
    c = b
    c += 17000

# while b != c:
#     for d in range(2, b):
#         for e in range(2, b):
#             if d * e == b:
#                 h += 1
#     b += 17

for x in range(b, c+1, 17):
    found = False
    for y in range(2, b):
        if x%y == 0:
            found = True
            break
    if found == True:
        h+= 1

print(h)