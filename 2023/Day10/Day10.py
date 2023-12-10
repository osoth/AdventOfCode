def is_valid_move(matrix, visited, row, col):
	return 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and not visited[row][col]


def dfs_with_distance(matrix, visited, row, col, start_row, start_col, prev_direction, dict, distance=0):
	opposite_direction = {"north": "south", "south": "north", "east": "west", "west": "east", None: None}
	# Check if we reached the start position again
	if row == start_row and col == start_col and distance > 0:
		return distance

	# Mark the current cell as visited
	visited[row][col] = True
	max_distance = distance

	# Get possible directions for the current symbol
	possible_directions = dict[matrix[row][col]]

	if possible_directions is not None:
		for new_direction in possible_directions:
			new_row, new_col = None, None
			# Calculate the new position based on the direction
			if new_direction == "north" and new_direction != opposite_direction[prev_direction]:
				new_row, new_col = row - 1, col
			elif new_direction == "south" and new_direction != opposite_direction[prev_direction]:
				new_row, new_col = row + 1, col
			elif new_direction == "east" and new_direction != opposite_direction[prev_direction]:
				new_row, new_col = row, col + 1
			elif new_direction == "west" and new_direction != opposite_direction[prev_direction]:
				new_row, new_col = row, col - 1
			if new_row is None or new_col is None:
				continue
			# Check if the move is valid and not going back
			if is_valid_move(matrix, visited, new_row, new_col) and new_direction != prev_direction:
				# Recursively call DFS for the next cell
				sub_distance = dfs_with_distance(matrix, visited, new_row, new_col, start_row, start_col, new_direction, dict, distance + 1)
				if sub_distance is None:
					sub_distance = max_distance
				# Update the maximum distance for the current cell
				max_distance = max(max_distance, sub_distance)

	# Backtrack: mark the current cell as not visited
		visited[row][col] = False
		return max_distance


def find_highest_distance_in_loop(matrix, start_symbol, dict):
	max_distance = 0
	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			if matrix[row][col] == start_symbol:
				visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
				distance = dfs_with_distance(matrix, visited, row, col, row, col, None, dict)
				max_distance = max(max_distance, distance)
	return max_distance


if __name__ == "__main__":
	dict = {
		"|": ("north", "south"),
		"-": ("east", "west"),
		"L": ("north", "east"),
		"7": ("south", "west"),
		"J": ("north", "east"),
		"F": ("south", "east"),
		"S": ("north", "south", "east", "west"),
		".": None
	}
	lines = []
	with open("Day10test.txt", "r") as f:
		for line in f:
			lines.append(line.rstrip("\n"))

	result = find_highest_distance_in_loop(lines, "S", dict)
	print(result)
