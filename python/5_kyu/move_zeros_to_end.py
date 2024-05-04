"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""

def move_zeros(lst):
    return [k for k in lst if k != 0] + [k for k in lst if k == 0]

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))

# for k in lst:
#     if k == 0:
#         list.append(k)
#     else
#         list2.append(k)
#
# return list + list2