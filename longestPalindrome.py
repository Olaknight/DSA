def checkPal(s):
    start = 0
    end = len(s) - 1
    i = 0

    while i < len(s) // 2:
        if s[start] != s[end]:
            return False
        else:
            start += 1
            end -= 1
            i += 1
    return True


def longestPali(s):
    

print(checkPal("omtmo"))