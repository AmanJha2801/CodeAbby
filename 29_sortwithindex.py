#create a dic using enum, where the dict key has the numbers and the values are the index
#store the 2 things in seperate things, sort one list with unmbers
#increment the index list with 1 and print, using lambda
#print the list with no brackets, and no comma using *

input_list = [788,741,496,105,682,595,306,441,639,153,542,205,400,925,350,840,48,248,885]


my_dict, temp_list, final_list = {}, [], []
for index, value in enumerate(input_list):
    my_dict[value] = index
    temp_list.append(value)

temp_list.sort()

for values in temp_list:
    final_list.append(my_dict[values])
#print(final_list)
#print(temp_list)
latest_list=list(map(lambda x: x + 1,final_list))
print(*latest_list)

