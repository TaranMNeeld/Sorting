from itertools import accumulate

# TO-DO: complete the helper function below to merge 2 sorted arrays

test_arr = [1, 9, 2, 3, 4, 0, 1, 1, 4, 6, 7, 8, 8, 9, 9, 6, 6, 8, 8, 9, 5]


def merge(arr1, arr2):

    # Length of both array args put together
    elements = len(arr1) + len(arr2)

    # A default array with the same length as both array args put together
    merged_arr = [0] * elements

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] > arr2[j]:
                merged_arr[]
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):

    if len(arr) > 1:
        first_half = merge_sort(arr[:len(arr)//2])
        second_half = merge_sort(arr[len(arr)//2:])
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
