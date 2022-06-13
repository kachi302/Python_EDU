n, k = map(int, input('입력 수 ').split())
a = list(map(int, input('배열1').split()))
b = list(map(int, input('배열2').split()))

# 배열 A는 오름차순으로 정렬
a.sort()
# 배열 B는 내림차순으로 정렬
b.sort(reverse=True)
#첫번째 인덱스부터 확인하며, 두배열의 원소를 최대 K 번비교
for i in range(k):
    if a[i]<b[i]:
        #두원소 교체
        a[i], b[i] = b[i], a[i]
    else:   #a의 원소가 b의 원소 보다 크면 탈출
        break
print(sum(a))        
