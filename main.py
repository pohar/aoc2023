import re
import time
from collections import Counter
from numba import jit
from numba.typed import List
import math
import networkx as nx
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point
from itertools import product

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
	def extend(s): #recursion
		i=0;
		diffs=[]
		for i in range(len(s)-1):
			diff = s[i+1] - s[i]
			diffs.append(diff)
		if all([v == 0 for v in s]):
			s.append(0)
			return 0
		else:
			s.append(s[-1]+extend(diffs))
		#print(s)
		return s[-1]

	print('Day 9 Part 1')
	start_time = time.time()

	sum=0
	with open(inputfile) as file:
		for line in file:
			nums = list(map(int,(line.split())))
			res=extend(nums)
			sum +=res
			print(f'input:{nums} : {res}')


	end_time = time.time()
	print("res:",sum)
	print('ended in:', end_time-start_time)
	print("End.")

def Day9Pt2(inputfile):
	def extend(s): #recursion
		i=0;
		diffs=[]
		for i in range(len(s)-1):
			diff = s[i+1] - s[i]
			diffs.append(diff)
		if all([v == 0 for v in s]):
			s.insert(0,1)
			return 0
		else:
			s.insert(0, s[0]-extend(diffs))
		#print(s)
		return s[0]

	print('Day 9 Part 2')
	start_time = time.time()

	sum=0
	with open(inputfile) as file:
		for line in file:
			nums = list(map(int,(line.split())))
			res=extend(nums)
			sum +=res
			print(f'input:{nums} : {res}')


	end_time = time.time()
	print("res:",sum)
	print('ended in:', end_time-start_time)
	print("End.")


def Day10Pt1(inputfile):
	print('Day 10 Part 1')
	start_time = time.time()

	with open(inputfile, 'r') as f:
		lines = f.readlines()
		f.close()

	GRID_SIZE_X = len(lines[0].strip())
	GRID_SIZE_Y = len(lines)
	print(f'Grid size: y: {GRID_SIZE_X} x: {GRID_SIZE_Y}')
	grid = [[0 for j in range(GRID_SIZE_X)] for i in range(GRID_SIZE_Y)]

	y=0
	for line in lines:
		x= line.find("S")
		if x>-1:
			startpos=(y,x)
		y+=1
	print('startpos',startpos)

	y = 0
	for line in lines:
		#map_object = map(char, line.rstrip())
		grid[y] = list(line.strip())
		if False:
			x=0
			for c in grid[y]:
				if '.' != c:
					G.add_node((y,x))
				if '|' == c:
					if(y-1>=0):
						G.add_edge((y,x),(y-1,x), weight=1)
					if(y+1<GRID_SIZE_Y):
						G.add_edge((y,x),(y+1,x), weight=1)
				if '-' == c:
					if(x-1>=0):
						G.add_edge((y,x),(y,x-1), weight=1)
					if(x+1<GRID_SIZE_X):
						G.add_edge((y,x),(y,x+1), weight=1)
				if 'L' == c:
					if (y - 1 >= 0):
						G.add_edge((y,x),(y-1,x), weight=1)
					if (x + 1 < GRID_SIZE_X):
						G.add_edge((y,x),(y,x+1), weight=1)
				if 'J' == c:
					if (y - 1 >= 0):
						G.add_edge((y,x),(y-1,x), weight=1)
					if (x - 1 >= 0):
						G.add_edge((y,x),(y,x-1), weight=1)
				if '7' == c:
					if(y+1<GRID_SIZE_Y):
						G.add_edge((y,x),(y+1,x), weight=1)
					if (x - 1 >= 0):
						G.add_edge((y,x),(y,x-1), weight=1)
				if 'F' == c:
					if(y+1<GRID_SIZE_Y):
						G.add_edge((y,x),(y+1,x), weight=1)
					if (x + 1 < GRID_SIZE_X):
						G.add_edge((y,x),(y,x+1), weight=1)
				if 'S' == c:
					if grid[y-1][x] in ['|', '7', 'F']: #connect north
						if (y - 1 >= 0):
							G.add_edge((y,x),(y-1,x), weight=1)
				if grid[y+1][x] in ['|', 'L', 'J']: #connect south
					if (y + 1 < GRID_SIZE_Y):
						G.add_edge((y,x),(y+1,x), weight=1)
				if grid[y+1][x] in ['-', 'L', 'F']: #connect west
					if (x - 1 >= 0):
						G.add_edge((y,x),(y,x-1), weight=1)
				if grid[y+1][x] in ['-', 'J', '7']: #connect east
					if (x + 1 < GRID_SIZE_Y):
						G.add_edge((y,x),(y,x+1), weight=1)
				x += 1
		y = y + 1

	res=0
	G = nx.Graph()
	print('startpos', startpos)
	G.add_node(startpos)
	y,x=startpos
	if(y-1>0):
		if grid[y - 1][x] in ['|', '7', 'F']:  # connect north
			G.add_edge((y, x), (y - 1, x), weight=1)
	if (y + 1 < GRID_SIZE_Y):
		if grid[y + 1][x] in ['|', 'L', 'J']:  # connect south
			G.add_edge((y, x), (y + 1, x), weight=1)
	if (x - 1 >= 0):
		if grid[y][x-1] in ['-', 'L', 'F']:  # connect west
			G.add_edge((y, x), (y, x - 1), weight=1)
	if (x + 1 < GRID_SIZE_X):
		if grid[y][x+1] in ['-', 'J', '7']:  # connect east
			G.add_edge((y, x), (y, x + 1), weight=1)

	print("histogram:",nx.degree_histogram(G))
	num_nodes_1_nbr = nx.degree_histogram(G)[1]
	print('num_nodes_1_nbr:',num_nodes_1_nbr)
	while nx.degree_histogram(G)[1] :
		for n in G.nodes():
			if( 1 == len(list(G.neighbors(n)))):
				#print("single: ",n)
				y,x = n
				c=grid[y][x]
				if '|' == c:
					if(y-1>=0):
						if (y-1,x) not in G.neighbors(n):
							G.add_edge((y,x),(y-1,x), weight=1)
					if(y+1<GRID_SIZE_Y):
						if (y +1, x) not in G.neighbors(n):
							G.add_edge((y,x),(y+1,x), weight=1)
				if '-' == c:
					if(x-1>=0):
						if (y, x-1) not in G.neighbors(n):
							G.add_edge((y,x),(y,x-1), weight=1)
					if(x+1<GRID_SIZE_X):
						if (y , x+1) not in G.neighbors(n):
							G.add_edge((y,x),(y,x+1), weight=1)
				if 'L' == c:
					if (y - 1 >= 0):
						if (y - 1, x) not in G.neighbors(n):
							G.add_edge((y,x),(y-1,x), weight=1)
					if (x + 1 < GRID_SIZE_X):
						if (y , x+1) not in G.neighbors(n):
							G.add_edge((y,x),(y,x+1), weight=1)
				if 'J' == c:
					if (y - 1 >= 0):
						if (y - 1, x) not in G.neighbors(n):
							G.add_edge((y,x),(y-1,x), weight=1)
					if (x - 1 >= 0):
						if (y , x+1) not in G.neighbors(n):
							G.add_edge((y,x),(y,x-1), weight=1)
				if '7' == c:
					if(y+1<GRID_SIZE_Y):
						if (y +1, x) not in G.neighbors(n):
							G.add_edge((y,x),(y+1,x), weight=1)
					if (x - 1 >= 0):
						if (y , x-1) not in G.neighbors(n):
							G.add_edge((y,x),(y,x-1), weight=1)
				if 'F' == c:
					if(y+1<GRID_SIZE_Y):
						if (y + 1, x) not in G.neighbors(n):
							G.add_edge((y,x),(y+1,x), weight=1)
					if (x + 1 < GRID_SIZE_X):
						if (y , x+1) not in G.neighbors(n):
							G.add_edge((y,x),(y,x+1), weight=1)
				if 'S' == c:
					pass
				break

	print("final histogram:",nx.degree_histogram(G))
	num_nodes_2_nbr = nx.degree_histogram(G)[2]
	print('num_nodes_2_nbr:',num_nodes_2_nbr)
	print("res", num_nodes_2_nbr/2)

	for n in G.nodes:
		#print('node: ',n,G.degree(n), list(G.neighbors(n)))
		pass

	if False:
		length = nx.single_source_shortest_path_length(G, startpos)
		for node in length:
			k = length[node]
			if k>res:
				res=k

	print('res:',res) #not 557, 437 is too low, 13734 not good

	end_time = time.time()
	print('ended in:', end_time-start_time)
	print("End.")


