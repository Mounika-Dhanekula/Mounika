"""Create two sets of integers. Perform the given set operations"""
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Set 1:", set1)
print("Set 2:", set2)
print("Union of sets:", set1.union(set2)) 
print("Intersection of sets:", set1.intersection(set2))  
print("Difference (set1 - set2):", set1.difference(set2)) 
print("Symmetric difference of sets:", set1.symmetric_difference(set2))