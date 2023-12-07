# Day 7 of Advent Of Code 2023 // Oskar Soth
cards_to_value = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3,
                  "2": 2}
hand_to_value = {"5": 7, "4": 6, "F": 5, "3": 4, "2P": 3, "1P": 2, "H": 1}


def check_FiveOfKind(deck):
	s = set(deck[0])
	if len(s) == 1:
		return ["5", deck]
	return None


def check_FourAndFullHouse(deck):
	s = set(deck[0])
	if len(s) == 2:
		for i in s:
			if deck[0].count(i) == 4:
				return ["4", deck]
			elif deck[0].count(i) == 3:
				return ["F", deck]
	return None


def check_ThreeAndTwoPairs(deck):
	s = set(deck[0])
	if len(s) == 3:
		for i in s:
			if deck[0].count(i) == 3:
				return ["3", deck]
			elif deck[0].count(i) == 2:
				return ["2P", deck]
	return None


def check_OnePair(deck):
	s = set(deck[0])
	if len(s) == 4 or len(s) == 5:
		for i in s:
			if deck[0].count(i) == 2:
				return ["1P", deck]
		return ["H", deck]


def sortCards(deck):
	for b in range(1, len(deck)):
		key = deck[b]
		j = b - 1

		# Sort by hand_to_value and cards_to_value
		while j >= 0 and (hand_to_value[key[0]] < hand_to_value[deck[j][0]] or (hand_to_value[key[0]] == hand_to_value[deck[j][0]] and cards_to_value_compare(deck[j][1][0], key[1][0]) == -1)):
			deck[j + 1] = deck[j]
			j -= 1
		deck[j + 1] = key

	return deck


def cards_to_value_compare(cards1, cards2):
	for p in range(5):
		if cards_to_value[cards1[p]] < cards_to_value[cards2[p]]:
			return 1
		elif cards_to_value[cards1[p]] > cards_to_value[cards2[p]]:
			return -1
	return 0



if __name__ == "__main__":
	L = [["32T3K", 765], ["T55J5", 684], ["KK677", 28], ["KTJJT", 220], ["QQQJA", 483]]
	input_list = []
	A = []
	B = []
	with open('day7.txt', 'r') as f:
		for line in f:
			splt = line.rstrip('\n').split(" ")
			splt[1] = int(splt[1])
			input_list.append(splt)

	for g in range(len(L)):
		if check_FiveOfKind(L[g]):
			B.append(check_FiveOfKind(L[g]))
		elif check_FourAndFullHouse(L[g]):
			B.append(check_FourAndFullHouse(L[g]))
		elif check_ThreeAndTwoPairs(L[g]):
			B.append(check_ThreeAndTwoPairs(L[g]))
		elif check_OnePair(L[g]):
			B.append(check_OnePair(L[g]))

	X = sortCards(B)
	sum1 = 0
	for j in range(len(X)):
		sum1 += (j + 1) * X[j][1][1]
	print(sum1)

	for i in range(len(input_list)):
		if check_FiveOfKind(input_list[i]):
			A.append(check_FiveOfKind(input_list[i]))
		elif check_FourAndFullHouse(input_list[i]):
			A.append(check_FourAndFullHouse(input_list[i]))
		elif check_ThreeAndTwoPairs(input_list[i]):
			A.append(check_ThreeAndTwoPairs(input_list[i]))
		elif check_OnePair(input_list[i]):
			A.append(check_OnePair(input_list[i]))
	Z = sortCards(A)
	# print(Z)
	sum = 0
	p = []
	for j in range(len(Z)):
		p.append(Z[j][1][1])
		sum += (j + 1) * Z[j][1][1]
	# print(sum)
	result = 0
	for index, value in enumerate(p):
		result += (index + 1) * value
	# print(str(index+1) + "*" + str(value) + "=" + str((index + 1) * value))

	print(result)