def Day10Pt2(inputfile):
	def areafunc(m):
		a = 0
		d=[]
		d.append(m[0])
		for i in range(len(m)-1):
			d.append(m[i+1]-m[i])
		print('m:',m)
		print('d:',d)
		return a

	print('Day 10 Part 2')
	start_time = time.time()

	with open(inputfile, 'r') as f:
		lines = f.readlines()
		f.close()

	GRID_SIZE_X = len(lines[0].strip())
	GRID_SIZE_Y = len(lines)
	print(f'Grid size: y: {GRID_SIZE_X} x: {GRID_SIZE_Y}')
	grid = [[0 for j in range(GRID_SIZE_X)] for i in range(GRID_SIZE_Y)]
	grid2 = [[0 for j in range(GRID_SIZE_X)] for i in range(GRID_SIZE_Y)]

	y=0
	for line in lines:
		x= line.find("S")
		if x>-1:
			startpos=(y,x)
		y+=1
	print('startpos',startpos)

	y = 0
	for line in lines:
		#map_object = map(char, line.rstrip())
		grid[y] = list(line.strip())
		if False:
			x=0
			for c in grid[y]:
				if '.' != c:
					G.add_node((y,x))
				if '|' == c:
					if(y-1>=0):
						G.add_edge((y,x),(y-1,x), weight=1)
					if(y+1<GRID_SIZE_Y):
						G.add_edge((y,x),(y+1,x), weight=1)
				if '-' == c:
					if(x-1>=0):
						G.add_edge((y,x),(y,x-1), weight=1)
					if(x+1<GRID_SIZE_X):
						G.add_edge((y,x),(y,x+1), weight=1)
				if 'L' == c:
					if (y - 1 >= 0):
						G.add_edge((y,x),(y-1,x), weight=1)
					if (x + 1 < GRID_SIZE_X):
						G.add_edge((y,x),(y,x+1), weight=1)
				if 'J' == c:
					if (y - 1 >= 0):
						G.add_edge((y,x),(y-1,x), weight=1)
					if (x - 1 >= 0):
						G.add_edge((y,x),(y,x-1), weight=1)
				if '7' == c:
					if(y+1<GRID_SIZE_Y):
						G.add_edge((y,x),(y+1,x), weight=1)
					if (x - 1 >= 0):
						G.add_edge((y,x),(y,x-1), weight=1)
				if 'F' == c:
					if(y+1<GRID_SIZE_Y):
						G.add_edge((y,x),(y+1,x), weight=1)
					if (x + 1 < GRID_SIZE_X):
						G.add_edge((y,x),(y,x+1), weight=1)
				if 'S' == c:
					if grid[y-1][x] in ['|', '7', 'F']: #connect north
						if (y - 1 >= 0):
							G.add_edge((y,x),(y-1,x), weight=1)
				if grid[y+1][x] in ['|', 'L', 'J']: #connect south
					if (y + 1 < GRID_SIZE_Y):
						G.add_edge((y,x),(y+1,x), weight=1)
				if grid[y+1][x] in ['-', 'L', 'F']: #connect west
					if (x - 1 >= 0):
						G.add_edge((y,x),(y,x-1), weight=1)
				if grid[y+1][x] in ['-', 'J', '7']: #connect east
					if (x + 1 < GRID_SIZE_Y):
						G.add_edge((y,x),(y,x+1), weight=1)
				x += 1
		y = y + 1

	res=0
	G = nx.Graph()
	print('startpos', startpos)
	G.add_node(startpos)
	y,x=startpos
	if(y-1>0):
		if grid[y - 1][x] in ['|', '7', 'F']:  # connect north
			G.add_edge((y, x), (y - 1, x), weight=1)
	if (y + 1 < GRID_SIZE_Y):
		if grid[y + 1][x] in ['|', 'L', 'J']:  # connect south
			G.add_edge((y, x), (y + 1, x), weight=1)
	if (x - 1 >= 0):
		if grid[y][x-1] in ['-', 'L', 'F']:  # connect west
			G.add_edge((y, x), (y, x - 1), weight=1)
	if (x + 1 < GRID_SIZE_X):
		if grid[y][x+1] in ['-', 'J', '7']:  # connect east
			G.add_edge((y, x), (y, x + 1), weight=1)

	print("histogram:",nx.degree_histogram(G))
	num_nodes_1_nbr = nx.degree_histogram(G)[1]
	print('num_nodes_1_nbr:',num_nodes_1_nbr)
	while nx.degree_histogram(G)[1] :
		for n in G.nodes():
			if( 1 == len(list(G.neighbors(n)))):
				#print("single: ",n)
				y,x = n
				c=grid[y][x]
				if '|' == c:
					if(y-1>=0):
						if (y-1,x) not in G.neighbors(n):
							G.add_edge((y,x),(y-1,x), weight=1)
					if(y+1<GRID_SIZE_Y):
						if (y +1, x) not in G.neighbors(n):
							G.add_edge((y,x),(y+1,x), weight=1)
				if '-' == c:
					if(x-1>=0):
						if (y, x-1) not in G.neighbors(n):
							G.add_edge((y,x),(y,x-1), weight=1)
					if(x+1<GRID_SIZE_X):
						if (y , x+1) not in G.neighbors(n):
							G.add_edge((y,x),(y,x+1), weight=1)
				if 'L' == c:
					if (y - 1 >= 0):
						if (y - 1, x) not in G.neighbors(n):
							G.add_edge((y,x),(y-1,x), weight=1)
					if (x + 1 < GRID_SIZE_X):
						if (y , x+1) not in G.neighbors(n):
							G.add_edge((y,x),(y,x+1), weight=1)
				if 'J' == c:
					if (y - 1 >= 0):
						if (y - 1, x) not in G.neighbors(n):
							G.add_edge((y,x),(y-1,x), weight=1)
					if (x - 1 >= 0):
						if (y , x+1) not in G.neighbors(n):
							G.add_edge((y,x),(y,x-1), weight=1)
				if '7' == c:
					if(y+1<GRID_SIZE_Y):
						if (y +1, x) not in G.neighbors(n):
							G.add_edge((y,x),(y+1,x), weight=1)
					if (x - 1 >= 0):
						if (y , x-1) not in G.neighbors(n):
							G.add_edge((y,x),(y,x-1), weight=1)
				if 'F' == c:
					if(y+1<GRID_SIZE_Y):
						if (y + 1, x) not in G.neighbors(n):
							G.add_edge((y,x),(y+1,x), weight=1)
					if (x + 1 < GRID_SIZE_X):
						if (y , x+1) not in G.neighbors(n):
							G.add_edge((y,x),(y,x+1), weight=1)
				if 'S' == c:
					pass
				break

	print("final histogram:",nx.degree_histogram(G))

	res=0
	for n in G.nodes():
		y,x = n
		grid2[y][x]=1

	pos= startpos
	nextpos = list(G.neighbors(startpos))[1]
	leng=1
	pts=[]
	pts.append(startpos)
	while nextpos!=startpos:
		leng +=1
		#print(pos)
		next = list(G.neighbors(nextpos))[0]
		if next==pos:
			next = list(G.neighbors(nextpos))[1]
		pos=nextpos
		nextpos=next
		pts.append(pos)

	poly = Polygon(pts)
	print('poly len:', poly.length, 'area:', poly.area )

	res=0
	for y in range(GRID_SIZE_Y):
		for x in range(GRID_SIZE_X):
			pp=Point(y, x)
			if(poly.contains(pp)):
				print(y,x)
				res += 1

	print('res:',res) #
	end_time = time.time()
	print('ended in:', end_time-start_time)


	print("End.")

