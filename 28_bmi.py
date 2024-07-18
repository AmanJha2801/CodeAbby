input_list = '''80 1.73
55 1.58
49 1.91'''

# numbers = list(map(float, input_list.split()))
# print(numbers)
#
# coupled_list = [numbers[i:i+2] for i in range(0, len(numbers), 2)]

coupled_list = [list(map(float, input_list.split()))[i:i+2] for i in range(0, len(list(map(float, input_list.split()))), 2)]

print(coupled_list)

final_list=[]

bmi_list=[]
# final_list=[]
def BMI_cal(w, h):
    value = w/float(h*h)
    bmi_list.append(round(value,1))
    if bmi_list[-1] > 30.0:
        bmi = "obese"
    elif 30.0 >= bmi_list[-1] > 25.0:
        bmi = "over"
    elif 25.0 >= bmi_list[-1] > 18.5:
        bmi = "normal"
    else:
        bmi = "under"
    final_list.append(bmi)


for pair in coupled_list:
    BMI_cal(pair[0], pair[1])
print(*final_list)