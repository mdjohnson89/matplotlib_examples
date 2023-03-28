import matplotlib.pyplot as plt

with open('Female_Political_Representation.csv') as filey:
    header = filey.readline()
    data = filey.readlines()

country1 = input('What is the first country to compare?')
country2 = input('What is the next country to compare?')

x_data = []
y1_data = []
y2_data = []

for line in data:
    to_read = line.split(',')
    if to_read[0] == country1:
        x_data.append(int(to_read[2]))
        y1_data.append(float(to_read[3])*100)
    elif to_read[0] == country2:
        y2_data.append(float(to_read[3])*100)

print(x_data, y1_data, y2_data)
