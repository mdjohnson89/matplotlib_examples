import matplotlib.pyplot as plt

with open('women_in_congress.csv') as file:
    data = file.readlines()

xdata = []
ydata = []

for line in data:
    to_read = line.split(',')
    xdata.append(int(to_read[0]))
    ydata.append(float(to_read[1]))

plt.xlabel('Year')
plt.ylabel('Percentage of Congress that is Female')
plt.title('Percentage of Congress that is Female 1997-2019')
plt.ylim([0,1])
plt.xticks(xdata, rotation='vertical')

plt.plot(xdata, ydata)
plt.savefig('my_cool_plot.png', dpi=300, format='png')
plt.show()