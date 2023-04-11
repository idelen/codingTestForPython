def removeStars(s):
    result = []

    for text in s:
        if text != '*':
            result.append(text)
        else:
            result.pop(-1)
    return ''.join(result)


s_list = ["leet**cod*e", "erase*****"]
for s in s_list:
    print(removeStars(s))