# 27 23 21 29 6 20 19 10 15 15 22#11_sum of digits

#list ko split karo
#list of lists containing 3 numbers each
#a,b,c, iterate and get sum
#x=a*b+c, take sum of digits of x and store that in a list
input_list = '''393 45 54
395 92 178
382 226 80
97 78 113
180 5 150
94 294 194
312 257 34
286 84 196
175 16 131
40 135 24
243 112 112'''
numbers = list(map(int, input_list.split()))
print(numbers)
coupled_list = [numbers[i:i+3] for i in range(0, len(numbers), 3)]
sum_list = [x[0] * x[1] + x[2] for x in coupled_list]
final_list = [sum(int(digit) for digit in str(val)) for val in sum_list]
print(*final_list)