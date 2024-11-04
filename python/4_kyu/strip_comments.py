def strip_comments(strng, markers):
    lines = strng.split("\n")

    final = ""

    for line in lines:
        new_line = ""
        for char in line:
            if char in markers:
                break
            new_line += char
        final += new_line.rstrip(" ") + "\n"

    return final[:-1]


print(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
