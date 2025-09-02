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
    for i in range(1, len(arr)):
        for j in range(i-1, -1, -1):
            # i is target index and, j is 
            if arr[i] >= arr[j]:
                temp = arr[i]
                arr[]
