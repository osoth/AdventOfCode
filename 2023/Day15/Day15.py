def find_hash_subset(s):
	i = 0
	j = 0
	while j < len(s):
		p = ord(s[j])
		i += p
		i *= 17
		i = i % 256
		j += 1
	return i


def split_substrings(s):
	q = s.split("-")
	p = s.split("=")
	if len(p) == 1:
		return q[0]
	else:
		return [p[0] , int(p[1])]


if __name__ == "__main__":
	L = []
	with open("Day15.txt") as f:
		for line in f:
			L = line.strip().split(",")
	result = 0
	for i in L:
		result += find_hash_subset(i)
	print(result)
	boxes = [[] for i in range(256)]
	for i in range(len(L)):
		a = split_substrings(L[i])
		if type(a) == list:
			# Find the index of the sublist with the same first value
			index_to_replace = None
			for index, j in enumerate(boxes[find_hash_subset(a[0])]):
				if j[0] == a[0]:
					index_to_replace = index
					break

			# Replace the old sublist if it exists, otherwise append the new one
			if index_to_replace is not None:
				boxes[find_hash_subset(a[0])][index_to_replace] = [a[0], a[1]]
			else:
				boxes[find_hash_subset(a[0])].append([a[0], a[1]])
		else:
			for j in boxes[find_hash_subset(a)]:
				if j[0] == a:
					boxes[find_hash_subset(a)].remove(j)
	result2 = 0
	for i in range(len(boxes)):
		for j in range(len(boxes[i])):
			result2 += (i+1)*(j+1)*boxes[i][j][1]
	print(result2)

