def load_data():
    with open("dane.txt", "r", encoding="utf-8") as f:
        return f.read().rstrip().split('\n')


def compare_alphabetically(left, right):
    return left < right

def compare_by_length(left, right):
    return len(left) < len(right)


def _merge_sort(arr, compare):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        _merge_sort(L, compare)
        _merge_sort(R, compare)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if compare(L[i], R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def merge_sort(arr, compare):
    _merge_sort(arr, compare)
    return arr
    


assert compare_alphabetically('a', 'b') == True
assert compare_by_length('aaaa', 'bddddddd') == True
assert merge_sort(['bb', 'aaa', 'c'], compare_alphabetically) == ['aaa', 'bb', 'c']
assert merge_sort(['bb', 'aaa', 'c'], compare_by_length) == ['c','bb','aaa']


if __name__ == '__main__':
    data = load_data()
    print("Sorting alphabetically:")
    print(merge_sort(data, compare_alphabetically))
    # print(merge_sort(data, lambda a, b: a < b))
    print("Sorting by length:")
    print(merge_sort(data, compare_by_length))
    # print(merge_sort(data, lambda a, b: len(a) < len(b)))

