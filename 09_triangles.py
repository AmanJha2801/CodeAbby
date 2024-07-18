import math

listOfNums = '''1002 514 1227 1427 591 520 564 973 1961 426 892 282 258 397 966 628 913 557 284 527 165 1367 975 1025 442 1423 876 162 197 298 393 604 1442 1077 395 494 197 517 217 996 746 2441 359 537 1263 640 2338 1184 917 1395 568 711 229 379 1034 690 750 1460 2223 738 390 237 476 1362 2411 717 3292 1564 903 442 333 240 1419 1852 943 954 1094 2582 216 170 118 1340 816 3326 1166 2760 886 752 2333 1076'''

def triangle(a, b, c):
    s = (a + b + c) / 2
    if s - a < 0 or s - b < 0 or s - c < 0:
        return 0
    else:
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area

listOfNums = [int(x) for x in listOfNums.split()]
mas = []
index = 0
lenOfArray = len(listOfNums) // 3

for i in range(lenOfArray):
    mas.append([])
    for j in range(3):
        mas[i].append(listOfNums[index])
        index += 1

area_triangle = [triangle(x[0], x[1], x[2]) for x in mas]
final_list = []

for i, value in enumerate(area_triangle):
    if value > 0:
        final_list.append('1')
    else:
        final_list.append('0')

print(*final_list)