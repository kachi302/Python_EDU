# 선택 정렬 소스
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(array)):
    min_index = i   #가장 작은 원소의 Index
    print('min_index : ', min_index)
    for j in range(i + 1, len(array)):
        print('j :', j)
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 스와프
print(array)