
def main():
    memo = [0]*10**7
    chec = [False]*10**7
    t = int(raw_input())
    A = map(int, raw_input().split())
    for n in A:
        memo[1] = 1
        if n & 1 == 0:
            n -= 1
        if memo[n] != 0:
            print memo[n]
        else:
            for i in range(1,n+1,2):
                if memo[i] == 0:
                    a = "{0:b}".format(i)
                    st = str(i)
                    if a == a[::-1] and st == st[::-1]:
                        memo[i] = memo[i-2] +1
                    else:
                        memo[i] = memo[i-2]
            print memo[n]            

if __name__ == '__main__':
    main()
