import json

with open('./in.json') as f:
	data = json.load(f)

seen = []

for num in data:
	if 2020 - num in seen:
		print(num * (2020 - num))
		break
	else:
		seen.append(num)
