import json

with open('./in.json') as f:
	data = json.load(f)

seen = []

for num in data:
	for i in seen:
		if 2020 - i - num in seen:
			print(num * i * (2020 - i - num))
			break
	seen.append(num)
