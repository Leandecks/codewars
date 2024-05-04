# def solution(number):
#     result = 0
#
#     for k in range(number):
#         if k % 5 == 0 or k % 3 == 0:
#             result += k
#
#     return result

def solution(number):
    return sum(k for k in range(number) if k % 5 == 0 or k % 3 == 0)

print(solution(4))

