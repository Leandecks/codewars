def dig_pow(n, p):
    result = 0
    for k in str(n):
        result += int(k) ** p
        p += 1
    return result // n if result % n == 0 else -1


print(dig_pow(89, 1))
