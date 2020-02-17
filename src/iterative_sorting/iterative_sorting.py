# TO-DO: Complete the selection_sort() function below

test_arr = [5, 4, 1, 7, 8, 0, 2, 3, 9, 6]

def selection_sort( arr ):
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
                print(arr)
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr