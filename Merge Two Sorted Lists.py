"""

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

"""

list1 = [1,3,5]

list2 = [2,4,6]


list3 = list1 + list2

list3.sort()

print(list3)