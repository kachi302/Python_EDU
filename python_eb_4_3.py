# 현재 나이트의 위치 입력 받기
input_data = input()
row = int(input_data[1])
# ord : unicode 변환
print('input data =', input_data,'  ', ord(input_data[0]), ' row =', row)
column = int(ord(input_data[0])) - int(ord('a'))+1
print('int(ord(input_data[0]))', int(ord(input_data[0])), 'int(ord(''a''))', int(ord('a')), column)

#나이트가 이동할수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

#8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    #이동 하고자 하는 위치 확인
    print('step : ', step,' step[0] ' ,' step[0]',step[0],' step[1]=',step[1])
    next_row = row + step[0]   
    next_column = column + step[1]
    print('next_row =',next_row,'row : ',row,  'next_column=', next_column,' column :', column )
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <=8 and next_column >=1 and next_column <=8:
        print(' in ','next_row =',next_row,' next_column=', next_column)
        result += 1
print(result)        