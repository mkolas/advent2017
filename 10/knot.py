list_ = [x for x in range(256)]
size = len(list_)
lengths = [183,0,31,146,254,240,223,150,2,206,161,1,255,232,199,88]
position = 0
skip = 0

def wrap_slice(list_, position, size):
    if position + size > len(list_):
        return list_[position:] + list_[:(position+size)%len(list_)]
    return list_[position:position+size]

for length in lengths:
    # first, reverse length
    sublist = wrap_slice(list_, position, length)
    sublist.reverse()
    for i in range(len(sublist)):
        list_[(position+i)%size] = sublist[i]
    # move position forward...
    position = (position+length+skip)%size
    skip += 1

print("multiplication of first two values: {}".format(list_[0]*list_[1]))
