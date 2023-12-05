from tqdm import tqdm

def find_next(num, table):
	# look at the second position of every sublist in the table
	# and see if the num is bigger than the second position
	# if it is see if the num is in the range from the second number and the second number + the third number
	for i in range(len(table)):
		if table[i][1] < num <= table[i][1] + table[i][2]:
			return num + table[i][0] - table[i][1]
	return num


if __name__ == "__main__":
	input_list = []
	with open('day5.txt') as f:
		for line in f:
			input_list.append(line.rstrip('\n'))
	seeds = input_list[0].split(':')[1]
	seeds_int = [int(i) for i in seeds.split()]
	# seed to soil 2D array
	seed_to_soil = []
	for i in range(3, 16):
		seed_to_soil.append([int(j) for j in input_list[i].split()])
	# soil_to_fertilizer 2D array
	soil_to_fertilizer = []
	for i in range(18, 39):
		soil_to_fertilizer.append([int(j) for j in input_list[i].split()])

	# fertilizer_to_water 2D array
	fertilizer_to_water = []
	for i in range(41, 89):
		fertilizer_to_water.append([int(j) for j in input_list[i].split()])

	# water_to_light 2D array
	water_to_light = []
	for i in range(91, 130):
		water_to_light.append([int(j) for j in input_list[i].split()])

	# light_to_temperature 2D array
	light_to_temperature = []
	for i in range(132, 148):
		light_to_temperature.append([int(j) for j in input_list[i].split()])

	# temperature_to_humidity 2D array
	temperature_to_humidity = []
	for i in range(150, 157):
		temperature_to_humidity.append([int(j) for j in input_list[i].split()])

	# humidity_to_location 2D array
	humidity_to_location = []
	for i in range(159, 190):
		humidity_to_location.append([int(j) for j in input_list[i].split()])

	# Teil 1
	seed_to_location = []
	print(len(seeds_int))
	for i in range(len(seeds_int)):
		soil = find_next(seeds_int[i], seed_to_soil)
		fertilizer = find_next(soil, soil_to_fertilizer)
		water = find_next(fertilizer, fertilizer_to_water)
		light = find_next(water, water_to_light)
		temperature = find_next(light, light_to_temperature)
		humidity = find_next(temperature, temperature_to_humidity)
		location = find_next(humidity, humidity_to_location)
		seed_to_location.append(location)
	print("the lowest Location for the seeds is: " + str(sorted(seed_to_location)[0]))

	#Teil 2
	seed_to_location = 999999999999999999999999999999999999999999
	for i in tqdm(range(0, 20, 2)):
		for j in tqdm(range(seeds_int[i], seeds_int[i] + seeds_int[i+1])):
			soil = find_next(j, seed_to_soil)
			fertilizer = find_next(soil, soil_to_fertilizer)
			water = find_next(fertilizer, fertilizer_to_water)
			light = find_next(water, water_to_light)
			temperature = find_next(light, light_to_temperature)
			humidity = find_next(temperature, temperature_to_humidity)
			location = find_next(humidity, humidity_to_location)
			if location < seed_to_location:
				seed_to_location = location
	print("the lowest Location for the range of seeds is: " + str(seed_to_location))
