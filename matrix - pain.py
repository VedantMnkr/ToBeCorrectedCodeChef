# Problem Code: MATPAIN80 on code chef




t = int(input())

MOD = 10**9+ 7

for i in range(t):
    # take input
    N, M, K = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    
    # initialize arrays and prefix sums
    row = [1] * N
    col = [1] * M
    prefix_row = [[0] * (M+1) for i in range(N)]
    prefix_col = [[0] * (N+1) for i in range(M)]
    
    for i in range(N):
        for j in range(M):
            prefix_row[j][i+1] = prefix_row[j][i] + A[i][j]
            prefix_col[i][j+1] = prefix_col[i][j] + A[i][j]
    
    # perform operations
    for i in range(K):
        Q, X, V = map(int, input().split())
        if Q == 0:
            row[X-1] = (row[X-1] * V) % MOD
        elif Q == 1:
            col[X-1] = (col[X-1] * V) % MOD
    
    # calculate sum
    total = 0
    for i in range(N):
        for j in range(M):
            total = (total + A[i][j] * row[i] * col[j]) % MOD
    print(total)
    
