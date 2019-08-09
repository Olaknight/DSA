def lcs(s1, s2):
    present = 0
    string = ""
    for i in range(len(s1)):
        x = s2[present: ].find(s1[i])
        if x != -1:
            string = string + s1[i]
            present = x

    return string

s1 = "abcjkpoodgh"
s2 = "aicdwefesygh"           
print(lcs(s1, s2))