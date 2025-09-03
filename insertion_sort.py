def insertion_sort(arr:list)->list:
    '''Sort the array in ascending order.

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
    >> print(insertion_sort(arr))
    [1, 2, 3, 4, 5, 6]
    '''
    sorted_arr = arr[:]
    for i in range(1, len(sorted_arr)):
        for j in range(i-1, -1, -1):
            # i is target index and, j is 
            if sorted_arr[i] >= sorted_arr[j]:
                # move sorted_arr[j+1:i] to [j+2:i+1]
                # i goto j+1
                temp = sorted_arr[i]
                # for k in range(i, j, -1):
                #     sorted_arr[k] = arr[k-1]
                sorted_arr[j+2:i+1] = sorted_arr[j+1:i]
                sorted_arr[j+1] = temp
                break
    return sorted_arr
