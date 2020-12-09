import problem

forms = problem.questions.split('\n\n')

total = 0

for form in forms:
	letters = [i for i in form if i != '\n']
	seen = set({})
	_ = [seen.add(i) for i in letters]
	total += len(seen)
print(total)
