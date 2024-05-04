def friend(x):
    return [f for f in x if len(f) == 4]

print(friend(["Ryan", "Kieran", "Mark",]))