import problem
import re 

passports = problem.pps.split('\n\n')

valids = 0

for ppt in passports:
	creds = re.split(' |\n', ppt)
	required = [
		'byr', 
		'iyr', 
		'eyr', 
		'hgt', 
		'hcl', 
		'ecl', 
		'pid', 
		'cid' 
	]

	if '' in creds:
		creds.remove('')

	for cred in creds:
		p = cred.split(':')
		curr = p[0]
		val = p[1]

		if curr == 'byr':
			if not (1920 <= int(val) <= 2020):
				break	
		elif curr == 'iyr':
			if not (2010 <= int(val) <= 2020):
				break	
		elif curr == 'eyr':
			if not (2020 <= int(val) <= 2030):
				break
		elif curr == 'hgt':
			mes = val[-2:]
			if mes != 'cm' and mes != 'in':
				break
			if mes == 'cm':
				if not (150 <= int(val[:-2]) <= 193):
					break
			if mes == 'in':
				if not (59 <= int(val[:-2]) <= 76):
					break
		elif curr == 'hcl':
			if val[0] != '#' or len(val) != 7:
				break
			failed = False
			
			try:
				_ = int(''.join(val[1:]), 16)
			except:
				failed = True
			if failed:
				break
		elif curr == 'ecl':
			if val not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
				break
		elif curr == 'pid':
			if len(val) != 9:
				break
			failed = False
			try:
				_ = int(val)
			except:
				failed = True
			if failed:
				break
		required.remove(cred.split(':')[0])
		
	if len(required) == 0:
		valids += 1
	elif len(required) == 1:
		if required[0] == 'cid':
			valids += 1 

print(valids)
