a = {"James", "Ann", "Ruth", "Victor"}
b = {"Ann", "Victor", "Elizabeth", "Tyson", "Shepard"}

intersect_cardinality = len(a) - len(a - b)
union_cardinality = len(a) + len(b) - intersect_cardinality
print("Jaccard", int(intersect_cardinality / union_cardinality * 10000) / 10000)


def jaccard_index(first_set, second_set):
    for element in first_set:
        intersection_cardinality = 0
        if element in second_set:
            intersection_cardinality += 1
    return intersection_cardinality / (len(first_set) + len(second_set) - intersection_cardinality)


print(jaccard_index(a, b))
