# stack sample
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
print(stack)
stack.pop()
#최하단 원소부터 출력
print(stack)
# 최상단 원소부터 출력
print(stack[::-1])