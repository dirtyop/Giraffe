a = ["32 + 698", "2 - 3801", "45 + 43", "123 + 49"]
line1 = ""
line2 = ""
for b in a:
	c = b.split()
	#print(c)
	n1 = c[0]
	op = c[1]
	n2 = c[2]
	space = max(len(n1), len(n2))
	line1 += n1.rjust(space + 2)
	line2 += op.rjust(space) + n2

print(line1)
print(line2)
