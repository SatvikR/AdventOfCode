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

highest = 0
for seat in data:
	row = bin_row(0, 127, seat[:7], 0)
	col = bin_col(0, 7, seat[7:], 0)
	if row * 8 + col > highest:
		highest = row * 8 + col

print(highest)
