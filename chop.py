#---------IMPORTS---------------
from timeit import timeit
"Module: timeit used for execution measurement in 'Work' section"
"Module: functools, time used for execution measurement with decorators"
"       Note: ^ commented out because timeit works better, leaving it in because it's another way to do it and it's a good example of decorators"
#import functools, time
#---------IMPORTS---------------
#---------Tests-----------------
#def timing(f):
    # @functools.wraps(f)
    # def wrap(*args):
    #     time1 = time.time()
    #     ret = f(*args)
    #     time2 = time.time()
    #     print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
    #     return ret
    # return wrap

#@timing
def chop_test():
    "Test for method 1 of the 'chop' problem kata"
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

#@timing
def chop2_test():
    "Test for method 2 of the 'chop' problem kata"
    assert chop2(3, []) == -1
    assert chop2(3, [1]) == -1
    assert chop2(1, [1]) == 0
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
    assert chop2(0, [1, 3, 5, 7]) == -1
    assert chop2(2, [1, 3, 5, 7]) == -1
    assert chop2(4, [1, 3, 5, 7]) == -1
    assert chop2(6, [1, 3, 5, 7]) == -1
    assert chop2(8, [1, 3, 5, 7]) == -1
    return "chop2 Passed!"

#@timing
def chop3_test():
    "Test for method 3 of the 'chop' problem kata"
    assert chop3(3, []) == -1
    assert chop3(3, [1]) == -1
    assert chop3(1, [1]) == 0
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
    assert chop3(0, [1, 3, 5, 7]) == -1
    assert chop3(2, [1, 3, 5, 7]) == -1
    assert chop3(4, [1, 3, 5, 7]) == -1
    assert chop3(6, [1, 3, 5, 7]) == -1
    assert chop3(8, [1, 3, 5, 7]) == -1
    return "chop3 Passed!"

#@timing
def chop4_test():
    "Test for method 4 of the 'chop' problem kata"
    assert chop4(3, []) == -1
    assert chop4(3, [1]) == -1
    assert chop4(1, [1]) == 0
    assert chop4(1, [1, 3, 5]) == 0
    assert chop4(3, [1, 3, 5]) == 1
    assert chop4(5, [1, 3, 5]) == 2
    assert chop4(0, [1, 3, 5]) == -1
    assert chop4(2, [1, 3, 5]) == -1
    assert chop4(4, [1, 3, 5]) == -1
    assert chop4(6, [1, 3, 5]) == -1
    assert chop4(1, [1, 3, 5, 7]) == 0
    assert chop4(3, [1, 3, 5, 7]) == 1
    assert chop4(5, [1, 3, 5, 7]) == 2
    assert chop4(7, [1, 3, 5, 7]) == 3
    assert chop4(0, [1, 3, 5, 7]) == -1
    assert chop4(2, [1, 3, 5, 7]) == -1
    assert chop4(4, [1, 3, 5, 7]) == -1
    assert chop4(6, [1, 3, 5, 7]) == -1
    assert chop4(8, [1, 3, 5, 7]) == -1
    return "chop4 Passed!"

def chop5_test():
    "Test for method 5 of the 'chop' problem kata"
    assert chop5(3, []) == -1
    assert chop5(3, [1]) == -1
    assert chop5(1, [1]) == 0
    assert chop5(1, [1, 3, 5]) == 0
    assert chop5(3, [1, 3, 5]) == 1
    assert chop5(5, [1, 3, 5]) == 2
    assert chop5(0, [1, 3, 5]) == -1
    assert chop5(2, [1, 3, 5]) == -1
    assert chop5(4, [1, 3, 5]) == -1
    assert chop5(6, [1, 3, 5]) == -1
    assert chop5(1, [1, 3, 5, 7]) == 0
    assert chop5(3, [1, 3, 5, 7]) == 1
    assert chop5(5, [1, 3, 5, 7]) == 2
    assert chop5(7, [1, 3, 5, 7]) == 3
    assert chop5(0, [1, 3, 5, 7]) == -1
    assert chop5(2, [1, 3, 5, 7]) == -1
    assert chop5(4, [1, 3, 5, 7]) == -1
    assert chop5(6, [1, 3, 5, 7]) == -1
    assert chop5(8, [1, 3, 5, 7]) == -1
    return "chop5 Passed!"

#---------Tests-----------------

#---------Functions-------------
#@timing
def chop(int, list_of_int):
    if type(int).__name__ != 'int':
        raise TypeError("Value must be an integer.")
    if type(list_of_int).__name__ != "list":
        raise TypeError("Value of 'list' must be of type: list.")
    if int in list_of_int:
        return list_of_int.index(int)
    return -1

chop2 = lambda integer, list_of_int: list_of_int.index(integer) if integer in list_of_int else -1

#@timing
def chop3(integer, list_of_int):
    result = -1
    for index in range(len(list_of_int)):
        if list_of_int[index] == integer:
            result = index
            break
        else:
            continue
    return result

#@timing
def chop4(integer,list_of_int):
    if isinstance(integer,int) and isinstance(list_of_int,list):
        int_dict = {}
        for index in range(len(list_of_int)):
            dset = {list_of_int[index]:index}
            int_dict.update(dset)
        try:
            return int_dict[integer]
        except Exception:
            return -1

def chop5(integer, list_of_int):
    integer = int(integer)
    list_of_int = list(list_of_int)
    for count, item in enumerate(list_of_int):
        if item is integer:
            return count
        else:
            continue
    return -1

#---------Functions-------------
#---------Work------------------
print(chop_test())
print(chop2_test())
print(chop3_test())
print(chop4_test())
print(chop5_test())
print(timeit(lambda: chop_test(), number=1000))
print(timeit(lambda: chop2_test(), number=1000))
print(timeit(lambda: chop3_test(), number=1000))
print(timeit(lambda: chop4_test(), number=1000))
print(timeit(lambda: chop5_test(), number=1000))
#---------Work------------------
