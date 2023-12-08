import time
import sys
from math import gcd


def lcm(list):
	result = 1
	for i in list:
		result = result * i // gcd(result, i)
	return result


def convert_table_to_dictionary(input_list):
	result_dict = {}

	for item in input_list:
		# Split the string into key and values
		key, values_str = item.split(' = ')
		key = key.strip()

		# Extract values within parentheses and convert them into a tuple
		values = tuple(value.strip() for value in values_str[1:-1].split(','))

		# Add key-value pair to the dictionary
		result_dict[key] = values

	return result_dict


def steps_start_finish(dict, header, start, finish):
	i = 0
	current = start
	while True:
		for j in header:
			if j == "L":
				current = dict[current][0]
			if j == "R":
				current = dict[current][1]
			i += 1
			if current == finish:
				return i


def steps_start_finish_2(dict, header, starts):
	i = 0
	current = starts
	positions = []
	all = []
	while True:
		if len(positions) > 1:
			return positions
		for j in header:
			if j == "L":
				current = dict[current][0]
			if j == "R":
				current = dict[current][1]
			i += 1
			if current[2] == 'Z':
				return i


if __name__ == "__main__":
	header = ""
	lines = []
	with open("Day8.txt", "r") as f:
		i = 0
		for line in f:
			if i == 0:
				header += line.rstrip("\n")
				i += 1
			elif i > 1:
				lines.append(line.rstrip("\n"))
			else:
				i += 1
	dict = convert_table_to_dictionary(lines)

	'''
	Part 1
	'''
	print("Solution Part 1: " + str(steps_start_finish(dict, header, 'AAA', 'ZZZ')))


	'''
	Part 2:
	'''
	starts = [key for key in dict.keys() if key[2] == 'A']
	all_of_them = []
	for i in range(len(starts)):
		all_of_them.append(steps_start_finish_2(dict, header, starts[i]))
	print("Solution Part 2: " + str(lcm(all_of_them)))

