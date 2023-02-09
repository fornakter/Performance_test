import datetime
result_table = []


for a in range(5):
    start = datetime.datetime.now()
    for i in range(100000000):
        i += 1
    end = datetime.datetime.now()
    result = (end - start)
    print(f'Test nr {a}: {result}')
    result_table.append(result)

for o in range(1, 5):
    print(o)
    result_table[0] += result_table[o]
print(result_table[0])

