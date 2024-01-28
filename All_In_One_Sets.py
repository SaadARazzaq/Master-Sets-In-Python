import os
import time as t

print("\t\t***Python Program starting shortly...***")
t.sleep(1.5)

# There are various set methods in Python

# 1) add(): This method adds an element to the set.
# The add() method takes exactly one argument.

print("\n<---------------1) add() method---------------->\n")

set_to_add = {1, 2, 3}
print("Original set: ", set_to_add)
element_to_add = int(input("Enter an element to add to the set: "))
set_to_add.add(element_to_add)
print("Set after adding the element: ", set_to_add)

# 2) update(): This method adds elements to the set from another set or iterable.
# The update() method takes either a set or any iterable as an argument.

t.sleep(3)
print("\n<---------------2) update() method---------------->\n")

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Set 1: ", set1)
print("Set 2: ", set2)
set1.update(set2)
print("Set after updating with Set 2: ", set1)

# 3) remove(): This method removes a specified element from the set.
# If the element is not present, it raises a KeyError.

t.sleep(3)
print("\n<---------------3) remove() method---------------->\n")

set_to_remove = {1, 2, 3, 4, 5}
print("Original set: ", set_to_remove)
element_to_remove = int(input("Enter an element to remove from the set: "))
set_to_remove.remove(element_to_remove)
print("Set after removing the element: ", set_to_remove)

# 4) discard(): This method removes a specified element from the set.
# If the element is not present, it does nothing.

t.sleep(3)
print("\n<---------------4) discard() method---------------->\n")

set_to_discard = {1, 2, 3, 4, 5}
print("Original set: ", set_to_discard)
element_to_discard = int(input("Enter an element to discard from the set: "))
set_to_discard.discard(element_to_discard)
print("Set after discarding the element: ", set_to_discard)

# 5) pop(): This method removes and returns an arbitrary element from the set.
# If the set is empty, it raises a KeyError.

t.sleep(3)
print("\n<---------------5) pop() method---------------->\n")

set_to_pop = {1, 2, 3, 4, 5}
print("Original set: ", set_to_pop)
popped_element = set_to_pop.pop()
print(f"Popped element: {popped_element}")
print("Set after popping the element: ", set_to_pop)

# 6) clear(): This method removes all elements from the set.

t.sleep(3)
print("\n<---------------6) clear() method---------------->\n")

set_to_clear = {1, 2, 3, 4, 5}
print("Original set: ", set_to_clear)
set_to_clear.clear()
print("Set after clearing all elements: ", set_to_clear)

# 7) union(): This method returns a new set containing all unique elements from the sets.

t.sleep(3)
print("\n<---------------7) union() method---------------->\n")

set_union1 = {1, 2, 3}
set_union2 = {3, 4, 5}
union_result = set_union1.union(set_union2)
print("Set 1: ", set_union1)
print("Set 2: ", set_union2)
print("Union of Set 1 and Set 2: ", union_result)

# 8) intersection(): This method returns a new set containing common elements from the sets.

t.sleep(3)
print("\n<---------------8) intersection() method---------------->\n")

set_intersection1 = {1, 2, 3, 4}
set_intersection2 = {3, 4, 5}
intersection_result = set_intersection1.intersection(set_intersection2)
print("Set 1: ", set_intersection1)
print("Set 2: ", set_intersection2)
print("Intersection of Set 1 and Set 2: ", intersection_result)

# 9) difference(): This method returns a new set containing elements that are in the first set but not in the second set.

t.sleep(3)
print("\n<---------------9) difference() method---------------->\n")

set_difference1 = {1, 2, 3, 4}
set_difference2 = {3, 4, 5}
difference_result = set_difference1.difference(set_difference2)
print("Set 1: ", set_difference1)
print("Set 2: ", set_difference2)
print("Difference of Set 1 and Set 2: ", difference_result)

# 10) symmetric_difference(): This method returns a new set containing elements that are unique to each set.

t.sleep(3)
print("\n<---------------10) symmetric_difference() method---------------->\n")

set_symmetric1 = {1, 2, 3, 4}
set_symmetric2 = {3, 4, 5}
symmetric_difference_result = set_symmetric1.symmetric_difference(set_symmetric2)
print("Set 1: ", set_symmetric1)
print("Set 2: ", set_symmetric2)
print("Symmetric Difference of Set 1 and Set 2: ", symmetric_difference_result)

# 11) issubset(): This method returns True if all elements of a set are present in another set.

t.sleep(3)
print("\n<---------------11) issubset() method---------------->\n")

set_issubset1 = {1, 2}
set_issubset2 = {1, 2, 3, 4, 5}
print("Set 1: ", set_issubset1)
print("Set 2: ", set_issubset2)
print("Is Set 1 a subset of Set 2? ", set_issubset1.issubset(set_issubset2))

