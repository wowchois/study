# b되기 위한 최솟값 0
# ba되기 위한 최솟값 b/a(b없음->0), ba -> 1
# ban되기 위한 최솟값 b/a/n(b없음->0), ba/n -> 2, ban -> 0
# bana되기 위한 최솟값 ba/na -> 2, ban(2)/a(1) -> 3
# 반복
def solution(strs, t):
    answer = 0
    dp = [0] * (len(t)+1)
    strs = set(strs)
    
    for i in range(1,len(t)+1):
        dp[i] = float('inf')
        for j in range(1,min(i+1,6)):
            print(i-j,i,j,min(i+1,6))
            print(t[i-j:i])
            print(dp[i],dp[i-j])
            if t[i-j:i] in strs:
                print('--',min(dp[i],dp[i-j]+1))
                dp[i] = min(dp[i],dp[i-j]+1)

    return -1 if dp[-1] == float('inf') else dp[-1]
