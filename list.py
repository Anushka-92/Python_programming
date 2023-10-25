# Lists
List = [12, "Arr", 12.4, 'd']
print("Type:", type(List))
# Extract first and last element
print("First:", List[0])  # first
print("Last:", List[-1])  # last
# Modify the list
List[1] = 1
print(List)
# append
List.append("esha")
print(List)
# pop
print(List.pop())

L1 = [1, 'a', True, 34]
print(L1.pop())
print(L1)
# reverse
List.reverse()
print(List)

# insert
List.insert(1, "esha")
print(List)
# sort
L1 = [1, 5, 78, 34]
L1.sort()
print(L1)

# concatenate
print(L1 + List)

# repeat
print(L1 * 3)

# repeat and concatenate
print(L1 * 2 + List)