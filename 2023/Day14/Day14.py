import numpy as np
from tqdm import tqdm

def move_O_to_right(matrix):
	rows = len(matrix)
	cols = len(matrix[0])

	for i in range(rows):
		for j in range(cols - 2, -1, -1):
			if matrix[i][j] == 'O':
				# Check if there is a '#' in the way to the right
				k = j + 1
				while k < cols and matrix[i][k] != '#':
					matrix[i][k], matrix[i][k - 1] = matrix[i][k - 1], matrix[i][k]
					k += 1


if __name__ == "__main__":
	lines = []
	with open("Day14test.txt") as f:
		for line in f:
			lines.append(line.strip())
	lines = [list(i) for i in lines]

	mat = np.array(lines)
	mat = np.rot90(mat, 3)
	move_O_to_right(mat)
	#print(mat)
	result = 0
	for i in range(len(mat)):
		for j in range(len(mat[0])):
			if mat[i][j] == 'O':
				result += j+1
	#print(result)
	mat2 = np.array(lines)
	test_mat = np.array(lines)
	print(test_mat)
	test_mat = np.rot90(test_mat, 3)
	move_O_to_right(test_mat)
	print(test_mat)
	test_mat = np.rot90(test_mat, 3)
	move_O_to_right(test_mat)
	print(test_mat)
	test_mat = np.rot90(test_mat, 3)
	move_O_to_right(test_mat)
	print(test_mat)
	test_mat = np.rot90(test_mat, 3)
	move_O_to_right(test_mat)
	print(test_mat)
	i = 0
	while True:
		if i > 1 and np.array_equal(mat2, test_mat):
			break
		if i%10000 == 0:
			print(i)
		mat2 = np.rot90(mat2, 3)
		move_O_to_right(mat2)
		mat2 = np.rot90(mat2, 3)
		move_O_to_right(mat2)
		mat2 = np.rot90(mat2, 3)
		move_O_to_right(mat2)
		mat2 = np.rot90(mat2, 3)
		move_O_to_right(mat2)
		i += 1
	print(i)

