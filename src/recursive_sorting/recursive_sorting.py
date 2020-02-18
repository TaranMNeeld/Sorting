# TO-DO: complete the helper function below to merge 2 sorted arrays

test_arr2 = [1, 2, 2, 3, 4, 0, 1, 1, 4, 6, 7, 8, 8, 9, 9, 6, 6, 8, 8, 9]


def merge(arr1, arr2):

    # Length of both array args put together
    elements = len(arr1) + len(arr2)

    # A default array with the same length as both array args put together
    merged_arr = [0] * elements

    # Add arr2 to the end of arr1
    arr1.extend(arr2)

    # While i >= 0 && i <= n - 1
    for i in range(len(merged_arr)):
        merged_arr[i] = arr1[i]

    merged_arr.sort()

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

    # Take 1 unsorted array

    # Split the array down to multiple arrays with 1 element

    # if length > 1, then sort arrays

    # pass 2 sorted arrays into merge(arr1, arr2)

    return arr


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
