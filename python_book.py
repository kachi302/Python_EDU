# 그리디 알고리즘
# n = 1260
# count = 0
# coins_type = [500, 100, 50, 10]
# for coin in coins_type:
#     count += n // coin
#     n %= coin
#     print(coin, count, n)
# print(count)   

# # n, m ,k 를 공백으로 구분해서 입력 , n: 전체 입력 갯수, m: 반복 횟수, k: 더하기 횟수
# n, m, k = map(int, input().split())
# # n 의 입력 수
# data = list(map(int, input().split()))

# data.sort() # 입력수 sort
# first = data[n -1]  #max value
# second = data[n - 2]    #second max

# result = 0
# while True:
#     for i in range(k):
#         #가장 큰수를 k 번 더하기 
#         if m == 0:
#             break
#         result += first
#         m -= 1      #더할때 마다 1씩 빼기
#     if m == 0:
#         break
#     result += second
#     m -= 1
# print(result)    

# n, m, k = map(int, input().split())
# data = list(map(int,input().split()))

# data.sort()
# first = data[n - 1]
# second = data[n - 2]

# #가장 큰수 더해지는 횟수 계산
# # m / ( K + 1)  -- 수열이 반복되는 수열 횟수, K+1 반복 수열의 길이
# count = int( m / (k + 1)) * k
# print(m / (k + 1), count)
# count += m % (k + 1)
# print(m % (k + 1), count)
# result = 0
# result += (count) * first
# result += (m - count) * second
# print(result) 
        
# 리스트 컴프리헨션
n = [i*2 for i in range(1,10)]
print(n)
m = [i for i in range(1, 20) if i % 2 == 0]
print(m)
m = 5
n = 5
k = [[0]*m for _ in range(n)]
print(k)        