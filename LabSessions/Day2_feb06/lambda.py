nums = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)
squared = list(map(lambda x: x * x, nums))
print(squared)
from functools import reduce

print(reduce(lambda x,y:x+y,nums))



salaries = [25000, 40000, 32000, 18000]

num = list(filter(lambda x: x>30000, salaries))
print(num)

hiked = list(map(lambda x: x * 1.10,num))
print(hiked)


from functools import reduce

print(reduce(lambda x,y:x+y,hiked))