def Day11Pt1(inputfile):
	print('Day 11 Part 1')
	start_time = time.time()

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
		if 0== grid[y].count('#'): #expand y
			y += 1
			grid.insert(y, list(line.strip()))
			GRID_SIZE_Y += 1
		y+=1

	#expand x
	for x in range(GRID_SIZE_X-1, 0, -1):
		alldot=True
		for y in range(GRID_SIZE_Y):
			if '.' != grid[y][x]:
				alldot = False
				break
		if alldot:
			for y in range(GRID_SIZE_Y):
				grid[y].insert(x,'.')
			GRID_SIZE_X += 1

	#find galaxies:
	galaxies=[]
	for y in range(GRID_SIZE_Y):
		for x in range(GRID_SIZE_X):
			if "#"==grid[y][x]:
				galaxies.append((y,x,1+len(galaxies)))

	print('gal:', galaxies)

	res=0
	#distances=dict()
	for i in range(len(galaxies)-1):
		bestdist=9999999
		for j in range(i+1, len(galaxies)):
			x1,y1,i1=galaxies[i]
			x2,y2,i2=galaxies[j]
			dist=abs(x1-x2)+abs(y1-y2)
			res += dist


	print('res:',res) #
	end_time = time.time()
	print('ended in:', end_time-start_time)


	print("End.")

