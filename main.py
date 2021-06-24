import math
import csv
with open("data.csv",newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    
    mean = total/n
    return mean

squard_data = []
for n in data:
    a = int(n)-mean(data)
    a = a*a
    squard_data.append(a)

sum = 0
for i in squard_data:
    sum = sum+i

result = sum/ (len(data)-1)

std_deviation = math.sqrt(result)
print(std_deviation)