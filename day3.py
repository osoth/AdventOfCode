def gear_ration(block):
	# a gear ratio is the product of two numbers that are adjacent to a "*" symbol
	# find the sum of all gear ratios in the block
	sum = 0
	for i in range(len(block)):
		for j in range(len(block[i])):
			if block[i][j] == "*":




def find_adjecent_seats(block):
	sum = 0
	for i in range(len(block)):
		j = 0
		while j < len(block[i]):
			if block[i][j].isdigit():
				# print block from i, j until there is no digit
				g = j
				first = j
				while j < len(block[i]) and block[i][j].isdigit():
					j += 1
					continue
				last = j -1
				adjacent_symbol = False
				if i == 0:
					if ((32 < ord(block[i][first - 1]) < 48) or (57 < ord(block[i][last + 1]) < 65) or (90 < ord(block[i][last + 1]) < 97) or (122 < ord(block[i][last + 1]) < 127)) and ord(block[i][first -1]) != 46 and ord(block[i][last + 1]) != 46:
						adjacent_symbol = True
					elif ((32 < ord(block[i+1][first - 1]) < 48) or (57 < ord(block[i+1][last + 1]) < 65) or (90 < ord(block[i+1][last + 1]) < 97) or (122 < ord(block[i+1][last + 1]) < 127)) and ord(block[i+1][first -1]) != 46 and ord(block[i+1][last + 1]) != 46:
						adjacent_symbol = True
					elif ((32 < ord(block[i+1][first]) < 48) or (57 < ord(block[i+1][last]) < 65) or (90 < ord(block[i+1][last]) < 97) or (122 < ord(block[i+1][last]) < 127)) and ord(block[i+1][first]) != 46 and ord(block[i+1][last]) != 46:
						adjacent_symbol = True
					elif ((32 < ord(block[i+1][first + 1]) < 48) or (57 < ord(block[i+1][last - 1]) < 65) or (90 < ord(block[i+1][last - 1]) < 97) or (122 < ord(block[i+1][last - 1]) < 127)) and ord(block[i+1][first + 1]) != 46 and ord(block[i+1][last - 1]) != 46:
						adjacent_symbol = True
					# now for last
					elif ((32 < ord(block[i][last + 1]) < 48) or (57 < ord(block[i][last + 1]) < 65) or (90 < ord(block[i][last + 1]) < 97) or (122 < ord(block[i][last + 1]) < 127)) and ord(block[i][last + 1]) != 46:
						adjacent_symbol = True
					elif ((32 < ord(block[i+1][last + 1]) < 48) or (57 < ord(block[i+1][last + 1]) < 65) or (90 < ord(block[i+1][last + 1]) < 97) or (122 < ord(block[i+1][last + 1]) < 127)) and ord(block[i+1][last + 1]) != 46:
						adjacent_symbol = True
					elif ((32 < ord(block[i+1][last]) < 48) or (57 < ord(block[i+1][last]) < 65) or (90 < ord(block[i+1][last]) < 97) or (122 < ord(block[i+1][last]) < 127)) and ord(block[i+1][last]) != 46:
						adjacent_symbol = True
					elif ((32 < ord(block[i+1][last - 1]) < 48) or (57 < ord(block[i+1][last - 1]) < 65) or (90 < ord(block[i+1][last - 1]) < 97) or (122 < ord(block[i+1][last - 1]) < 127)) and ord(block[i+1][last - 1]) != 46:
						adjacent_symbol = True
				if i == len(block) - 1:
					if ((32 < ord(block[i][first - 1]) < 48) or (57 < ord(block[i][first -1]) < 65) or (90 < ord(block[i][first -1]) < 97) or (122 < ord(block[i][first -1]) < 127)) and ord(block[i][first -1]) != 46:
						adjacent_symbol = True
					elif ((32 < ord(block[i-1][first - 1]) < 48) or (57 < ord(block[i-1][first -1]) < 65) or (90 < ord(block[i-1][first -1]) < 97) or (122 < ord(block[i-1][first -1]) < 127)) and ord(block[i-1][first -1]) != 46:
						adjacent_symbol = True
					elif ((32 < ord(block[i-1][first]) < 48) or (57 < ord(block[i-1][first]) < 65) or (90 < ord(block[i-1][first]) < 97) or (122 < ord(block[i-1][first]) < 127)) and ord(block[i-1][first]) != 46:
						adjacent_symbol = True
					elif ((32 < ord(block[i-1][first + 1]) < 48) or (57 < ord(block[i-1][first + 1]) < 65) or (90 < ord(block[i-1][first + 1]) < 97) or (122 < ord(block[i-1][first + 1]) < 127)) and ord(block[i-1][first + 1]) != 46:
						adjacent_symbol = True
					# now for last
					elif ((32 < ord(block[i][last + 1]) < 48) or (57 < ord(block[i][last + 1]) < 65) or (90 < ord(block[i][last + 1]) < 97) or (122 < ord(block[i][last + 1]) < 127)) and ord(block[i][last + 1]) != 46:
						adjacent_symbol = True
					elif ((32 < ord(block[i-1][last + 1]) < 48) or (57 < ord(block[i-1][last + 1]) < 65) or (90 < ord(block[i-1][last + 1]) < 97) or (122 < ord(block[i-1][last + 1]) < 127)) and ord(block[i-1][last + 1]) != 46:
						adjacent_symbol = True
					elif ((32 < ord(block[i-1][last]) < 48) or (57 < ord(block[i-1][last]) < 65) or (90 < ord(block[i-1][last]) < 97) or (122 < ord(block[i-1][last]) < 127)) and ord(block[i-1][last]) != 46:
						adjacent_symbol = True
					elif ((32 < ord(block[i-1][last - 1]) < 48) or (57 < ord(block[i-1][last - 1]) < 65) or (90 < ord(block[i-1][last - 1]) < 97) or (122 < ord(block[i-1][last - 1]) < 127)) and ord(block[i-1][last - 1]) != 46:
						adjacent_symbol = True

				else:
					if ((32 < ord(block[i][first - 1]) < 48) or (57 < ord(block[i][first -1]) < 65) or (90 < ord(block[i][first -1]) < 97) or (122 < ord(block[i][first -1]) < 127)) and ord(block[i][first -1]) != 46:
						adjacent_symbol = True
					elif ((32 < ord(block[i+1][first - 1]) < 48) or (57 < ord(block[i+1][first -1]) < 65) or (90 < ord(block[i+1][first -1]) < 97) or (122 < ord(block[i+1][first -1]) < 127)) and ord(block[i+1][first -1]) != 46:
						adjacent_symbol = True
					elif ((32 < ord(block[i+1][first]) < 48) or (57 < ord(block[i+1][first]) < 65) or (90 < ord(block[i+1][first]) < 97) or (122 < ord(block[i+1][first]) < 127)) and ord(block[i+1][first]) != 46:
						adjacent_symbol = True
					elif ((32 < ord(block[i+1][first + 1]) < 48) or (57 < ord(block[i+1][first + 1]) < 65) or (90 < ord(block[i+1][first + 1]) < 97) or (122 < ord(block[i+1][first + 1]) < 127)) and ord(block[i+1][first + 1]) != 46:
						adjacent_symbol = True
					# now for last
					elif ((32 < ord(block[i][last + 1]) < 48) or (57 < ord(block[i][last + 1]) < 65) or (90 < ord(block[i][last + 1]) < 97) or (122 < ord(block[i][last + 1]) < 127)) and ord(block[i][last + 1]) != 46:
						adjacent_symbol = True
					elif ((32 < ord(block[i+1][last + 1]) < 48) or (57 < ord(block[i+1][last + 1]) < 65) or (90 < ord(block[i+1][last + 1]) < 97) or (122 < ord(block[i+1][last + 1]) < 127)) and ord(block[i+1][last + 1]) != 46:
						adjacent_symbol = True
					elif ((32 < ord(block[i+1][last]) < 48) or (57 < ord(block[i+1][last]) < 65) or (90 < ord(block[i+1][last]) < 97) or (122 < ord(block[i+1][last]) < 127)) and ord(block[i+1][last]) != 46:
						adjacent_symbol = True
					elif ((32 < ord(block[i+1][last - 1]) < 48) or (57 < ord(block[i+1][last - 1]) < 65) or (90 < ord(block[i+1][last - 1]) < 97) or (122 < ord(block[i+1][last - 1]) < 127)) and ord(block[i+1][last - 1]) != 46:
						adjacent_symbol = True
					# and for i-1 for both
					elif ((32 < ord(block[i-1][first - 1]) < 48) or (57 < ord(block[i-1][first -1]) < 65) or (90 < ord(block[i-1][first -1]) < 97) or (122 < ord(block[i-1][first -1]) < 127)) and ord(block[i-1][first -1]) != 46:
						adjacent_symbol = True
					elif ((32 < ord(block[i-1][first]) < 48) or (57 < ord(block[i-1][first]) < 65) or (90 < ord(block[i-1][first]) < 97) or (122 < ord(block[i-1][first]) < 127)) and ord(block[i-1][first]) != 46:
						adjacent_symbol = True
					elif ((32 < ord(block[i-1][first + 1]) < 48) or (57 < ord(block[i-1][first + 1]) < 65) or (90 < ord(block[i-1][first + 1]) < 97) or (122 < ord(block[i-1][first + 1]) < 127)) and ord(block[i-1][first + 1]) != 46:
						adjacent_symbol = True
					# now for last
					elif ((32 < ord(block[i-1][last + 1]) < 48) or (57 < ord(block[i-1][last + 1]) < 65) or (90 < ord(block[i-1][last + 1]) < 97) or (122 < ord(block[i-1][last + 1]) < 127)) and ord(block[i-1][last + 1]) != 46:
						adjacent_symbol = True
					elif ((32 < ord(block[i-1][last]) < 48) or (57 < ord(block[i-1][last]) < 65) or (90 < ord(block[i-1][last]) < 97) or (122 < ord(block[i-1][last]) < 127)) and ord(block[i-1][last]) != 46:
						adjacent_symbol = True
					elif ((32 < ord(block[i-1][last - 1]) < 48) or (57 < ord(block[i-1][last - 1]) < 65) or (90 < ord(block[i-1][last - 1]) < 97) or (122 < ord(block[i-1][last - 1]) < 127)) and ord(block[i-1][last - 1]) != 46:
						adjacent_symbol = True
				if adjacent_symbol:
					print(block[i][first:last+1])
					sum += int(block[i][first:last+1])
			else:
				j += 1
				continue
	return sum


if __name__ == "__main__":
	block = []
	with open("day3.txt", "r") as f:
		lines = f.readlines()
		for line in lines:
			block.append(line.strip())
	print(find_adjecent_seats(block))


