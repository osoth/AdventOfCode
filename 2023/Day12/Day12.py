from time import time
import re


dynamic_dict = {}


def dynamic_programming(line, value, line_index, value_index, current):
	key = (line_index, value_index, current)
	if key in dynamic_dict:
		return dynamic_dict[key]
	if line_index == len(line):
		if value_index == len(value) and current == 0:
			return 1
		elif value_index == len(value) - 1 and value[value_index] == current:
			return 1
		else:
			return 0
	ans = 0
	for c in ['.', '#']:
		if line[line_index] == c or line[line_index] == '?':
			if c == '.' and current == 0:
				ans += dynamic_programming(line, value, line_index + 1, value_index, 0)
			elif c == '.' and current > 0 and value_index < len(value) and value[value_index] == current:
				ans += dynamic_programming(line, value, line_index + 1, value_index + 1, 0)
			elif c == '#':
				ans += dynamic_programming(line, value, line_index + 1, value_index, current + 1)
	dynamic_dict[key] = ans
	return ans


def check_consecutive(s):
	result = [len(match) for match in re.findall(r'#+', s)]
	return result


def find_combinations_count(s, values):
	current_value1 = check_consecutive(s)
	questionmarks = s.count("?")
	if questionmarks == 0:
		return 1 if current_value1 == values else 0
	if sum(current_value1) > sum(values):
		return 0
	if (sum(values) - questionmarks) > sum(current_value1):
		return 0
	count = 0
	count += find_combinations_count(s.replace("?", ".", 1), values)
	count += find_combinations_count(s.replace("?", "#", 1), values)

	return count


if __name__ == "__main__":
	Lines = []
	Values = []
	with open("Day12.txt", "r") as f:
		for line in f:
			Lines.append(line.split()[0])
			Values.append([i for i in line.split()[1].split(",")])
	for g in range(len(Values)):
		Values[g] = [int(i) for i in Values[g]]
	sum1 = 0
	start_time = time()
	for i in range(len(Lines)):
		dynamic_dict.clear()
		sum1 += dynamic_programming(Lines[i], Values[i], 0, 0, 0)
	print(sum1)
	end_time = time()
	print("Time for Part 1: ", end_time - start_time)
	start_time = time()
	sum2 = 0
	for i in range(len(Lines)):
		p = Lines[i]
		for j in range(4):
			Lines[i] = Lines[i] + "?" + p
		s = Values[i]
		g = len(s)
		for p in range(4):
			Values[i] = Values[i] + s
	for i in range(len(Lines)):
		dynamic_dict.clear()
		sum2 += dynamic_programming(Lines[i], Values[i], 0, 0, 0)
	print(sum2)
	end_time = time()
	print("Time for Part 2: " + str(end_time - start_time))
