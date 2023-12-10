if __name__ == "__main__":
	time = [60, 94, 78, 82]
	distance = [475, 2138, 1015, 1650]
	result = 1
	for i in range(len(time)):
		wins = 0
		for j in range(time[i]):
			if (time[i]-j) * j > distance[i]:
				wins += 1
		result *= wins
	print(result)

	wins2 = 0
	for i in range(60947882):
		if (60947882 - i)*i > 475213810151650:
			wins2 += 1
	print(wins2)
