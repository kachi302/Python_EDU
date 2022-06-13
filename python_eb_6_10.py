# N을 입력받기
n = int(input('입력 수의 갯수는 ? '))
#N 개의 정수를 입력 받아 리스트에 저장
array = []
for i in range(n):
    array.append(int(input(' 수 :')))
#파이썬 기본 정렬 라이브러리를 이용해서 정렬 수행
array = sorted(array, reverse=True)    

# 정렬이 수행된 경과를 출력
for i in array:
    print(i, end='')