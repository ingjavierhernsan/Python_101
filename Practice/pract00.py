def countingValleys(steps, path):
    valley = False
    p = 0
    ret = 0

    for x in range(steps):
        if path[x] == "U":
            valley = False
            p = p + 1
        elif path[x] == "D":
            valley = True
            p = p - 1
        
        if p == 0 and valley:
            ret = ret + 1

    return ret

#print(countingValleys(8, "DDUUUUDD"))
print(countingValleys(8, "UDDDUDUU")) #1
print(countingValleys(12, "DDUUDDUDUUUD"))#2
