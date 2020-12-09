import problem

forms = problem.questions.split('\n\n')

total = 0

for form in forms:
	ind_forms = form.split('\n')
	seen = {}
	for res in ind_forms:
		for i in res:
			if i in seen:
				seen[i] += 1
			else:
				seen[i] = 1
	for a, b in seen.items():
		if b == len(ind_forms):
			total += 1
	
print(total)
