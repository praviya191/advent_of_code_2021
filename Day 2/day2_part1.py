inputFile = open('input.txt', 'r')
h_pos = 0
v_pos = 0
for line in inputFile.read().splitlines():
	direction, value = line.split()
	if direction[0] == 'f':
		h_pos += int(value)
	elif direction[0] == 'u':
		v_pos -= int(value)
	elif direction[0] == 'd':
		v_pos += int(value)
print(h_pos * v_pos)
inputFile.close()