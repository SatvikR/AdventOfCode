import json
import math

with open('../in.json') as f:
	data = json.load(f)

def bin_row(min, max, text, i):
	if i == len(text):
		return min
	if text[i] == 'F':
		return bin_row(min, math.floor((min + max) / 2), text, i + 1) 
	if text[i] == 'B':
		return bin_row(math.ceil((min + max) / 2), max, text, i + 1)
	

def bin_col(min, max, text, i):
	if i == len(text):
		return min
	if text[i] == 'L':
		return bin_col(min, math.floor((min + max) / 2), text, i + 1) 
	if text[i] == 'R':
		return bin_col(math.ceil((min + max) / 2), max, text, i + 1)

taken = []

for seat in data:
	row = bin_row(0, 127, seat[:7], 0)
	col = bin_col(0, 7, seat[7:], 0)
	taken.append((row * 8) + col)

empty = []
for i in range(0, 128):
	for j in range(0, 8):
		if i * 8 + j not in taken:
			empty.append(i * 8 + j)

for seat in empty:
	if seat - 1 in taken and seat + 1 in taken:
		print(seat)
		break


