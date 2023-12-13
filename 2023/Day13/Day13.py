import numpy as np


def is_symmetric(matrix):
	symetry_list = []
	symetry_true = [[False for i in range(len(matrix))] for j in range(len(matrix[0])-1)]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])-1):
			if matrix[i][j] == matrix[i][j+1]:
				symetry_true[j][i] = True
	# find the index of all sublists of symetry_true where the whole list is true:
	for g in range(len(symetry_true)):
		if len(set(symetry_true[g])) == 1 and symetry_true[g][0] == True:
			symetry_list.append(g)
	# check whole canditate list for symetry
	for i in range(len(symetry_list)):
		# split the matrix into two parts at the index of the column in symetry_list
		matrix1 = [matrix[j][:symetry_list[i]+1] for j in range(len(matrix))]
		matrix2 = [matrix[j][symetry_list[i]+1:] for j in range(len(matrix))]
		size = min(len(matrix1[0]), len(matrix2[0]))
		matrix1 = [list(g) for g in matrix1]
		matrix1 = np.array(matrix1)
		matrix1 = np.fliplr(matrix1)
		matrix1 = matrix1.tolist()
		matrix1 = ["".join(g) for g in matrix1]
		is_sym = True
		for j in range(len(matrix1)):
			for z in range(size):
				if matrix1[j][z] != matrix2[j][z]:
					is_sym = False
					break
		if is_sym == True:
			return symetry_list[i]+1

	#rows
	symetry_list = []
	symetry_true = [[False for i in range(len(matrix[0]))] for j in range(len(matrix)-1)]
	for i in range(len(matrix)-1):
		for j in range(len(matrix[0])):
			if matrix[i][j] == matrix[i+1][j]:
				symetry_true[i][j] = True
	# find the index of all sublists of symetry_true where the whole list is true:
	for g in range(len(symetry_true)):
		if len(set(symetry_true[g])) == 1 and symetry_true[g][0] == True:
			symetry_list.append(g)
	for i in symetry_list:
		matrix1 = matrix[:i+1]
		matrix2 = matrix[i+1:]
		matrix1.reverse()
		is_sym = True
		for j in range(min(len(matrix1), len(matrix2))):
			if matrix1[j] != matrix2[j]:
				is_sym = False
				break
		if is_sym:
			return (i+1)*100
	return False

if __name__ == "__main__":
	matrices = []
	matrix = []
	with open("Day13.txt", "r") as f:
		for line in f:
			if line == "\n":
				matrices.append(matrix)
				matrix = []
			else:
				matrix.append(line.strip())
	sum1 = 0
	for i in matrices:
		sum1 += is_symmetric(i)
	print(sum1)
