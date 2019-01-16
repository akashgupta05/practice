def mystery(alist):
    for index in range(1, len(alist)):
    	pos = index
    	current = alist[index]
    	while pos > 0 and alist[pos-1] > current:
    	    alist[pos] = alist[pos-1]
    	    pos = pos - 1
    	alist[pos] = current
    print alist
    
mystery([1,3,5,2,6,3,9,8])
