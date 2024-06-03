"""

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

"""


def twoSortedList(list1, list2):

    for i in list2:
        inserted = False
        for j in range(len(list1)):
            if i <= list1[j]:
                list1.insert(j, i)
                inserted = True
                break
        if not inserted :
            list1.append(i)

    return list1

list1 = []
list2 = [0]

merged_list = twoSortedList(list1, list2)

print(merged_list)