import datetime
result_table = []


for a in range(50):
    start = datetime.datetime.now()
    for i in range(10000000):
        i += 1
    end = datetime.datetime.now()
    result = (end - start)
    print(f'Test nr {a}: {result}')
    result_table.append(result)

for o in range(1, len(result_table)):
    result_table[0] += result_table[o]
print(result_table[0])

