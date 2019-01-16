def isPossible(A,n,target):
    dp = [[False for j in range(target+1)] for i in range(3)]
    
    for i in range(n+1):
        for j in range(target + 1):
            if j == 0:
                dp[i%2][j] = True
            elif i == 0:
                dp[i%2][j] = False
            elif A[i-1] <= j:
                dp[i % 2][j] = dp[(i + 1) % 2][j - A[i - 1]] or dp[(i + 1) % 2][j]
            else:
                dp[i % 2][j] =dp[(i + 1) % 2][j]
            
    return dp[i%2][target]
            
            
for _ in xrange(input()):
    A = map(int, raw_input().split())
    n = A[0]
    target = int(raw_input())
    if isPossible(A[1:],n,target):
        print "YES"
    else:
        print "NO"
    