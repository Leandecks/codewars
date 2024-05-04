from functools import reduce
def create_phone_number(n):
    x = reduce(lambda x, y: str(x) + str(y), n)
    return f"({x[:3]}) {x[3:6]}-{x[6:]}"

# def create_phone_number(n):
#     x = ""
#     for k in n: x += str(k)
#
#     return f"({x[:3]}) {x[3:6]}-{x[6:]}"
    
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
