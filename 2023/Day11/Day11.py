from itertools import combinations


def get_coordinates(list):
	coords = []
	for i in range(len(list)):
		for j in range(len(list[i])):
			if list[i][j] == "#":
				coords.append((i, j))
	return coords


def find_empty_columns(cluster):
	temp = []
	for i in range(len(cluster)):
		for j in range(len(cluster[i])):
			if all(cluster[b][j] == "." for b in range(len(cluster))):
				temp.append(j)
	return temp


def find_empty_rows(cluster):
	temp = []
	for i in range(len(cluster)):
		if all(cluster[i][b] == "." for b in range(len(cluster[i]))):
			temp.append(i)
	return temp


def change_coordinates(coordinates, empty_rows, empty_columns, faktor):
	# Convert coordinates to a list of lists
	coordinates = [list(coord) for coord in coordinates]

	# Change the coordinates based on the number of empty rows and columns
	for i in range(len(coordinates)):
		if any(row < coordinates[i][0] for row in empty_rows):
			coordinates[i][0] += len([row for row in empty_rows if row < coordinates[i][0]]) * faktor
		if any(column < coordinates[i][1] for column in empty_columns):
			coordinates[i][1] += len([column for column in empty_columns if column < coordinates[i][1]]) * faktor

	# Convert coordinates back to a list of tuples
	coordinates = [tuple(coord) for coord in coordinates]

	return coordinates


def find_shortest_distance(pair):
	# Unpack the coordinate pairs
	coord1, coord2 = pair

	# Mathe 2 lässt Grüßen (Manhattan-Metrik)
	distance = abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

	return distance


def generate_coordinate_pairs(coordinates):
	# Use combinations to generate all possible pairs
	pairs = list(combinations(coordinates, 2))

	# Convert the pairs to a list of coordinates
	combined_coordinates = [((coord1), (coord2)) for coord1, coord2 in pairs]

	return combined_coordinates


if __name__ == "__main__":
	cluster = []
	with open("Day11.txt", "r") as f:
		for line in f:
			cluster.append(line.strip())
	empty_rows = find_empty_rows(cluster)
	empty_columns = find_empty_columns(cluster)
	empty_columns = set(empty_columns)
	empty_columns = list(empty_columns)
	coordinates = get_coordinates(cluster)
	changed_coordinates1 = change_coordinates(coordinates, empty_rows, empty_columns, 1)
	coordinate_pairs = generate_coordinate_pairs(changed_coordinates1)
	sum1 = 0
	for pair in coordinate_pairs:
		sum1 += find_shortest_distance(pair)
	print("Part 1:", sum1)
	changed_coordinates2 = change_coordinates(coordinates, empty_rows, empty_columns, 999999)
	coordinate_pairs = generate_coordinate_pairs(changed_coordinates2)
	sum2 = 0
	for pair in coordinate_pairs:
		sum2 += find_shortest_distance(pair)
	print("Part 2:", sum2)
