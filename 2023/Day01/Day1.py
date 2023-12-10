



def findFirstandLastNumber(s):
	# find first and last number in a given string
	first = 0
	last = 0
	for i in range(len(s)):
		if s[i].isdigit():
			first = i
			break
	for i in range(len(s)-1, -1, -1):
		if s[i].isdigit():
			last = i
			break
	return s[first] + s[last]


if __name__ == "__main__":
	# load input1.txt and put every line as a list element
	input_list = []
	with open('input1.txt') as f:
		for line in f:
			input_list.append(line.rstrip('\n'))

	lst = []
	# find first and last number in a given string
	for i in range(len(input_list)):
		lst.append(findFirstandLastNumber(input_list[i]))

	sum = 0
	for i in range(len(lst)):
		sum += int(lst[i])
	print(sum)
