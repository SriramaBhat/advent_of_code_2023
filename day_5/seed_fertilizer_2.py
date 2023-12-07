Seeds, TransTabs = [], [[],[],[],[],[],[],[]]
file = open("F:\\advent_of_code\\inputs\\day_5.txt", "r")
inp = file.readlines()
proctype = -1
for line in inp:
    if len(line) < 3:
        pass
    elif line[0:5] == 'seeds':
        Seeds = [int(n) for n in line[7:].split(' ')]
    elif ':' in line:
        proctype += 1
    else:
        numlist = [int(n) for n in line.split(' ')]
        TransTabs[proctype].append(numlist)
ans = []
for i in range(0, len(Seeds), 2):
    seedstart, seedrange, skip = Seeds[i], Seeds[i+1], Seeds[i+1]
    nextseed = seedstart
    while nextseed <= seedstart + seedrange:
        res = nextseed
        for transl in range(7):
            for val in TransTabs[transl]:
                if val[1] <= res < val[1] + val[2]:
                    skip = min(skip, val[1] + val[2] - res)
                    res += (val[0] - val[1])
                    if skip <= 0:
                        skip = 1
                    break
        ans.append(res)
        nextseed += skip
        skip = seedrange - nextseed + seedstart
print(min(ans))
