''' congress_ex.py creates a plot of the percentage of women that make up
    US Congress from 1997-2019.

    Used to demonstrate the functioning of matplotlib
'''
import matplotlib.pyplot as plt

# Read and process the data
with open('women_in_congress.csv') as file:
    # Reads in csv as a list of strings.
    data = file.readlines()

x_data = []
y_data = []

for line in data:
    to_read = line.split(',')
    x_data.append(int(to_read[0].strip()))
    y_data.append(float(to_read[1].strip())*100)

# Look and labels
plt.title('Percentage of Women in US Congress 1997 - 2019')
plt.xlabel = 'Year (starting 1997)'
plt.ylabel = 'Percentage of Congress that is Women'
plt.grid()
plt.xticks(x_data, rotation='vertical')
plt.ylim((0, 100))

# Create the plot
plt.plot(x_data, y_data)
plt.savefig('congress_fig.png', format='png')
plt.show()
