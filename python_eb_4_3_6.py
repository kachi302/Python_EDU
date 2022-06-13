# n, k 를 공백으로 받기
n, k = map(int, input('2 수').split())
result = 0
while True:
    # n == k 로 나누어 떨어질때 까지 1씩 뺴기
    target = (n // k) * k
    print('target',target)
    result += (n - target)
        
    n = target
    print('n 값',n, 'target',target)
    # n 이 k 보다 작을때(더이상 나눌수 없을때, 반복문 탈출)
    if n < k:
        break
    #k 로 나누기
    result += 1
    n //= k
    print(n)
# 마지막으로 남은 수에 대하여 1씩 뺴기
result += (n-1)
print(result)   