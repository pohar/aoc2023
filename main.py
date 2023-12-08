import re
import time
from collections import Counter
from numba import jit
from numba.typed import List
import math


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
        matches = re.findall(r'(\d+)', line)
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
        matches = re.findall(r'(\d+)', line)
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


@jit(nopython=True)
def calc_range(maps, range_end, range_start, res):
    for cs in range(range_start, range_end):
        s=cs
        for replaces in maps:
            for src_start, dst_start, range_len in replaces:
                if s in range(src_start, src_start + range_len):
                    s = s - src_start + dst_start
                    break
        if s < res:
            res = s
    return res

def Day5Pt2(inputfile):
    print('Day 5 Part 2')

    starttime = time.time()
    seeds=[]
    maps = List()
    categories=[]

    with open(inputfile, 'r') as f:
        lines = f.readlines()
        f.close()
    maxy=len(lines)

    y=0
    seeds = list(map(int,lines[0].split()[1:]))
    y+=1
    for cat in range(7):
        y +=1
        src_cat, _ , dst_cat = lines[y].strip().split()[0].split('-')
        categories.append(src_cat)
        if cat==6:
            categories.append(dst_cat)
        y += 1
        newmap=List()
        while '' != lines[y].strip():
            dst_start, src_start, range_len = list(map(int,lines[y].strip().split()))
            newmap.append((src_start, dst_start, range_len))
            y += 1
            if y>=maxy:
                break
        maps.append(newmap)

    res=999999999999
    print("*** starting replace ")
    for i in range(0,len(seeds),2):
        startrange = time.time()
        range_start = seeds [i]
        range_end = range_start+seeds [i+1]
        print(f"range: {range_start:_};{range_end:_}")

        res = calc_range(maps, range_end, range_start, res)
        endrange = time.time()
        print('range end time: ',endrange-startrange,' res so far: ', res)

    endtime = time.time()
    print('ended in:', endtime-starttime)
    print('final res: ',res) # 79004094


def Day6Pt1(inputfile):
    def calcdist(time, maxtime, startspeed=0):
        speed = startspeed + time
        dist = speed * (maxtime - time)
        return dist

    print('Day 6 Part 1')

    with open(inputfile) as file:
        for line in file:
            if line.startswith("Time:"):
                _, times_str = map(str.strip, line.split(":"))
                times = list(map(int, times_str.split()))
                print(times)
            elif line.startswith("Distance:"):
                _, distances_str = map(str.strip, line.split(":"))
                distances = list(map(int, distances_str.split()))
                print(distances)
            else:
                print("**** bad line ****")
        if len(times)!= len(distances):
            print("**** bad parse ****")

    goods=1
    for raceno in range(len(times)):
        time = times[raceno]
        distance = distances[raceno]
        num_good = 0
        for i in range(time+1):
            d = calcdist(i,time)
            #print(i,d)
            if(d>distance):
                num_good+=1
        print(f'race: {raceno} {num_good}')
        goods *= num_good

    print("res: ",goods)

def Day6Pt2(inputfile):
    def calcdist(time, maxtime, startspeed=0):
        speed = startspeed + time
        dist = speed * (maxtime - time)
        return dist

    print('Day 6 Part 2')

    with open(inputfile) as file:
        for line in file:
            line=line.replace(" ","")
            if line.startswith("Time:"):
                _, times_str = map(str.strip, line.split(":"))
                times = list(map(int, times_str.split()))
                print(times)
            elif line.startswith("Distance:"):
                _, distances_str = map(str.strip, line.split(":"))
                distances = list(map(int, distances_str.split()))
                print(distances)
            else:
                print("**** bad line ****")
        if len(times)!= len(distances):
            print("**** bad parse ****")

    goods=1
    for raceno in range(len(times)):
        time = times[raceno]
        distance = distances[raceno]
        num_good = 0
        for i in range(time+1):
            d = calcdist(i,time)
            #print(i,d)
            if(d>distance):
                num_good+=1
        print(f'race: {raceno} {num_good}')
        goods *= num_good

    print("res: ",goods) # bad: 499221010971440

def GetType(card):
    type=0
    sorted_card = sorted(card)
    setcard = set(card)
    if 1 == len(setcard): # Five of a kind
        type = 1
    elif 2 == len(setcard): # Four of a kind or Full House
        cnt = card.count(card[0])
        if cnt in [1,4]:
            type = 2  # Four of a kind
        else:
            type = 3 # Full House
    elif 3 == len(setcard): # Three of a kind or Two pair
        if (2== card.count(card[0])) or (2== card.count(card[1])):
            type = 5 # Two pair
        else:
            type = 4 # Three of a kind
    elif 4 == len(setcard):  # One pair
        type = 6
    elif 5 == len(setcard):  # High card
        type = 7
    else:
        print('Unknown hand type:', card)

    return type
def Day7Pt1(inputfile):
    print('Day 7 Part 1')
    starttime = time.time()

    hands=[] #List()
    bids=[] #List()
    with open(inputfile) as file:
        for line in file:
            hand,bid = line.split()
            hand_orig = hand
            hand=hand.replace('A','F')
            hand=hand.replace('K','E')
            hand=hand.replace('Q','D')
            hand=hand.replace('J','C')
            hand=hand.replace('T','B')
            hands.append((hand,bid,GetType(hand),hand_orig))

    #sort
    print("Start sorting")
    hands.sort(key=lambda x: x[0])
    hands.sort(key=lambda x: x[2], reverse=True)

    #sum
    print("Calc result")
    sum = 0
    i=1
    for _,bid,_,_ in hands:
        sum += i*int(bid)
        i +=1

    endtime = time.time()
    print('ended in:', endtime-starttime)
    print("res:",sum)
    print("End.")

