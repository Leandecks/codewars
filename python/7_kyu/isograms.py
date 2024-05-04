def is_isogram(string):
    isogram = True

    for k in string:
        if string.lower().count(k.lower()) > 1:
            isogram = False
            break
        else:
            isogram = True

    return isogram

print(is_isogram("moOse"))