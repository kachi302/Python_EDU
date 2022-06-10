# fruits = {'apple', 'banna', 'orange'}
# fruits.add('mango')
# print(fruits)

# companies = set()
# companies = {'samsung', 'apple', 'google'}
# print(type(fruits), type(companies))

# print(fruits & companies, fruits | companies)

# aphapet = list('google')
# print(aphapet)
# print(set(aphapet))

dice1 = (1, 2, 3, 4, 5, 6)
dice2 = (2, 3, 5, 7, 11, 13)

sum_of_the_two_dist = set()
for x in dice1:
    for y in dice2:
        sum_of_the_two_dist.add(x + y)

print(sum_of_the_two_dist)        