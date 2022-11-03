inputFile = open('input.txt', 'r')
# Creating a list from input data
measurements = list(map(int, inputFile.read().splitlines()))
count = 0
for i in range(len(measurements)-1):
    if measurements[i] < measurements[i+1]:
        count += 1 
print(count)
inputFile.close()