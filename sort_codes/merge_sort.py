def merge_sort(arr:list)->list:
    if len(arr) > 2:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        sorted_left_arr = merge_sort(left_arr)
        sorted_right_arr = merge_sort(right_arr)

        merged_arr = [None for _ in range(len(arr))]
        left_idx, right_idx, merged_idx = 0, 0, 0
        left_len, right_len = len(left_arr), len(right_arr)

        while left_idx < left_len and right_idx < right_len:
            if sorted_left_arr[left_idx] < sorted_right_arr[right_idx]:
                merged_arr[merged_idx] = sorted_left_arr[left_idx]
                left_idx += 1
            else:
                merged_arr[merged_idx] = sorted_right_arr[right_idx]
                right_idx += 1
            merged_idx += 1

        if left_idx == left_len:
            merged_arr[merged_idx:] = sorted_right_arr[right_idx:]
        elif right_idx == right_len:
            merged_arr[merged_idx:] = sorted_left_arr[left_idx:]
        else:
            exit(2)

        return merged_arr
    
    elif len(arr) == 2:
        if arr[0] <= arr[1]:
            return arr[:]
        else:
            return arr[::-1]
        
    elif len(arr) == 1:
        return arr[:]
    
    else:
        exit(1)