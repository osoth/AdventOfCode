import re


def parse_game_string(game_string):
	# Extract game_id and color information using regular expressions
	match = re.match(r"Game (\d+): (.+)", game_string)

	if not match:
		raise ValueError("Invalid input format")

	game_id = int(match.group(1))
	color_data = match.group(2)

	# Initialize the result list with game_id
	result = [[game_id]]

	# Split color data into individual segments
	segments = color_data.split(";")

	for segment in segments:
		# Extract color values using regular expressions
		color_match = re.findall(r"(\d+) (\w+)", segment)

		# Initialize a dictionary to store color values
		color_dict = {"red": 0, "green": 0, "blue": 0}

		# Update color values based on the extracted data
		for count, color in color_match:
			color_dict[color.lower()] = int(count)

		# Append the color values to the result list
		result.append([color_dict["red"], color_dict["green"], color_dict["blue"]])

	return result



def check_game_possible(game, possible):
	for i in range(1, len(game)):
		if game[i][0] > possible[0]:
			return 0
		if game[i][1] > possible[1]:
			return 0
		if game[i][2] > possible[2]:
			return 0
	return game[0][0]

def find_fewest_colors(game):
	red = 0
	green = 0
	blue = 0
	for i in range(1, len(game)):
		if game[i][0] > red:
			red = game[i][0]
		if game[i][1] > green:
			green = game[i][1]
		if game[i][2] > blue:
			blue = game[i][2]
	print(red, green, blue)
	return [red, green, blue]

if __name__ == "__main__":
	games = []
	with open('day2.txt') as f:
		for line in f:
			line = line.rstrip('\n')
			games.append(parse_game_string(line))
	possible = [12, 13, 14]
	sum = 0
	lowest_colors = [0, 0, 0]
	power_sum = 0
	for game in games:
		lowest_colors = find_fewest_colors(game)
		power_sum += lowest_colors[0] * lowest_colors[1] * lowest_colors[2]

	print(power_sum)





