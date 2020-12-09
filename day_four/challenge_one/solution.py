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
		required.remove(cred.split(':')[0])
	if len(required) == 0:
		valids += 1
	elif len(required) == 1:
		if required[0] == 'cid':
			valids += 1 

print(valids)
