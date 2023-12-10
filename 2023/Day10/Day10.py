import sys
from shapely.geometry import Polygon, Point
from time import time

'''
Ugliest Solution ever by Oskar Soth @ University of Potsdam
Not Proud!!!
'''
sys.setrecursionlimit(50000)
directions = {
	"|": ("north", "south"),
	"-": ("east", "west"),
	"L": ("north", "east"),
	"7": ("south", "west"),
	"J": ("north", "west"),
	"F": ("south", "east"),
	"S": ("north", "south", "east", "west"),
	".": None
}


def is_valid_move(x, y, visited):
	return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and (x, y) not in visited


def dfs(x, y, visited, current_path, start_position):
	visited.add((x, y))
	loops = []
	current_path.append((x, y))
	loops.append(current_path)
	if maze[x][y] == ".":
		return []

	if (x, y) == start_position and len(current_path) > 1:
		# Found a loop, terminate the path
		return [current_path]
	elif (x, y) in current_path[:-1]:
		# Found a revisited position, terminate the path
		return [current_path[current_path.index((x, y)):]]

	for direction in directions.get(maze[x][y], []):
		dx, dy = 0, 0
		if direction == "north":
			dx = -1
		elif direction == "south":
			dx = 1
		elif direction == "east":
			dy = 1
		elif direction == "west":
			dy = -1

		new_x, new_y = x + dx, y + dy

		if is_valid_move(new_x, new_y, visited):
			loops.extend(dfs(new_x, new_y, visited.copy(), current_path.copy(), start_position))
	return loops


def find_biggest_loop(start_x, start_y):
	visited = set()
	current_path = []
	loops = dfs(start_x, start_y, visited, current_path, (start_x, start_y))
	if loops:
		biggest_loop = max(loops, key=len)
		return biggest_loop
	else:
		return None


if __name__ == "__main__":
	start_time = time()
	with open("Day10.txt", "r") as f:
		maze = [list(line.strip()) for line in f.readlines()]
	start_position = [(i, row.index("S")) for i, row in enumerate(maze) if "S" in row][0]

	# Find the biggest loop starting from the "S" position
	result = find_biggest_loop(*start_position)
	if len(result) % 2 == 0:
		print("Aufgabe 1: "+ str(len(result)//2))
	else:
		print("Aufgabe 1: "+ str(len(result)//2 + 1))
	poly = Polygon(result)
	sum = 0
	for i in range(140):
		for j in range(140):
			if poly.contains(Point(i, j)):
				sum += 1
	print("Aufgabe 2: " + str(sum))
	end_time = time()
	print("Runtime: " + str(end_time - start_time))
