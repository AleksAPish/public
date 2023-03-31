array = [int(x) for x in input("Введите целые числа от 0 до 100 через пробел: ").split()]

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

array = sort(array)
print(array)

a = int(input("Введите любое число из списка: "))

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