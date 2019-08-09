# A recursive solution for the number of messages problem
#e.g "111" can be decoded as KA, AAA, AK ===> 3

def num_of_messages(s):
    if len(s) <= 1:
        return 1
    elif int(s[0: 2]) > 26:
        return num_of_messages(s[1: ])
    else:
        return num_of_messages(s[1: ]) + num_of_messages(s[2: ])


print(num_of_messages("111"))