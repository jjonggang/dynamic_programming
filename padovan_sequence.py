#-*- coding:utf-8 -*-
# 1 2 3 4 5 6 7 8 9 10 11
# 1 1 1 2 2 3 4 5 7 9  12
# dp[n+3] = dp[n] + dp[n+1]

dp = [0]*101
dp[1], dp[2], dp[3] = 1,1,1
for index in range(1, 98):
    dp[index+3] = dp[index] + dp[index+1]

n = int(input())
for i in range(n):
    m = int(input())
    print(dp[m]) # m번째 인덱스 값을 출력해라.