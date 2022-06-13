# 3-5 단순하게 풀기
n, k = map(int, input('두개의 수').split())
result = 0
# n 이 k 이상이면
while n >= k:
    # n이 k로 나누어 떨어지지 않으면 n에서 1 빼기
    while n % k != 0:
        print(n%k)
        n -= 1
        result += 1
        print('나누기 결과 (몫) 2 번째 while',n, 'result :', result)
    n //= k    
    result += 1
    print('나누기 결과 (몫)',n, 'result :', result)
# 마지막으로 남은 수에 대해서 1씩 뺴기
print(n)
while n >1:
    n -= 1
    result += 1
    print('나누기 결과 (몫) 3-while',n, 'result :', result)
print(result)            