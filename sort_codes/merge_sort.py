def merge_sort(arr:list)->list:
    '''Sort the array in ascending order with merge sort.

    Parameters
    ----------
    arr : list
        list to sort
    
    Returns
    -------
    sorted_arr : list
        list has been sorted
    
    Example
    -------
    >> arr = [3, 6, 1, 2, 5, 4]
    >> print(merge_sort(arr))
    [1, 2, 3, 4, 5, 6]
    '''
    if len(arr) > 2:
        # seperate given array to two parts, and sort by using recursion
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        sorted_left_arr = merge_sort(left_arr)
        sorted_right_arr = merge_sort(right_arr)

        merged_arr = [None for _ in range(len(arr))]
        left_idx, right_idx, merged_idx = 0, 0, 0
        left_len, right_len = len(left_arr), len(right_arr)

        # finish at left or right index is reach end of array
        while left_idx < left_len and right_idx < right_len:
            if sorted_left_arr[left_idx] < sorted_right_arr[right_idx]:
                merged_arr[merged_idx] = sorted_left_arr[left_idx]
                left_idx += 1
            else:
                merged_arr[merged_idx] = sorted_right_arr[right_idx]
                right_idx += 1
            merged_idx += 1
        # add rest array's elements to merged array
        if left_idx == left_len:
            merged_arr[merged_idx:] = sorted_right_arr[right_idx:]
        elif right_idx == right_len:
            merged_arr[merged_idx:] = sorted_left_arr[left_idx:]
        else:
            exit(2)

        return merged_arr
    # compare each array and return sorted array
    elif len(arr) == 2:
        if arr[0] <= arr[1]:
            return arr[:]
        else:
            return arr[::-1]
    # if array's lenth is 1, return itself
    elif len(arr) == 1:
        return arr[:]
    
    else:
        exit(1)

if __name__ == "__main__":
    print("run example code")

    arr = [4, 5, 9, 3, 1, 8, 2, 7, 0, 6]
    print(merge_sort(arr=arr))
