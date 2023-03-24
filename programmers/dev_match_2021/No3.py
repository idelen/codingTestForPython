import math


def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    answer_dict = dict()
    tree_dict = dict()
    for i in range(len(enroll)):
        tree_dict[enroll[i]] = referral[i]
        answer_dict[enroll[i]] = 0

    for sdx in range(len(seller)):
        profit = 100 * amount[sdx]
        person = seller[sdx]
        # 루프 시작?
        while 1:
            divide_profit = math.floor(profit * 0.1)
            answer_dict[person] += (profit - divide_profit)
            if divide_profit == 0 or tree_dict[person] == "-":
                break
            person = tree_dict[person]
            profit = divide_profit

    for i in range(len(enroll)):
        answer[i] = answer_dict.get(enroll[i])

    return answer


ENROLLS = [["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
           ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]]
REFERRALS = [["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
             ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]]
SELLERS = [
    ["young", "john", "tod", "emily", "mary"],
    ["sam", "emily", "jaimie", "edward"]
]
AMOUNTS = [[12, 4, 2, 5, 10], [2, 3, 5, 4]]

for i in range(2):
    print(solution(ENROLLS[i], REFERRALS[i], SELLERS[i], AMOUNTS[i]))
