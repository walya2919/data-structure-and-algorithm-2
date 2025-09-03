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
    # i is target idx, j is dest idx
    # move arr[i] to arr[j]
    # and shift right every element arr[j:i]
    for i in range(1, len(sorted_arr)):
        for j in range(i-1, -1, -1):
            if sorted_arr[i] >= sorted_arr[j]:
                j += 1
                break
        
        temp = sorted_arr[i]
        sorted_arr[j+1:i+1] = sorted_arr[j:i]
        sorted_arr[j] = temp
        
    return sorted_arr

if __name__ == "__main__":
    print("run example code")

    arr = [4, 5, 9, 3, 1, 8, 2, 7, 0, 6]
    print(insertion_sort(arr=arr))
