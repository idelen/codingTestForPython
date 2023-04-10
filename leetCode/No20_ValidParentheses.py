def isValid(s):
    open_brackets = ["(", "{", "["]
    close_brackets = [")", "}", "]"]

    bracket_dict = dict()

    for idx in range(len(open_brackets)):
        bracket_dict[open_brackets[idx]] = close_brackets[idx]

    brackets_stack = []

    for text in s:
        if text in open_brackets:
            brackets_stack.append(text)
        elif text in close_brackets:
            if len(brackets_stack) == 0:
                return False

            stack_tail = brackets_stack.pop(-1)

            if bracket_dict[stack_tail] != text:
                return False

    return len(brackets_stack) == 0


s_list = ["()", "()[]{}", "(]"]
for s in s_list:
    print(isValid(s))