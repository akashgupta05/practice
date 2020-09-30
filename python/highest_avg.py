def searchKPosition (arr, i, j, k):
	if j >= i:
		mid = i + (j - i)/2
		if arr[mid] == k:
			return mid
		elif arr[mid] > k:
			if mid > 0 and arr[mid-1] < k:
				return mid
			else:
				return searchKPosition(arr, i, mid-1, k)
		elif arr[mid] < k:
			if mid < len(arr)-1 and arr[mid+1] > k:
				return mid
			else:
				return searchKPosition(arr, mid+1, j, k)
	else:
		return -1

def main():
	n = int(raw_input())
	a = map(int, raw_input().split())
	arr = sorted(a)
	avg_arr = []
	sum_arr = 0;
	for i in range(0,len(arr)):
		sum_arr += arr[i]
		avg_arr.append(sum_arr/(i+1))
		
	for _ in xrange(input()):
		k = int(raw_input())
		if k in avg_arr:
			print avg_arr.index(k)
		elif k <= avg_arr[0]:
			print 0
		elif k >= avg_arr[len(avg_arr)-1]:
			print n
		else:
			print searchKPosition(avg_arr,0,n,k)
    
    
 
if __name__ == '__main__':
    main()