def Day11Pt2(inputfile):
	print('Day 11 Part 2')
	start_time = time.time()

	with open(inputfile, 'r') as f:
		lines = f.readlines()
		f.close()

	GRID_SIZE_X = len(lines[0].strip())
	GRID_SIZE_Y = len(lines)
	print(f'Grid size: y: {GRID_SIZE_X} x: {GRID_SIZE_Y}')
	grid = [[0 for j in range(GRID_SIZE_X)] for i in range(GRID_SIZE_Y)]

	y = 0
	jumpy=[]
	for line in lines:
		#map_object = map(char, line.rstrip())
		grid[y] = list(line.strip())
		if 0== grid[y].count('#'): #expand y
			jumpy.append(y)
		y+=1
	print('jumpy:', jumpy)

	#expand x
	jumpx=[]
	for x in range(GRID_SIZE_X):
		alldot=True
		for y in range(GRID_SIZE_Y):
			if '.' != grid[y][x]:
				alldot = False
				break
		if alldot:
			jumpx.append(x)
	print('jumpx:', jumpx)

	#find galaxies:
	galaxies=[]
	for y in range(GRID_SIZE_Y):
		for x in range(GRID_SIZE_X):
			if "#"==grid[y][x]:
				galaxies.append((y,x,1+len(galaxies)))

	print('gal:', galaxies)

	res=0
	for i in range(len(galaxies)-1):
		for k in range(i+1, len(galaxies)):
			y1,x1,i1=galaxies[i]
			y2,x2,i2=galaxies[k]
			jumpsx=0
			for j in jumpx:
				if j>(min(x1,x2)) and j<max(x1,x2):
					jumpsx +=1
			jumpsy=0
			for j in jumpy:
				if j>(min(y1,y2)) and j<max(y1,y2):
					jumpsy +=1

			jumps = jumpsx+jumpsy
			dist=abs(x1-x2)+abs(y1-y2) + jumps * (1_000_000-1) #1_000_000
			#print(i+1, k+1, abs(x1-x2),abs(y1-y2), jumpsx,jumpsy ,dist)
			res += dist

	print('res:',res) #
	end_time = time.time()
	print('ended in:', end_time-start_time)


	print("End.")

def Day12Pt1(inputfile):
	def linechecker(cond, nfo):
		ret = False
		result = re.findall(r"([#]+)", cond)
		found_hash_groups = len(result)
		if found_hash_groups == len(nfo):
			partsok=True
			for i in range(found_hash_groups):
				if nfo[i]!= len(result[i]):
					partsok = False
			if partsok:
				ret = True
		return ret

	print('Day 12 Part 1')
	start_time = time.time()

	with open(inputfile, 'r') as f:
		lines = f.readlines()
		f.close()

	res=0
	for line in lines:
		dres=0
		condition = line.split()[0]
		info = list(map(int,line.split()[1].split(',')))
		print ('\n',condition, info)
		if 0 == condition.count('?'):
			ret = True
			print (condition, info, ret)
		else:
			nques = condition.count('?')
			missing_dots = len(condition) - sum(info)- condition.count(".")
			prod = list(product('#.', repeat=nques))
			for pp in prod:
				j = 0
				p = ''
				for item in pp:
					p = p + item
				if p.count('.') == missing_dots:
					test=''
					for i in range(len(condition)):
						if condition[i]!='?':
							test = test + condition[i]
						else:
							test = test + p[j]
							j +=1
					if linechecker(test, info):
						print(test)
						res += 1
						dres +=1
		print (condition, info,  dres)

	print('res:',res) #
	end_time = time.time()
	print('ended in:', end_time-start_time)



def linechecker(cond, nfo):
	ret = False
	result = re.findall(r"([#]+)", cond)
	found_hash_groups = len(result)
	if found_hash_groups == len(nfo):
		partsok=True
		for i in range(found_hash_groups):
			if nfo[i]!= len(result[i]):
				partsok = False
				break
		if partsok:
			ret = True
	return ret

def generate_combinations(prefix, n, m, cond, nfo, reres):
	if n == 0 and m == 0:
		j = 0
		test=''
		for i in range(len(cond)):
			if cond[i]!='?':
				test = test + cond[i]
			else:
				test = test + prefix[j]
				j +=1
		if True == linechecker(test, nfo):
			reres += 1
		return reres
	if n > 0:
		reres = generate_combinations(prefix + '#', n - 1, m, cond, nfo, reres)
	if m > 0:
		reres = generate_combinations(prefix + '.', n, m - 1, cond, nfo, reres )

	return reres

def generate_all_cases(N, M, cond, nfo):
	reres = generate_combinations('', N, M,  cond, nfo, 0)
	return reres