# 12) issuperset(): This method returns True if all elements of another set are present in the set.

t.sleep(3)
print("\n<---------------12) issuperset() method---------------->\n")

set_issuperset1 = {1, 2, 3, 4, 5}
set_issuperset2 = {1, 2}
print("Set 1: ", set_issuperset1)
print("Set 2: ", set_issuperset2)
print("Is Set 1 a superset of Set 2? ", set_issuperset1.issuperset(set_issuperset2))

# 13) copy(): This method returns a shallow copy of the set.

t.sleep(3)
print("\n<---------------13) copy() method---------------->\n")

set_to_copy = {1, 2, 3}
copied_set = set_to_copy.copy()
print("Original set: ", set_to_copy)
print("Copied set: ", copied_set)

# 14) frozenset(): This method returns an immutable frozenset object.

t.sleep(3)
print("\n<---------------14) frozenset() method---------------->\n")

set_to_freeze = {1, 2, 3}
frozen_set = frozenset(set_to_freeze)
print("Original set: ", set_to_freeze)
print("Frozen set: ", frozen_set)

# 15) in and not in: These operators allow you to check if an element is present in a set.

t.sleep(3)
print("\n<---------------15) 'in' and 'not in' operators---------------->\n")

set_to_check = {1, 2, 3, 4, 5}
element_to_check = int(input("Enter an element to check in the set: "))
print("Set: ", set_to_check)
print(f"{element_to_check} is {'in' if element_to_check in set_to_check else 'not in'} the set.")

# 16) Removing Duplicate Elements from a List using set: You can use set to remove duplicate elements from a list.

t.sleep(3)
print("\n<---------------16) Removing Duplicate Elements from a List using set---------------->\n")

list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_elements_set = set(list_with_duplicates)
print("List with duplicates: ", list_with_duplicates)
print("List after removing duplicates using set: ", list(unique_elements_set))

# 17) intersection_update(): This method updates the set with the intersection of itself and another set.

t.sleep(3)
print("\n<---------------17) intersection_update() method---------------->\n")

set_intersection_update1 = {1, 2, 3, 4}
set_intersection_update2 = {3, 4, 5}
print("Set 1: ", set_intersection_update1)
print("Set 2: ", set_intersection_update2)
set_intersection_update1.intersection_update(set_intersection_update2)
print("Set after updating with the intersection of Set 1 and Set 2: ", set_intersection_update1)

# 18) difference_update(): This method updates the set with the difference of itself and another set.

t.sleep(3)
print("\n<---------------18) difference_update() method---------------->\n")

set_difference_update1 = {1, 2, 3, 4}
set_difference_update2 = {3, 4, 5}
print("Set 1: ", set_difference_update1)
print("Set 2: ", set_difference_update2)
set_difference_update1.difference_update(set_difference_update2)
print("Set after updating with the difference of Set 1 and Set 2: ", set_difference_update1)

# 19) symmetric_difference_update(): This method updates the set with the symmetric difference of itself and another set.

t.sleep(3)
print("\n<---------------19) symmetric_difference_update() method---------------->\n")

set_symmetric_difference_update1 = {1, 2, 3, 4}
set_symmetric_difference_update2 = {3, 4, 5}
print("Set 1: ", set_symmetric_difference_update1)
print("Set 2: ", set_symmetric_difference_update2)
set_symmetric_difference_update1.symmetric_difference_update(set_symmetric_difference_update2)
print("Set after updating with the symmetric difference of Set 1 and Set 2: ", set_symmetric_difference_update1)

# 20) isdisjoint(): This method returns True if two sets have no elements in common.

t.sleep(3)
print("\n<---------------20) isdisjoint() method---------------->\n")

set_isdisjoint1 = {1, 2, 3}
set_isdisjoint2 = {4, 5, 6}
print("Set 1: ", set_isdisjoint1)
print("Set 2: ", set_isdisjoint2)
print("Are Set 1 and Set 2 disjoint? ", set_isdisjoint1.isdisjoint(set_isdisjoint2))

# 21) union(): This method returns a new set containing all elements from the original sets.

t.sleep(3)
print("\n<---------------21) union() method---------------->\n")

set_union1 = {1, 2, 3}
set_union2 = {3, 4, 5}
print("Set 1: ", set_union1)
print("Set 2: ", set_union2)
union_set = set_union1.union(set_union2)
print("Union of Set 1 and Set 2: ", union_set)

# 22) issubset(): This method returns True if all elements of a set are present in another set.

t.sleep(3)
print("\n<---------------22) issubset() method---------------->\n")

set_issubset1 = {1, 2}
set_issubset2 = {1, 2, 3, 4}
print("Set 1: ", set_issubset1)
print("Set 2: ", set_issubset2)
print("Is Set 1 a subset of Set 2? ", set_issubset1.issubset(set_issubset2))
