array = []
def check():
    global array
    count = 0
    for i in array:
        if i < 1:
            print('Вы ввели число меньше 1')
            return create()
        elif i > 100:
            print('Вы ввели число больше 100')
            return create()
        else:
            i += 1

def create():
    global array
    array = [int(x) for x in input("Введите положительные целые числа через пробел: ").split()]
    check()

create()

def sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = sort(array[:middle])
        right = sort(array[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

array2 = sort(array)
print(array2)

a = None

def check2():
    global a
    if a < min(array) or a > max(array):
        print("Данное число не входит в список!")
        create2()


def create2():
    global a
    a = int(input("Введите любое число из полученного списка: "))
    check2()

create2()

def binary_search(array, a, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == a:
        return middle
    elif a < array[middle]:
        return binary_search(array, a, left, middle - 1)
    else:
        return binary_search(array, a, middle + 1, right)

b = binary_search(array, a, 0, len(array) - 1)
print(b)