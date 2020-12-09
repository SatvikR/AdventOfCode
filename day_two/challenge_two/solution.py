import json

with open('../in.json') as f:
	data = json.load(f)

class Password(object):
	def __init__(self, code_min, code_max, char, code):
		self.min = code_min
		self.max = code_max
		self.char = char
		self.code = code
	@staticmethod
	def create_password(text):
		parts = text.split(' ')
		code_range = parts[0].split('-')
		code_letter = parts[1][0]
		code_text = parts[2]
		return Password(int(code_range[0]), int(code_range[1]), 
				code_letter, code_text)

total = 0
for code in data:
	valid_pos = 0
	curr = Password.create_password(code)
	if curr.code[curr.min-1] == curr.char:
		valid_pos += 1
	if curr.code[curr.max-1] == curr.char:
		valid_pos += 1
	if valid_pos == 1:
		total += 1

print(total)
	
