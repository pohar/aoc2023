import re
def Findfirstdigit(str1):
    ret=0

    for c in str1:
        if c.isdigit():
            ret=int(c)
            break

    return ret

def Findlastdigit(str2):
    ret=0

    for c in str2:
        if c.isdigit():
            ret=int(c)
    return ret

def Findfirstdigitname(str1):
    ret=0

    nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    foundnum = -1
    foundpos = 99999
    for i in range(len(str1)):
        p=1
        for num in nums:
            x = str1[i:].startswith(num)
            if x:
                if i<foundpos:
                    foundnum = p
                    foundpos = i
                    ret = int(foundnum)
                break
            p = p + 1

    p2=0
    for c in str1:
        if c.isdigit():
            if p2<foundpos:
                ret=int(c)
            else:
                ret = int(foundnum)
            break
        p2 = p2 + 1

    return ret

def Findlastdigitname(str2):
    ret=0

    nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    foundnum = -1
    foundpos = -1
    for i in range(len(str2)):
        p=1
        for num in nums:
            x = str2[i:].startswith(num)
            if x:
                if i>foundpos:
                    foundnum = p
                    foundpos = i
                    ret = int(foundnum)
            p = p + 1

    p2=0
    for c in str2:
        if c.isdigit():
            if p2>foundpos:
                ret=int(c)
            else:
                ret = int(foundnum)
        p2 = p2 + 1
    return ret

def Day1Pt1(inputfile):
    print('Day 1 Part 1')
    sum = 0
    for line in open(inputfile):
        res = Findfirstdigit(line) *10 + Findlastdigit(line)
        print(f'Line res: {line} {res}')
        sum = sum+res

    print(f"Sum: {sum}")

def Day1Pt2(inputfile):
    print('Day 1 Part 2')
    sum = 0
    for line in open(inputfile):
        res = Findfirstdigitname(line) *10 + Findlastdigitname(line)
        print(f'Line res: {line} {res}')
        sum = sum+res

    print(f"Sum: {sum}")

def Day2Pt1(inputfile):
        print('Day 2 Part 1')
        maxcols = {'blue': 14, "red":12, "green":13}

        sum=0
        for line in open(inputfile):
            line = line.rstrip()
            line = line + ';'
            parts = line.split()
            gameno = int(parts[1][:-1])
            impossible = False
            for i in range(2,len(parts),2):
                num = parts[i]
                col = parts[i + 1][:-1]
                separator = parts[i + 1][-1]
                maxcol = maxcols[col]
                if int(num)>maxcol: #impossible
                    impossible = True
                #print(num, col, maxcol, separator)
            #print(f'gameno:{gameno} impossible:{impossible}')
            if not impossible:
                sum = sum + gameno

        print(f'sum ID: {sum}')


def Day2Pt2(inputfile):
    print('Day 2 Part 2')

    sum = 0
    for line in open(inputfile):
        minblue = mingreen = minred = 0

        line = line.rstrip()
        line = line + ';'
        parts = line.split()
        for i in range(2, len(parts), 2):
            num = int(parts[i])
            col = parts[i + 1][:-1]

            if 'blue' == col:
                minblue = max(minblue, num)
            if 'green' == col:
                mingreen = max(mingreen, num)
            if 'red' == col:
                minred = max(minred, num)

        power = minblue * mingreen * minred
        sum = sum + power

    print(f'sum ID: {sum}')

def Day3Pt1(inputfile):
    print('Day 3 Part 1')

    with open(inputfile, 'r') as f:
        lines = f.readlines()
        f.close()

    GRID_SIZE_X = len(lines[0].strip())
    GRID_SIZE_Y = len(lines)
    print(f'Grid size: y: {GRID_SIZE_X} x: {GRID_SIZE_Y}')
    grid = [[0 for j in range(GRID_SIZE_X)] for i in range(GRID_SIZE_Y)]

    y = 0
    for line in lines:
        #map_object = map(char, line.rstrip())
        grid[y] = list(line.strip())
        y = y + 1

    y=0
    sum=0
    for line in lines:
        x=0
        matches = re.findall('(\d+)', line)
        if matches:
            for match in matches:
                n = int(match)
                x=line.find(match,x)
                ln = len(match)
                if x<0:
                    hiba=1

                #check neighbours
                nok=True
                for ny in range (y-1,y+2):
                    for nx in range(x - 1, x + ln + 1):
                        if (ny>=0) and (ny<GRID_SIZE_Y) and (nx>=0) and (nx<GRID_SIZE_X):
                            if not((y==ny) and (nx>=x) and (nx<x+ln)):
                                #print(f'x:{nx} y:{ny} {grid[ny][nx]}')
                                if grid[ny][nx]!='.':
                                    nok=False
                                    break


                print(f'found num: {n} ({x},{y}) OK:{not nok} ')
                x=x+ln
                if not nok:
                    sum = sum + n

        y=y+1
    print(f'sum: {sum}') #  534249 , 535882, 518661, 517028, 517025 are bad answers

def Day3Pt2(inputfile):
    print('Day 3 Part 2')

    sum = 0
    for line in open(inputfile):
        pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #Day1Pt1('input1_.txt')
    #Day1Pt2('input1.txt')
    #Day2Pt1('input2_.txt')
    #Day2Pt2('input2_.txt')
    Day3Pt1('input3.txt')
    #Day3Pt2('input3_.txt')