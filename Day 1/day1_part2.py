inputFile = open('input.txt', 'r')
# Creating a list from input data
measurements = list(map(int, inputFile.read().splitlines()))
count = 0
size = len(measurements)
prev_window = sum(measurements[:3])
for i in range(3, size):
    curr_sum = prev_window + measurements[i] - measurements[i-3]
    if prev_window < curr_sum:
        count += 1 
    prev_window = curr_sum
print(count)
inputFile.close()