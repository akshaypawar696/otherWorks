def avg(marks):
	assert len(marks) != 0,"List is empty."
	return sum(marks)/len(marks)

mark2 = [60,70]
print("Average2:",avg(mark2))

mark1 = []
print("Average1:",avg(mark1))
