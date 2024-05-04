# # [a if a else 2 for a in [0, 1, 0, 3]]
#
# def pig_it(text):
#     text = text.split(" ")
#     result = [k if k == "!" or k == "?" else k[1:] + k[0] + "ay" for k in text]
#     print(text)
#
#     for k in text:
#         if k == "!" or k == "?":
#             result.append(k)
#         else:
#             result.append(k[1:] + k[0] + "ay")
#
#     return " ".join(result)

def pig_it(text):
    return " ".join([k if k == "!" or k == "?" else k[1:] + k[0] + "ay" for k in text.split(" ")])

print(pig_it("Pig Latin is cool !"))