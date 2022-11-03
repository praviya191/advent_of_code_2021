inputFile = open('input.txt', 'r')
h_pos = 0
v_pos = 0
aim = 0
for line in inputFile.read().splitlines():
    direction, value = line.split()
    if direction[0] == 'f':
        h_pos += int(value)
        v_pos += aim * int(value)
    elif direction[0] == 'u':
        aim -= int(value)
    elif direction[0] == 'd':
        aim += int(value)
print(h_pos * v_pos)
inputFile.close()