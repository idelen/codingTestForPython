def longestPalindrome(s):
    result = s[0]
    text_dict = dict()
    for idx, text in enumerate(s):
        if text not in text_dict:
            text_dict[text] = []
        text_dict[text].append(idx)

    for key, value in text_dict.items():
        if len(value) < 2:
            continue

        sorted(value)

        for sdx in range(len(value)):
            init_head = value[sdx]
            for edx in range(len(value) - 1, sdx, -1):
                init_tail = value[edx]

                if (init_tail - init_head + 1) < len(result):
                    break

                temp = s[init_head:init_tail + 1]

                if temp == temp[::-1]:
                    if len(result) < len(temp):
                        result = temp

    return result









s_list = ["babad", "cbbd"]
for s in s_list:
    print(longestPalindrome(s))
