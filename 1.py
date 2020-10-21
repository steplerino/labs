array = ['a', 'b', 'c', 'd', 'e', 'a', 'a', 'b', 'c']
result = dict()
for index in range(len(array)):
    if array[index] in result:
        result[array[index]].append(index)
    else:
        result[array[index]] = [index]
print(result)

result_one_line = {key: [index for index in range(len(array)) if array[index] == key] for key in array}
print(result_one_line)
