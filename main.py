import timeit
result_table = []

start = timeit.timeit()
for a in range(10):
    for i in range(10000000):
        i += 1
    end = timeit.timeit()
    result = (start - end)*10
    print(f'Test nr {a}: {round(result, 6)}')
    result_table.append(result)

print(sum(result_table))
