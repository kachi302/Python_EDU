# 학생수 입력 받기 (N)
n = int(input('학생수 : '))
# n 명의 학생정보 입력받아서 리스트에 저장
array=[]
for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환해서 저장
    array.append((input_data[0], int(input_data[1])))
    
    
# 키(Key) 를 이용하여 점수를 기준으로 정렬
array = sorted(array, key=lambda student: student[1])

# 정렬된 결과를 출력
for student in array:
    print(student[0], end=' ')
       