def Day12Pt2(inputfile):
	print('Day 12 Part 2')
	start_time = time.time()

	with open(inputfile, 'r') as f:
		lines = f.readlines()
		f.close()

	res=0
	ind=0
	for line in lines:
		line_start_time = time.time()

		# N = 1
		condition = line.split()[0] # + '?' + line.split()[0] + '?' +  line.split()[0] + '?' +  line.split()[0] + '?' + line.split()[0]
		info = list(map(int,line.split()[1].split(',')))
		nques = condition.count('?')
		missing_dots = len(condition) - sum(info)- condition.count(".") # expectedFailure() num of new dots
		missing_ques = nques - missing_dots
		dres = generate_all_cases(missing_ques, missing_dots, condition, info)

		# N=2
		condition = line.split()[0] + '?' + line.split()[0] # + '?' +  line.split()[0] + '?' +  line.split()[0] + '?' + line.split()[0]
		info = list(map(int,line.split()[1].split(',')) )* 2
		nques = condition.count('?')
		missing_dots = len(condition) - sum(info)- condition.count(".") # expectedFailure() num of new dots
		missing_ques = nques - missing_dots
		eres = generate_all_cases(missing_ques, missing_dots, condition, info)

		mult = eres/dres
		fres = int(dres * mult ** 4)

		res +=fres
		line_end_time = time.time()
		print(ind,'res', res, 'fres',fres,'line ended in:', line_end_time - line_start_time)
		ind +=1

	print('res:',res) #
	end_time = time.time()
	print('ended in:', end_time-start_time)

def Day13Pt1(inputfile):
	def ColumnsEqual(area, x1, x2, maxy):
		is_ok = True
		for y in range(maxy):
			if area[y][x1] != area[y][x2]:
				is_ok = False
				break
		return is_ok

	def RowsEqual(area, y1, y2, maxx):
		is_ok = True
		if area[y1]!= area[y2]:
			is_ok = False
		return is_ok

	print('Day 13 Part 1')
	start_time = time.time()

	with open(inputfile, 'r') as f:
		lines = f.readlines()
		f.close()

	if False:
		GRID_SIZE_X = len(lines[0].strip())
		GRID_SIZE_Y = len(lines)
		print(f'Grid size: y: {GRID_SIZE_X} x: {GRID_SIZE_Y}')
		grid = [[0 for j in range(GRID_SIZE_X)] for i in range(GRID_SIZE_Y)]

	starty = 0
	grid=[]
	res=0
	for y,line in enumerate(lines):
		if len(line)>1:
			grid.append( list(line.strip()))
		else:
			vmirr=[]
			hmirr=[]
			GRID_SIZE_X = len(grid[0])
			GRID_SIZE_Y = len(grid)
			print(f'Grid size: y: {GRID_SIZE_X} x: {GRID_SIZE_Y}')

			#find vertical mirror (without using mirror)
			for x1 in range(GRID_SIZE_X-1):
				x2=x1+1
				if ColumnsEqual(grid, x1, x2, GRID_SIZE_Y):
					x3=x1-1
					x4=x2+1
					ok=True
					while(x3>=0) and (x4<GRID_SIZE_X) and ok:
						if ColumnsEqual(grid, x3, x4, GRID_SIZE_Y):
							x3 -=  1
							x4 += 1
						else:
							ok=False
					if ok:
						res += x1+1
						vmirr.append(x1)
			print("vmirr:", vmirr)

			#find vertical mirror (without using mirror)
			for y1 in range(GRID_SIZE_Y-1):
				y2=y1+1
				if RowsEqual(grid, y1, y2, GRID_SIZE_X):
					y3=y1-1
					y4=y2+1
					ok=True
					while(y3>=0) and (y4<GRID_SIZE_Y) and ok:
						if RowsEqual(grid, y3, y4, GRID_SIZE_X):
							y3 -=  1
							y4 += 1
						else:
							ok=False
					if ok:
						res += (y1+1)*100
						hmirr.append(y1)
			print("hmirr:", hmirr)

			grid = []

	print('res:',res) #
	end_time = time.time()
	print('ended in:', end_time-start_time)


def Day13Pt2(inputfile):
	def ColumnsDiff(area, x1, x2, maxy):
		diff = 0
		for y in range(maxy):
			if area[y][x1] != area[y][x2]:
				diff +=1
		return diff

	def RowsDiff(area, y1, y2, maxx):
		diff = 0
		for x in range(maxx):
			if area[y1][x] != area[y2][x]:
				diff +=1
		return diff

	print('Day 13 Part 2')
	start_time = time.time()

	with open(inputfile, 'r') as f:
		lines = f.readlines()
		f.close()

	if False:
		GRID_SIZE_X = len(lines[0].strip())
		GRID_SIZE_Y = len(lines)
		print(f'Grid size: y: {GRID_SIZE_X} x: {GRID_SIZE_Y}')
		grid = [[0 for j in range(GRID_SIZE_X)] for i in range(GRID_SIZE_Y)]

	starty = 0
	grid=[]
	res=0
	for y,line in enumerate(lines):
		if len(line)>1:
			grid.append( list(line.strip()))
		else:
			vmirr=[]
			hmirr=[]
			GRID_SIZE_X = len(grid[0])
			GRID_SIZE_Y = len(grid)
			print(f'Grid size: y: {GRID_SIZE_X} x: {GRID_SIZE_Y}')

			#find vertical mirror (without using mirror)
			for x1 in range(GRID_SIZE_X-1):
				x2=x1+1
				sumd=0
				x3=x1
				x4=x2
				ok=True
				while(x3>=0) and (x4<GRID_SIZE_X) and ok :
					d=ColumnsDiff(grid, x3, x4, GRID_SIZE_Y)
					x3 -=  1
					x4 += 1
					if d>0:
						sumd += d
						if sumd>1:
							ok=False
				if 1==sumd:
					res += x1+1
					vmirr.append(x1)
			print("vmirr:", vmirr)

			#find horizontal mirror (without using mirror)
			for y1 in range(GRID_SIZE_Y-1):
				y2=y1+1
				sumd=0
				y3=y1
				y4=y2
				ok=True
				while(y3>=0) and (y4<GRID_SIZE_Y) and ok:
					d =RowsDiff(grid, y3, y4, GRID_SIZE_X)
					y3 -=  1
					y4 += 1
					if d>0:
						sumd += d
						if sumd>1:
							ok=False
				if 1==sumd:
					res += (y1+1)*100
					hmirr.append(y1)
			print("hmirr:", hmirr)

			grid = []

	print('res:',res)  # too low: 29112
	end_time = time.time()
	print('ended in:', end_time-start_time)

