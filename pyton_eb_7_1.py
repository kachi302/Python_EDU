# 순차 탐색 소스 코드
def sequential_search(n, target, array):
    #각 원소를 하나씩 확인하며,
    for i in range(n):
        #현재의 원소가 찾고자 하는 원소와 동일할 경우
        if array[i] == target:
            return i + 1 # 현재 위치 반환 (index 는 0부터 시작 하므로 1 더하기)

print('생성할 원소의 갯수를 입력한 다음 한칸 띄고 찾을 문자열 입력하세요')
input_data = input().split()
n = int(input_data[0])  #원소의 갯수
target = input_data[1]  #찾고자 하는 문자열 

print("앞서 적은 원소 갯수만큼 문자열을 입력하세요, 구분은 한칸 띄어쓰기...")
array = input().split()

# 순차 탐색 결과
print(sequential_search(n, target, array))       