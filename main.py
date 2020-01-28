def read_data(filename):
	with open(filename) as file:
		unused = file.readline()
		plates = []
		for line in file:
			buffer = []
			for letter in line:
				buffer.append(letter)
			plates.append(buffer[:-1])
	return plates


def solve(plates):
	rows = len(plates)
	columns = len(plates[0])
	ways = [[0 for i in range(columns)] for j in range(rows)]
	for j in range(columns):
		for i in range(rows):
			count_ways(plates, i, j, ways)
			print()
	return ways[0][columns - 1] + ways[rows - 1][columns - 1]


def count_ways(plates, i, j, ways):
	if j == 0:
		ways[i][j] = 1
	else:
		letter = plates[i][j]
		ways[i][j] = ways[i][j - 1]
		for column in range(j):
			for row in range(len(ways)):
				if plates[row][column] == letter:
					if not (row == i and column == j - 1):
						ways[i][j] += ways[row][column]
	print_arr(ways)


def print_arr(arr):
	for line in arr:
		print(line)

if __name__ == '__main__':
	print(solve(read_data("ijones.in")))
