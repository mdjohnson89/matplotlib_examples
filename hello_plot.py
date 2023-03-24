''' matplotlib used to create figure for this data visualization '''
import matplotlib.pyplot as plt

x = range(11)
y = [y**2 for y in range(11)]

plt.xlabel('Numbers')
plt.ylabel('Squares')
plt.title('My fun plot')

labels = ['zero', 'one', 'two', 'three', 'four', '5', 'six', 'seven', '8', 'nine', 'ten']
plt.xticks(x, labels, rotation='vertical')
plt.yticks(range(0, 110, 10))

plt.plot(x, y)

plt.savefig('my_figure.png', dpi = 300, format='png')
plt.show()
