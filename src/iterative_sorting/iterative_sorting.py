# TO-DO: Complete the selection_sort() function below

test_arr = [5, 4, 1, 7, 8, 0, 2, 3, 9, 6]


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(smallest_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                # TO-DO: swap
                arr[j], arr[smallest_index] = arr[smallest_index], arr[j]
                print(f'{arr}, swapped {arr[j]} with {arr[smallest_index]}')
    return arr


# TO-DO:  implement the Bubble Sort function below
swap_occurred = False


def bubble_sort(arr):
    print(arr)
    for i in range(0, len(arr) - 1):
        global swap_occurred
        swap_occurred = False
        for j in range(0, len(arr) - 1):
            first_index = j
            second_index = j + 1
            if arr[first_index] > arr[second_index]:
                arr[first_index], arr[second_index] = arr[second_index], arr[first_index]
                swap_occurred = True
                print(f'{arr}, swapped {arr[second_index]} with {arr[first_index]}')
        if not swap_occurred:
            pass
    return arr


selection_sort(test_arr)


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr
