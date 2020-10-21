a = {"James", "Ann", "Ruth", "Victor"}
b = {"Ann", "Victor", "Elizabeth", "Tyson", "Shepard"}

def jaccard_index(first_set, second_set):
    intersection_cardinality = 0
    for element in first_set:
        if element in second_set:
            intersection_cardinality += 1
    return intersection_cardinality / (len(first_set) + len(second_set) - intersection_cardinality)


print(jaccard_index(a, b))