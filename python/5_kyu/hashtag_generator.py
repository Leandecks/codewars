def generate_hashtag(s):
    result = "#"
    s = s.split(" ")
    for k in s:
        if k != "":
            result += k.capitalize()
    if result == "#" or len(result) > 140:
        return False
    else:
        return result

print(generate_hashtag(""))