def Day14Pt1(inputfile):
	def printgrid(grid_, x1, y1, x2, y2):
		for y in range(y1, y2 ):
			for x in range(x1, x2 ):
				print(grid_[y][x], end="")
			print("")
		return

	def MoveRocks(area,x,y):
		if (0==x) and (-1==y): # move north
			for y in range(GRID_SIZE_Y-1):
				for x in range(GRID_SIZE_X):
					ym=y
					while ('.'==grid[ym][x]) and (ym<GRID_SIZE_Y-1):
						ym += 1
					if (ym!=y) and ('O'==grid[ym][x]):
						grid[y][x]='O'
						grid[ym][x]='.'
		return

	print('Day 14 Part 1')
	start_time = time.time()

	with open(inputfile, 'r') as f:
		lines = f.readlines()
		f.close()

	GRID_SIZE_X = len(lines[0].strip())
	GRID_SIZE_Y = len(lines)
	print(f'Grid size: y: {GRID_SIZE_X} x: {GRID_SIZE_Y}')
	grid = [[0 for j in range(GRID_SIZE_X)] for i in range(GRID_SIZE_Y)]
	y=0
	for line in lines:
		grid[y] = list(line.strip())
		y+=1
	#printgrid(grid,0,0, GRID_SIZE_X, GRID_SIZE_Y)

	MoveRocks(grid,0,-1)
	print("Move North")
	#printgrid(grid,0,0, GRID_SIZE_X, GRID_SIZE_Y)

	res=0
	for y in range(GRID_SIZE_Y):
		subres = grid[y].count('O') * (GRID_SIZE_Y-y)
		#print(subres)
		res += subres

	print('res:',res)
	end_time = time.time()
	print('ended in:', end_time-start_time)



def MoveRocks(grid,GRID_SIZE_X,GRID_SIZE_Y):
	# move north
	for y in range(GRID_SIZE_Y - 1):
		for x in range(GRID_SIZE_X):
			ym = y
			while ('.' == grid[ym][x]) and (ym < GRID_SIZE_Y - 1):
				ym += 1
			if (ym != y) and ('O' == grid[ym][x]):
				grid[y][x] = 'O'
				grid[ym][x] = '.'

	# move west
	for x in range(GRID_SIZE_X-1):
		for y in range(GRID_SIZE_Y):
			xm=x
			while ('.'==grid[y][xm]) and (xm<GRID_SIZE_X-1):
				xm += 1
			if (xm!=x) and ('O'==grid[y][xm]):
				grid[y][x]='O'
				grid[y][xm]='.'

	# move south
	for y in range(GRID_SIZE_Y-1,0,-1):
		for x in range(GRID_SIZE_X):
			ym=y
			while ('.'==grid[ym][x]) and (ym>0):
				ym -= 1
			if (ym!=y) and ('O'==grid[ym][x]):
				grid[y][x]='O'
				grid[ym][x]='.'

	#east
	for x in range(GRID_SIZE_X-1,0,-1):
		for y in range(GRID_SIZE_Y):
			xm=x
			while ('.'==grid[y][xm]) and (xm>0):
				xm -= 1
			if (xm!=x) and ('O'==grid[y][xm]):
				grid[y][x]='O'
				grid[y][xm]='.'
	return
def Day14Pt2(inputfile):
	def printgrid(grid_, x1, y1, x2, y2):
		for y in range(y1, y2 ):
			for x in range(x1, x2 ):
				print(grid_[y][x], end="")
			print("")
		return

	print('Day 14 Part 2')
	start_time = time.time()

	with open(inputfile, 'r') as f:
		lines = f.readlines()
		f.close()

	GRID_SIZE_X = len(lines[0].strip())
	GRID_SIZE_Y = len(lines)
	print(f'Grid size: y: {GRID_SIZE_X} x: {GRID_SIZE_Y}')
	#grid = [[0 for j in range(GRID_SIZE_X)] for i in range(GRID_SIZE_Y)]
	grid=list()
	y=0
	for line in lines:
		grid.append(list(line.strip()))
		y+=1
	#printgrid(grid,0,0, GRID_SIZE_X, GRID_SIZE_Y)

	states = []
	i=0
	while i <1_000_000_000:
		currstate=hash(tuple(map(tuple, grid)))
		if currstate not in states:
			states.append(currstate)
			MoveRocks(grid,GRID_SIZE_X,GRID_SIZE_Y)
			i += 1
		else:
			ind = states.index(currstate)
			print("found earlier state:" , i, " ==" , ind)
			cyclen=i-ind
			#while (i+cyclen) < 1_000_000_000:
			#	i+=cyclen
			i = (1_000_000_000 + ind - (1_000_000_000 % cyclen) - cyclen)
			states.clear() #hack
			print("new i:", i)

	#calculate result
	res=0
	for y in range(GRID_SIZE_Y):
		subres = grid[y].count('O') * (GRID_SIZE_Y-y)
		#print(subres)
		res += subres

	print('res:',res) #118747
	end_time = time.time()
	print('ended in:', end_time-start_time)

