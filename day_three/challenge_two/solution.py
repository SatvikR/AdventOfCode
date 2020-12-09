import json

with open('../in.json') as f:
	data = json.load(f)


slopes = [
	[1, 1],
	[3, 1],
	[5, 1],
	[7, 1],
	[1, 2]
]

totals = 1

for slope in slopes:
	row = 0
	col = 0

	total = 0
	while row <= len(data) - 1:
		if data[row][col % len(data[row])] == '#':
			total += 1	
		row += slope[1]
		col += slope[0]
	totals *= total

print(totals)
