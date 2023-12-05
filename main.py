import re
from collections import Counter
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
    print(f'sum: {sum}')


def letterFrequency(fileName, letter):
    # open file in read mode
    file = open(fileName, 'r')

    # store content of the file in a variable
    text = file.read()

    # using count()
    return text.count(letter)
def Day3Pt2(inputfile):
    print('Day 3 Part 2')

    with open(inputfile, 'r') as f:
        lines = f.readlines()
        f.close()

    print('number of stars:', letterFrequency(inputfile, '*'))

    GRID_SIZE_X = len(lines[0].strip())
    GRID_SIZE_Y = len(lines)
    print(f'Grid size: y: {GRID_SIZE_X} x: {GRID_SIZE_Y}')
    grid = [[0 for j in range(GRID_SIZE_X)] for i in range(GRID_SIZE_Y)]

    y = 0
    for line in lines:
        #map_object = map(char, line.rstrip())
        grid[y] = list(line.strip())
        y = y + 1

    gears={}
    gears_n={}
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

                #find gears around numbers
                for ny in range (y-1,y+2):
                    for nx in range(x - 1, x + ln + 1):
                        if (ny>=0) and (ny<GRID_SIZE_Y) and (nx>=0) and (nx<GRID_SIZE_X):
                            if not((y==ny) and (nx>=x) and (nx<x+ln)):
                                if grid[ny][nx]=='*': #found a gear
                                    if (ny, nx) in gears_n.keys():
                                        gears_n[(ny, nx)] = 1 + gears_n[(ny, nx)]
                                        if( 2<gears_n[(ny, nx)]):
                                            hiba=2
                                    else:
                                        gears_n[(ny, nx)] = 1

                                    if (ny,nx) in gears.keys():
                                        gears[(ny, nx)] = n*gears[(ny,nx)]
                                    else:
                                        gears[(ny,nx)] = n

                                    break
                x = x + ln

        y=y+1
    #print('number of gears:', len(gears),len(gears_n))
    #print(gears)
    #print(gears_n)

    for keys in gears_n:
        if gears_n[keys] == 2:
            sum = sum + gears[keys]

    print(f'sum: {sum}') # 163075488, 80671890, 79940686 are bad

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))
def Day4Pt1(inputfile):
    print('Day 4 Part 1')

    sum = 0
    for line in open(inputfile):
        cardno , numbers = line.strip().split(":")
       # print (cardno , numbers)
        mynumbers_str, winnernums_str = numbers.strip().split('|')
        mynumbers = mynumbers_str.strip().split(" ")
        mynumbers = [i for i in mynumbers if i]
        winnernums =winnernums_str.strip().split(" ")
        winnernums = [i for i in winnernums if i]

        points =len(intersection(mynumbers,winnernums))
        if points>0:
            points =2**(len(intersection(mynumbers,winnernums))-1)
        #print(points)
        sum = sum+points
        #print(mynumbers, winnernums)
    print(f"sum: {sum}")

def Day4Pt2(inputfile):
    print('Day 4 Part 2')

    copies= [1]*300

    i=0
    for line in open(inputfile):
        cardno , numbers = line.split(":")
        #print (cardno , numbers)
        mynumbers_str, winnernums_str = numbers.split('|')
        mynumbers = mynumbers_str.split()
        winnernums =winnernums_str.split()

        points =len(intersection(mynumbers,winnernums))
        if points>0:
            for j in range(i+1,i+points+1):
                copies[j] += copies[i]

        i = i+1

    total=sum(copies[:i])

    print(f"total: {total}") # 14814534


def Day4Pt2x(inputfile):
    print('Day 4 Part 2 ChatGPT optimized version')

    copies = [1] * 300
    i = 0
    with open(inputfile) as file:
        for line in file:
            cardno, numbers = map(str.strip, line.split(":"))
            mynumbers_str, winnernums_str = map(str.strip, numbers.split('|'))

            mynumbers = list(filter(None, mynumbers_str.split(" ")))
            winnernums = list(filter(None, winnernums_str.split(" ")))

            points = len(set(mynumbers) & set(winnernums))

            if points > 0:
                for j in range(i + 1, i + points + 1):
                    copies[j] += copies[i]

            i += 1

    total_sum = sum(copies[:i])
    print(f"sum: {total_sum}")

def Day5Pt1(inputfile):
    print('Day 5 Part 1')

    for line in open(inputfile):
        pass

def Day5Pt1(inputfile):
    print('Day 5 Part 1')

    seeds=[]
    maps=dict()
    categories=[]

    with open(inputfile, 'r') as f:
        lines = f.readlines()
        f.close()
    maxy=len(lines)

    y=0
    seeds = list(map(int,lines[0].split()[1:]))
    y+=1
    for cat in range(0,7):
        y +=1
        src_cat, _ , dst_cat = lines[y].strip().split()[0].split('-')
        categories.append(src_cat)
        if cat==6:
            categories.append(dst_cat)
        y += 1
        maps[(src_cat, dst_cat)]=[]
        while '' != lines[y].strip():
            dst_start, src_start, range_len = list(map(int,lines[y].strip().split()))
            maps[((src_cat, dst_cat))].append((src_start, dst_start, range_len))
            y += 1
            if y>=maxy:
                break

    print("starting replace")
    res=[]
    for seed in seeds:
        s=seed
        #print("seed:", seed)
        for cat in range(0,7):
            replaces = maps[(categories[cat], categories[cat+1])]
            for repl in replaces:
                src_start, dst_start, range_len = repl
                if s in range(src_start , src_start+range_len+1):
                    s =  s - src_start + dst_start
                    break
            #print(categories[cat+1], s)
        res.append(s)

    print("seeds:",seeds)
    print("res:",res)
    print("min res:",min(res)) # 9607836 is too low
    print('end')

if __name__ == '__main__':
    #Day1Pt1('input1_.txt')
    #Day1Pt2('input1.txt')
    #Day2Pt1('input2_.txt')
    #Day2Pt2('input2_.txt')
    #Day3Pt1('input3.txt')
    #Day3Pt2('input3.txt')
    #Day4Pt1('input4.txt')
    #Day4Pt2('input4.txt')
    #Day4Pt2x('input4.txt')
    Day5Pt1('input5.txt')
    #Day5Pt2('input5_.txt')
