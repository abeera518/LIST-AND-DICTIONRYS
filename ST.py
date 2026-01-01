lst=['apple', 'banana', 'cherry', 'date', 'elderberry', 'peach', 'grape']

print("length of the list:", len(lst))
print("first element:", lst[0])
print("last element:", lst[-1])

lst.append("kiwi")
print("updated list:", lst)

lst.remove("date")
print("updated list:", lst)

lst.sort()
print("sorted list:", lst)

lst.pop(1)
print("updated list:", lst)

lst.reverse()
print("reversed list:", lst)    

print("Multiplying the list by 2:", lst * 2)

lst = lst[:4]
print("sliced list :", lst)

lst.clear()
print("cleared list:", lst)