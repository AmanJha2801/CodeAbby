input_list = '''0 0 1 1
1 0 0 1'''

#list ko shi se kiye
numbered_list = list(map(int, input_list.split()))

# print(numbered_list)

#y=ax+b
#b=y-ax
#slope nikalo
#a=y2-y1/x2-x1
#fir test case
#4 number ko x1,y1,x2,y2 de diye aur ye finction me baitha diya
#usse a aur b aa gya


def find_linear_function(x1, y1, x2, y2):
    a = (y2 - y1) / (x2 - x1)
    b = y1 - a * x1
    return a, b

result = []

test_cases = len(numbered_list) // 4
for i in range(test_cases):
    # x1, y1, x2, y2 = numbered_list[0], numbered_list[1], numbered_list[2], numbered_list[3]
    x1, y1, x2, y2 = numbered_list[i * 4:(i + 1) * 4]
    a, b = find_linear_function(x1, y1, x2, y2)
    print(f"({a} {b})")

