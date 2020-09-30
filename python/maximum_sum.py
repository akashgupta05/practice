def get_max_sum(arr, arr_length):
    pivot_item = arr[arr_length - 1]
    total_sum = pivot_item
    for i in range(arr_length-2, -1, -1):
        if arr[i] > pivot_item:
            total_sum += pivot_item
            continue
        
        total_sum += arr[i]
        pivot_item = arr[i]
            
    return total_sum 
 
def main():
    test_cases = int(raw_input())
    for _ in range(test_cases):
        arr_length = int(raw_input())
        arr = map(int, raw_input().split())
        print get_max_sum(arr, arr_length)
 
if __name__ == '__main__':
    main()
