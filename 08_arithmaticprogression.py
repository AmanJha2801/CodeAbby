num=[4,16,11,12,16,24,19,26]
steps=[14,12,9,11,6,13,13,8]
times=[75,32,49,65,64,57,11,10]

result = []

"""how the below loop works

iteration 1:

- init = 4 (from num)
- step = 14 (from steps)
- n = 75 (from times)
- Arithmetic progression: 4, 18, 32, ... (75 terms)
- Sum: 2916
- result = [2916]

iteration 2:

- init = 16 (from num)
- step = 12 (from steps)
- n = 32 (from times)
- Arithmetic progression: 16, 28, 40, ... (32 terms)
- Sum: 1584
- result = [2916, 1584]

"""
for init, step, n in zip(num, steps, times):
    result.append(sum([init + i * step for i in range(n)]))


print(*result)