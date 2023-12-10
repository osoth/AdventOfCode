

def findFirstandLastNumber(s, dict):


	# find first and last number in a given string but this time, the numbers can also be written in words

	first = 0
	last = 0
	for i in range(len(s)):
		if s[i].isdigit():
			first = s[i]
			break
		if s[i:i+3] in dict:
			first = dict[s[i:i+3]]
			break
		if s[i:i+4] in dict:
			first = dict[s[i:i+4]]
			break
		if s[i:i+5] in dict:
			first = dict[s[i:i+5]]
			break

	for i in range(len(s)-1, -1, -1):
		if s[i].isdigit():
			last = s[i]
			break
		if s[i:i+3] in dict:
			last = dict[s[i:i+3]]
			break
		if s[i:i+4] in dict:
			last = dict[s[i:i+4]]
			break
		if s[i:i+5] in dict:
			last = dict[s[i:i+5]]
			break
	return first + last



if __name__ == "__main__":
	# load input1.txt and put every line as a list element
	dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

	input_list = []
	with open('input1.txt') as f:
		for line in f:
			input_list.append(line.rstrip('\n'))
	print(len(input_list))
	lst = []
	# find first and last number in a given string
	for i in range(len(input_list)):
		lst.append(findFirstandLastNumber(input_list[i], dict))
	sum = 0
	print(len(lst))
	for i in range(len(lst)):
		print(lst[i])
		sum += int(lst[i])
	print(sum)
