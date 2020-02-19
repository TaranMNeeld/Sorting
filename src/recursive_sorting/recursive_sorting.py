from itertools import accumulate

# TO-DO: complete the helper function below to merge 2 sorted arrays

test_arr = [1, 9, 2, 3, 4, 0, 1, 1, 4, 6, 7, 8, 8, 9, 9, 6, 6, 8, 8, 9, 5]
test_arr1 = [1, 2, 3, 4, 5]
test_arr2 = [3, 4, 5, 6, 7]


def merge(arr1, arr2):
    # Length of both array args put together
    elements = len(arr1) + len(arr2)

    # A default array with the same length as both array args put together
    merged_arr = [0] * elements

    # With the arrays already being sorted, I can insert 1 array into the other at the correct position
    for i in range(len(merged_arr)):
        if len(arr1) == 0 or len(arr2) == 0:
            print(merged_arr[:i] + arr1 + arr2)
            return merged_arr[:i] + arr1 + arr2
        elif arr1[0] > arr2[0]:
            merged_arr[i] = arr2.pop(0)
        else:
            merged_arr[i] = arr1.pop(0)


# merge(test_arr1, test_arr2)
# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    if len(arr) > 1:
        first_half = merge_sort(arr[:len(arr) // 2])
        second_half = merge_sort(arr[len(arr) // 2:])
        return merge(first_half, second_half)

    return arr


merge_sort(test_arr)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    return arr
