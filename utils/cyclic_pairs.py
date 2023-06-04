def rotate_string(s, n):
    return s[n:] + s[:n]


def get_cyclic_pairs(n):
    all_pairs = getAllBinaryStrings(n)
    cyclic_pairs = []
    for i in range(0, len(all_pairs)):
        s = all_pairs[i]
        print(s)
        unique = True
        for j in range(n):
            s2 = rotate_string(s, j+1)
            if s2 in cyclic_pairs:
                print('rep')
                unique = False
                break
        if unique:
            #print(s)
            cyclic_pairs.append(s)
    return cyclic_pairs


def getAllBinaryStrings(n):
    arr_ret = []
    getAllBinaryStringsRec(n, [None]*n, 0, arr_ret)
    return arr_ret


def getAllBinaryStringsRec(n, arr, i, arr_ret):
    # Stop case
    if i == n:
        #print(''.join(map(str, arr)))
        arr_ret.append(''.join(map(str, arr)))
        return

    # First assign 0 and try every permutation
    arr[i] = 0
    getAllBinaryStringsRec(n, arr, i + 1, arr_ret)

    # Try 1
    arr[i] = 1
    getAllBinaryStringsRec(n, arr, i + 1, arr_ret)
