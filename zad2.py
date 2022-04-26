def same_parity(a, b):
    return a % 2 == b % 2

assert same_parity(0,0) and same_parity(1,1) and not same_parity(1, 0)

def atypical_compare(a, b):
    if same_parity(a, b):
        return a < b if a % 2 == 1 else a > b
    return a % 2 > b % 2

assert atypical_compare(0, 5) is False
assert atypical_compare(5, 0) is True
assert atypical_compare(4, 6) is False


def atypical_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            # if arr[min_idx] > arr[j]:
            if atypical_compare(arr[j], arr[min_idx]):
                min_idx = j      
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

numbers = [1, 2, 3, 4, 5, 6]
atypical_sort(numbers)
assert numbers == [1, 3, 5, 6, 4, 2]

numbers = [1, 1, 1, 4, 5, 6]
atypical_sort(numbers)
assert numbers == [1, 1, 1, 5, 6, 4]



if __name__ == '__main__':
    print(atypical_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

