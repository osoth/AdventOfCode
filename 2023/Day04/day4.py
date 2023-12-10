def intersection(lst1, lst2):
	lst3 = [value for value in lst1 if value in lst2]
	return lst3


def calculate_total_cards(winning_cards):
	if len(winning_cards) == 0:
		return 0
	else:
		total_cards = len(winning_cards)  # Initial number of cards
		for i in range(len(winning_cards)):
			total_cards += calculate_total_cards(winning_cards[i+1:i + winning_cards[i] + 1])
		return total_cards


def card_to_list(card):
	# Card   1:  4 16 87 61 11 37 43 25 49 17 | 54 36 14 55 83 58 43 15 87 17 97 11 62 75 37  4 49 80 42 61 20 79 25 24 16
	# winners = [4, 16, 87, 61, 11, 37, 43, 25, 49, 17]
	# my_cards = [54, 36, 14, 55, 83, 58, 43, 15, 87, 17, 97, 11, 62, 75, 37,  4, 49, 80, 42, 61, 20, 79, 25, 24, 16]
	all = []
	for i in card:
		# find start of the winner's card
		# from ":" to "|" is the winner's card
		# split the winner and add them to winner
		combined = []
		split = i.replace(":", "|").split("|")
		winners = split[1].split()
		all_cards = split[2].split()
		combined.append(winners)
		combined.append(all_cards)
		all.append(combined)
	return all


def find_intersecttion(list):
	sum2 = 0
	sum3 = 0
	winners = []
	values = []
	for i in range(len(list)):
		value = intersection(list[i][0], list[i][1])
		i = 1
		winners.append(len(value))
		if len(value) == 0:
			i = 0
			values.append(i)
			continue
		for j in range(1, len(value)):
			i *= 2
		values.append(i)
		sum2 += i
	# when you have a winner with the value 0f 4 you win an extra card of the next 4 winners. if you win with the extra won cards you win an extra card of the next i winners and so on.
	print(calculate_total_cards(winners))
	return sum2


if __name__ == "__main__":
	# read in file and put every line as a list element
	deck = []
	with open('day4.txt') as f:
		for line in f:
			deck.append(line.rstrip('\n'))
	all_cards = card_to_list(deck)
	print(find_intersecttion(all_cards))
