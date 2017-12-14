def wrap_slice(list_, position, size):
    if position + size > len(list_):
        return list_[position:] + list_[:(position + size) % len(list_)]
    return list_[position:position + size]


def knot_hash(input_string):

    list_ = [x for x in range(256)]
    size = len(list_)
    lengths = [ord(x) for x in input_string]
    lengths.extend([17, 31, 73, 47, 23])
    position = 0
    skip = 0

    # do this 64 times now
    for x in range(64):
        for length in lengths:
            # first, reverse length
            sublist = wrap_slice(list_, position, length)
            sublist.reverse()
            for i in range(len(sublist)):
                list_[(position+i)%size] = sublist[i]
            # move position forward...
            position = (position+length+skip)%size
            skip += 1

    # generate dense hash

    hash_array = []
    val = 0

    for x in range(16):
        to_hash = list_[:16]
        val = 0
        for y in to_hash:
            val = val ^ y
        hash_array.append(val)
        list_ = list_[16:]

    # convert to hex string

    hash_string = ""
    for x in hash_array:
        no_pad = hex(x)[2:]
        if len(no_pad) == 1:
            no_pad = "0" + no_pad
        hash_string += no_pad

    return hash_string
