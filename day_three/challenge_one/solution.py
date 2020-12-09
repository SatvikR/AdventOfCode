import json

with open('../in.json') as f:
	data = json.load(f)


row = 0
col = 0

total = 0

while row <= len(data) - 1:
	if data[row][col % len(data[row])] == '#':
		total += 1	
	row += 1
	col += 3

print(total)
