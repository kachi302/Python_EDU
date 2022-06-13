#재귀 함수 호출
def recursive_function(i):
    #100 번쨰 출력 했을때 종료 
    if i == 100:
        return
    print(i, '번째 재귀 함수에서 ', i + 1,'번째 재귀 함수 호출입니다.')
    recursive_function(i+1)
    print(i, '번째 재귀 함수 호출을 종료 합니다.')    
recursive_function(1)    