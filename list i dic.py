def test(lst):
    results = {}
    for item in lst:
        results[item[0]] = item[1:]
    return results

students = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]

print("\nOriginal list of lists:")
print(students)
print("\nConverted to dictionary:")
print(test(students))