def Day15Pt1(inputfile):
	print('Day 15 Part 1')
	start_time = time.time()

	with open(inputfile, 'r') as f:
		lines = f.readlines()
		f.close()

	res = 0
	for line in lines:
		parts = line.strip().split(',')
		for part in parts:
			currentvalue = 0
			for c in part:
				currentvalue += ord(c)
				currentvalue *= 17
				currentvalue = 	currentvalue % 256
			#print(part, currentvalue)
			res += currentvalue

	print('res:',res)
	end_time = time.time()
	print('ended in:', end_time-start_time)


def Day15Pt2(inputfile):
	print('Day 15 Part 2')
	start_time = time.time()

	with open(inputfile, 'r') as f:
		lines = f.readlines()
		f.close()

	#boxes= {} * 256
	boxes = [{} for i in range(256)]
	for line in lines:
		parts = line.strip().split(',')
		for part in parts:
			currentvalue = 0
			if part.count('-'):
				mykey = part[:-1]
			else:
				mykey,_ = part.split('=')
			for c in mykey:
				currentvalue += ord(c)
				currentvalue *= 17
				currentvalue = 	currentvalue % 256
			#print(part, currentvalue)
			if part.count('-'):
				if mykey in boxes[currentvalue].keys():
					boxes[currentvalue].pop(mykey)
			else:
				_,value = part.split('=')
				#print(currentvalue,mykey)
				boxes[currentvalue][mykey] = value

	res=0
	print("boxes:", boxes)
	slotindex=1
	prevbox=-1
	for i,box in enumerate(boxes):
		for key in box:
			boxno = i+1
			if (prevbox!=-1) and (boxno!=prevbox):
				slotindex = 1

			focallen = box[key]
			subres = int(boxno) * slotindex * int(focallen)
			print(key, subres)
			res += subres
			slotindex +=1
			prevbox = boxno

	print('res:',res)
	end_time = time.time()
	print('ended in:', end_time-start_time)

def Day16Pt1(inputfile):
	def printgrid(grid_, x1, y1, x2, y2):
		for y in range(y1, y2 ):
			for x in range(x1, x2 ):
				print('#' if (x,y) in grid_ else'.', end="")
			print("")
		return

	print('Day 16 Part 1')
	start_time = time.time()

	with open(inputfile, 'r') as f:
		lines = f.readlines()
		f.close()

	GRID_SIZE_X = len(lines[0].strip())
	GRID_SIZE_Y = len(lines)
	print(f'Grid size: y: {GRID_SIZE_X} x: {GRID_SIZE_Y}')
	#grid = [[0 for j in range(GRID_SIZE_X)] for i in range(GRID_SIZE_Y)]
	grid=list()
	for line in lines:
		grid.append(list(line.rstrip()))

	#dirs 0=right, 1 = down, 2,=left, 3 = up
	beams=[]
	energized={}
	visited={}
	beams.append((0,0,0)) # x,y,dir
	while beams:
		newbeams=[]
		for i  in range(len(beams)):
			x,y,dir = beams[i]
			energized[(x,y)]=1
			bounced = False
			if '.' == grid[y][x]:
				if 0 == dir:
					x += 1
				elif 2 == dir:
					x -= 1
				elif 1 == dir:
					y += 1
				elif 3 == dir:
					y -= 1
			elif '/' == grid[y][x]:
				if 0 == dir:
					dir = 3
					y -= 1
				elif 2 == dir:
					dir = 1
					y += 1
				elif 1 == dir:
					dir = 2
					x -= 1
				elif 3 == dir:
					dir  = 0
					x += 1
			elif "\\" == grid[y][x]:
				if 0 == dir:
					dir = 1
					y += 1
				elif 2 == dir:
					dir = 3
					y -= 1
				elif 1 == dir:
					dir = 0
					x += 1
				elif 3 == dir:
					dir  = 2
					x -= 1
			elif "|" == grid[y][x]:
				if (0 == dir) or (2 ==dir):
					bounced = True
					if not((y-1 < 0) or (x < 0) or (y-1 >= GRID_SIZE_Y) or (x >= GRID_SIZE_X)):
						newbeams.append((x,y-1,3)) #bounce
					if not ((y+1 < 0) or (x < 0) or (y+1 >= GRID_SIZE_Y) or (x >= GRID_SIZE_X)):
						newbeams.append((x , y+1, 1))  # bounce
				elif 1 == dir:
					y += 1
				elif 3 == dir:
					y -= 1
			elif "-" == grid[y][x]:
				if 0 == dir:
					x += 1
				elif 2 == dir:
					x -= 1
				elif (1 == dir) or (3 == dir):
					bounced = True
					if not((y < 0) or (x-1 < 0) or (y >= GRID_SIZE_Y) or (x-1 >= GRID_SIZE_X)):
						newbeams.append((x-1 , y, 2))  # bounce new ray
					if not((y < 0) or (x+1 < 0) or (y >= GRID_SIZE_Y) or (x+1 >= GRID_SIZE_X)):
						newbeams.append((x+1 , y, 0))  # bounce

			if not((y<0) or (x<0) or (y>=GRID_SIZE_Y) or (x>=GRID_SIZE_X)) and not bounced:
				newbeams.append((x,y,dir)) # remain active
		beams=[]
		for nb in newbeams:
			if nb not in visited:
				visited[nb]=1
				beams.append(nb)
		#printgrid(energized, 0, 0, GRID_SIZE_X, GRID_SIZE_Y)
		#print(10 * '=')
		#print(beams) #, energized)

	res = len(energized)

	print('res:',res)
	end_time = time.time()
	print('ended in:', end_time-start_time)

