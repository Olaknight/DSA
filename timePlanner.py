#input:  slotsA = [[10, 50], [60, 120], [140, 210]]
 #       slotsB = [[0, 15], [60, 70]] 
#      dur = 8
#ans [60, 68]
##Time complexity = O(n + m)

slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]] 
dur = 12


def timePlanner(slotsA, slotsB, dur):
    i, j = 0, 0

    while i < len(slotsA) and j < len(slotsB):
        start = max(slotsA[i][0], slotsB[j][0])
        end = min(slotsA[i][1], slotsB[j][1])
        if end - start >= dur:
            return [start, start + dur]
        else:
            if slotsA[i][1] > slotsB[j][1]:
                j += 1
            else:
                i += 1
    return []

print( timePlanner(slotsA, slotsB, dur))