def GetType2(ocard):
    def most_frequent(List):
        counter = 0
        num = List[0]

        for i in List:
            if '1'!=i:
                curr_frequency = List.count(i)
                if (curr_frequency > counter):
                    counter = curr_frequency
                    num = i

        return num

    type=0
    mostcommon = most_frequent(ocard)
    card = ocard.replace("1", mostcommon)
    setcard = set(card)
    if 1 == len(setcard): # Five of a kind
        type = 1
    elif 2 == len(setcard): # Four of a kind or Full House
        cnt = card.count(card[0])
        if cnt in [1,4]:
            type = 2  # Four of a kind
        else:
            type = 3 # Full House
    elif 3 == len(setcard): # Three of a kind or Two pair
        if (2== card.count(card[0])) or (2== card.count(card[1])):
            type = 5 # Two pair
        else:
            type = 4 # Three of a kind
    elif 4 == len(setcard):  # One pair
        type = 6
    elif 5 == len(setcard):  # High card
        type = 7
    else:
        print('Unknown hand type:', card)

    return type

def Day7Pt2(inputfile):
    print('Day 7 Part 2')
    starttime = time.time()

    hands=[] #List()
    bids=[] #List()
    with open(inputfile) as file:
        for line in file:
            hand,bid = line.split()
            hand_orig = hand
            hand=hand.replace('A','F')
            hand=hand.replace('K','E')
            hand=hand.replace('Q','D')
            hand=hand.replace('J','1')
            hand=hand.replace('T','B')
            hands.append((hand,bid,GetType2(hand),hand_orig))

    #sort
    print("Start sorting")
    hands.sort(key=lambda x: x[0])
    hands.sort(key=lambda x: x[2], reverse=True)

    #sum
    print("Calc result")
    sum = 0
    i=1
    for _,bid,_,_ in hands:
        sum += i*int(bid)
        i +=1

    endtime = time.time()
    print('ended in:', endtime-starttime)
    #print(hands)
    print("res:",sum)
    print("End.")

def Day8Pt1(inputfile):
    print('Day 8 Part 1')
    start_time = time.time()

    instr = ""
    navi = {}
    with open(inputfile) as file:
        for line in file:
            if len(line) <=1:
                continue
            if 0==line.count("=") :
                instr = line.strip()
            else:
                start = line.split()[0]
                left = line.split()[2][1:-1]
                right = line.split()[3][:-1]
                navi[start]=(left,right)
    print(instr)
    print(navi)

    #navigate
    print("navi start")
    pos='AAA'
    i=0
    leni = len(instr)
    step=0
    while 'ZZZ' != pos:
        print(step, pos)
        nexti = instr[ i % leni]
        left_next, right_next = navi[pos]
        if 'L' == nexti:
            pos = left_next
        elif 'R' == nexti:
            pos = right_next

        step +=1
        i +=1 #end of while!!!

    end_time = time.time()
    print("steps:", step)
    print('ended in:', end_time-start_time)
    print("End.")

def Day8Pt2(inputfile):
    print('Day 8 Part 2')
    start_time = time.time()

    navi = {}
    starts=[]
    with open(inputfile) as file:
        for line in file:
            if len(line) <=1:
                continue
            if 0==line.count("=") :
                instr = line.strip()
            else:
                start = line.split()[0]
                if start.endswith("A"):
                    starts.append(start)
                left = line.split()[2][1:-1]
                right = line.split()[3][:-1]
                navi[start]=(left,right)
    print(instr)
    print(navi)

    #navigate
    print("navi start")
    pos=starts
    leni = len(instr)
    cycles=[]
    pi=0
    for p in pos:
        i = 0
        step = 0
        print(p, end=" ")
        finished = False
        while not finished:
            nexti = instr[i % leni]
            left_next, right_next = navi[pos[pi]]
            if 'L' == nexti:
                pos[pi] = left_next
            elif 'R' == nexti:
                pos[pi] = right_next
            if pos[pi].endswith('Z'):
                finished = True
            step +=1
            i +=1
        print("steps:", step)
        cycles.append(step)
        pi +=1

    lcmm = math.lcm(*cycles)
    print(f"The least common multiple of the given numbers is: {lcmm}")

    end_time = time.time()
    print('ended in:', end_time-start_time)
    print("End.")

def Day9Pt1(inputfile):
    print('Day 9 Part 1')
    start_time = time.time()

    with open(inputfile) as file:
        for line in file:
            pass

    end_time = time.time()
    print('ended in:', end_time-start_time)
    print("End.")

def Day9Pt2(inputfile):
    print('Day 9 Part 2')
    start_time = time.time()

    with open(inputfile) as file:
        for line in file:
            pass

    end_time = time.time()
    print('ended in:', end_time-start_time)
    print("End.")


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
    #Day5Pt1('input5.txt')
    #Day5Pt2('input5.txt')
    #Day6Pt1('input6.txt')
    #Day6Pt2('input6.txt')
    #Day7Pt1('input7.txt')
    #Day7Pt2('input7.txt')
    #Day8Pt1('input8.txt')
    #Day8Pt2('input8.txt')
    Day9Pt1('input9_.txt')
    #Day9Pt2('input9.txt')