def Day16Pt2(inputfile):
	def printgrid(grid_, x1, y1, x2, y2):
		for y in range(y1, y2 ):
			for x in range(x1, x2 ):
				print('#' if (x,y) in grid_ else'.', end="")
			print("")
		return

	print('Day 16 Part 2')
	start_time = time.time()

	with open(inputfile, 'r') as f:
		lines = f.readlines()
		f.close()

	GRID_SIZE_X = len(lines[0].strip())
	GRID_SIZE_Y = len(lines)
	print(f'Grid size: y: {GRID_SIZE_X} x: {GRID_SIZE_Y}')
	#grid = [[0 for j in range(GRID_SIZE_X)] for i in range(GRID_SIZE_Y)]
	grid=list()
	for line in lines:
		grid.append(list(line.rstrip()))

	#dirs 0=right, 1 = down, 2,=left, 3 = up
	res = 0
	for startx in range(GRID_SIZE_X):
		subres = method_name(startx, 0, 1, GRID_SIZE_X, GRID_SIZE_Y, grid)
		if subres > res:
			res = subres

		subres = method_name(startx, GRID_SIZE_Y-1, 3, GRID_SIZE_X, GRID_SIZE_Y, grid)
		if subres > res:
			res = subres

	for starty in range(GRID_SIZE_Y):
		subres = method_name(0, starty, 1, GRID_SIZE_X, GRID_SIZE_Y, grid)
		if subres > res:
			res = subres

		subres = method_name(GRID_SIZE_X-1, starty, 3, GRID_SIZE_X, GRID_SIZE_Y, grid)
		if subres > res:
			res = subres

	print('res:',res)
	end_time = time.time()
	print('ended in:', end_time-start_time)


def method_name(sx,sy,sdir, GRID_SIZE_X, GRID_SIZE_Y, grid):
	beams = []
	energized = {}
	visited = {}
	beams.append((sx, sy, sdir))  # x,y,dir
	visited[(sx, sy, sdir)]=1
	while beams:
		newbeams = []
		for i in range(len(beams)):
			x, y, dir = beams[i]
			energized[(x, y)] = 1
			bounced = False
			if '.' == grid[y][x]:
				if 0 == dir:
					x += 1
				elif 2 == dir:
					x -= 1
				elif 1 == dir:
					y += 1
				elif 3 == dir:
					y -= 1
			elif '/' == grid[y][x]:
				if 0 == dir:
					dir = 3
					y -= 1
				elif 2 == dir:
					dir = 1
					y += 1
				elif 1 == dir:
					dir = 2
					x -= 1
				elif 3 == dir:
					dir = 0
					x += 1
			elif "\\" == grid[y][x]:
				if 0 == dir:
					dir = 1
					y += 1
				elif 2 == dir:
					dir = 3
					y -= 1
				elif 1 == dir:
					dir = 0
					x += 1
				elif 3 == dir:
					dir = 2
					x -= 1
			elif "|" == grid[y][x]:
				if (0 == dir) or (2 == dir):
					bounced = True
					if not ((y - 1 < 0) or (x < 0) or (y - 1 >= GRID_SIZE_Y) or (x >= GRID_SIZE_X)):
						newbeams.append((x, y - 1, 3))  # bounce
					if not ((y + 1 < 0) or (x < 0) or (y + 1 >= GRID_SIZE_Y) or (x >= GRID_SIZE_X)):
						newbeams.append((x, y + 1, 1))  # bounce
				elif 1 == dir:
					y += 1
				elif 3 == dir:
					y -= 1
			elif "-" == grid[y][x]:
				if 0 == dir:
					x += 1
				elif 2 == dir:
					x -= 1
				elif (1 == dir) or (3 == dir):
					bounced = True
					if not ((y < 0) or (x - 1 < 0) or (y >= GRID_SIZE_Y) or (x - 1 >= GRID_SIZE_X)):
						newbeams.append((x - 1, y, 2))  # bounce new ray
					if not ((y < 0) or (x + 1 < 0) or (y >= GRID_SIZE_Y) or (x + 1 >= GRID_SIZE_X)):
						newbeams.append((x + 1, y, 0))  # bounce

			if not ((y < 0) or (x < 0) or (y >= GRID_SIZE_Y) or (x >= GRID_SIZE_X)) and not bounced:
				newbeams.append((x, y, dir))  # remain active
		beams = []
		for nb in newbeams:
			if nb not in visited:
				visited[nb] = 1
				beams.append(nb)
	res = len(energized)
	return res

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
	#Day9Pt1('input9.txt')
	#Day9Pt2('input9.txt')
	#Day10Pt1('input10.txt')
	#Day10Pt2('input10.txt')
	#Day11Pt1('input11.txt')
	#Day11Pt2('input11.txt')
	#Day12Pt1('input12_.txt')
	#Day12Pt2('input12.txt') # not working
	#Day13Pt1('input13.txt')
	#Day13Pt2('input13.txt')
	#Day14Pt1('input14.txt')
	#Day14Pt2('input14.txt')
	#Day15Pt1('input15.txt')
	#Day15Pt2('input15.txt')
	#Day16Pt1('input16.txt')
	Day16Pt2('input16.txt')
