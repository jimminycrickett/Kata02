def chop_test():
    assert chop(3, []) == -1
    assert chop(3, [1]) == -1
    assert chop(1, [1]) == 0
    assert chop(1, [1, 3, 5]) == 0
    assert chop(3, [1, 3, 5]) == 1
    assert chop(5, [1, 3, 5]) == 2
    assert chop(0, [1, 3, 5]) == -1
    assert chop(2, [1, 3, 5]) == -1
    assert chop(4, [1, 3, 5]) == -1
    assert chop(6, [1, 3, 5]) == -1
    assert chop(1, [1, 3, 5, 7]) == 0
    assert chop(3, [1, 3, 5, 7]) == 1
    assert chop(5, [1, 3, 5, 7]) == 2
    assert chop(7, [1, 3, 5, 7]) == 3
    assert chop(0, [1, 3, 5, 7]) == -1
    assert chop(2, [1, 3, 5, 7]) == -1
    assert chop(4, [1, 3, 5, 7]) == -1
    assert chop(6, [1, 3, 5, 7]) == -1
    assert chop(8, [1, 3, 5, 7]) == -1
    return "chop Passed!"

def chop2_test():
    assert chop2(3,[]) == -1
    assert chop2(3,[1]) == -1
    assert chop2(1,[1]) == 0
    assert chop2(1, [1, 3, 5]) == 0
    assert chop2(3, [1, 3, 5]) == 1
    assert chop2(5, [1, 3, 5]) == 2
    assert chop2(0, [1, 3, 5]) == -1
    assert chop2(2, [1, 3, 5]) == -1
    assert chop2(4, [1, 3, 5]) == -1
    assert chop2(6, [1, 3, 5]) == -1
    assert chop2(1, [1, 3, 5, 7]) == 0
    assert chop2(3, [1, 3, 5, 7]) == 1
    assert chop2(5, [1, 3, 5, 7]) == 2
    assert chop2(7, [1, 3, 5, 7]) == 3
    assert chop2(0, [1, 3, 5, 7])== -1
    assert chop2(2, [1, 3, 5, 7])== -1
    assert chop2(4, [1, 3, 5, 7])== -1
    assert chop2(6, [1, 3, 5, 7])== -1
    assert chop2(8, [1, 3, 5, 7])== -1
    return "chop2 Passed!"

def chop3_test():
    assert chop3(3,[]) == -1
    assert chop3(3,[1]) == -1
    assert chop3(1,[1]) == 0
    assert chop3(1, [1, 3, 5]) == 0
    assert chop3(3, [1, 3, 5]) == 1
    assert chop3(5, [1, 3, 5]) == 2
    assert chop3(0, [1, 3, 5]) == -1
    assert chop3(2, [1, 3, 5]) == -1
    assert chop3(4, [1, 3, 5]) == -1
    assert chop3(6, [1, 3, 5]) == -1
    assert chop3(1, [1, 3, 5, 7]) == 0
    assert chop3(3, [1, 3, 5, 7]) == 1
    assert chop3(5, [1, 3, 5, 7]) == 2
    assert chop3(7, [1, 3, 5, 7]) == 3
    assert chop3(0, [1, 3, 5, 7])== -1
    assert chop3(2, [1, 3, 5, 7])== -1
    assert chop3(4, [1, 3, 5, 7])== -1
    assert chop3(6, [1, 3, 5, 7])== -1
    assert chop3(8, [1, 3, 5, 7])== -1
    return "chop3 Passed!"

def chop(int, list_of_int):
    if type(int).__name__ != 'int':
        raise TypeError("Value must be an integer.")
    if type(list_of_int).__name__ != "list":
        raise TypeError("Value of 'list' must be of type: list.")
    if int in list_of_int:
        return list_of_int.index(int)
    else:
        return -1

chop2 = lambda int, list_of_int: list_of_int.index(int) if int in list_of_int else -1

def chop3(integer, list_of_int):
    result = -1
    for index in range(len(list_of_int)):
        if list_of_int[index] == integer:
            result = index
            break
        else:
            continue
    return result

print(chop_test())
print(chop2_test())
print(chop3_test())


