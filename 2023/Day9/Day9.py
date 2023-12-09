'''

Solutions for Part 1 and 2 for Day9 Advent of Code 2023
Oskar Soth

'''



def calc_next_value(list):
	L = []
	L.append(list)
	while True:
		last = L[-1]
		current = []
		for i in range(len(last)-1):
			current.append(last[i+1]-last[i])
		L.append(current)
		if sum(current) == 0:
			break
	# traverse backwards
	tmp = 0
	for i in range(len(L)-1, 0, -1):
		tmp = tmp + L[i-1][-1]
	return tmp

def calc_new_first_value(list):
	L = []
	L.append(list)
	while True:
		last = L[-1]
		current = []
		for i in range(len(last)-1):
			current.append(last[i+1]-last[i])
		L.append(current)
		if sum(current) == 0:
			break
	tmp = 0
	for i in range(len(L)-1, 0, -1):
		tmp = L[i-1][0] - tmp
	return tmp


if __name__ == "__main__":
	with open("Day9.txt", "r") as f:
		i = 0
		table = []
		for line in f:
			a = [int(x) for x in line.rstrip("\n").split()]
			table.append(a)

	result = 0
	for i in range(len(table)):
		result += calc_next_value(table[i])
	print(result)

	result2 = 0
	for i in range(len(table)):
		result2 += calc_new_first_value(table[i])
	print(result2)
