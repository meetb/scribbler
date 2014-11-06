from random import randint

a = {}
for i in range(0, 9):
	a[i] = '_';

combs=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def drawGrid():
	for i in range(0,3):
		print '|',
		print a[i],
	print '|'
	for i in range(3,6):
		print '|',
		print a[i],
	print '|'
	for i in range(6,9):
		print '|',
		print a[i],
	print '|'

def gridComplete():
	for i in range(0,9):
		if a[i] != 'X' or a[i] != 'O':
			return 0
	return 1

def win():
	for comb in combs:
		if a[comb[0]] == a[comb[1]] == a[comb[2]] =='X':
			return 'X'
		elif a[comb[0]] == a[comb[1]] == a[comb[2]] == 'O':
			return 'O'
	return 0;

def twoLeft():
	for comb in combs:
		if a[comb[0]] == a[comb[1]] and a[comb[2]] == '_':
			if a[comb[0]] == 'O':
				return [comb[2], 'O']
			elif a[comb[0]] == 'X':
				return [comb[2], 'X']
		elif a[comb[1]] == a[comb[2]] and a[comb[0]] == '_':
			if a[comb[1]] == 'O':
				return [comb[0], 'O']
			elif a[comb[1]] == 'X':
				return [comb[0], 'X']
		elif a[comb[2]] == a[comb[0]] and a[comb[1]] == '_':
			if a[comb[2]] == 'O':
				return [comb[1], 'O']
			elif a[comb[2]] == 'O':
				return [comb[1], 'O']
	return [-1, '_']

while(gridComplete()==0):
	flag = 0
	while(flag==0):
		n1 = raw_input("Player 1\n >")
		n1 = int(n1)
		if a[n1] == '_':
			flag = 1
	a[n1] = 'X'
	drawGrid()
	if(win()!=0):
		print "Player 1 wins"
		break
	flag = 0
	print("Player 2's turn")
	while flag==0:
		n2 = randint(0,8)
		if a[n2] == '_':
			flag = 1
	a[n2] = 'O'
	drawGrid()
	if(win()!=0):
		print "Player 2 wins"
		break

if win() == 'X':
	print "Player 1 wins"
elif win() == 'O':
	print "Player 2 wins"
	