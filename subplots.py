import matplotlib.pyplot as plt

# Create sample data
x = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 4, 9, 16, 25]
y2 = [0, 2, 4, 6, 8, 10]
y3 = [25, 16, 9, 4, 1, 0]
y4 = [10, 8, 6, 4, 2, 0]

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))

# First subplot (top-left)
axs[0, 0].plot(x, y1)
axs[0, 0].set_title("Quadratic")

# Second subplot (top-right)
axs[0, 1].plot(x, y2)
axs[0, 1].set_title("Linear")

# Third subplot (bottom-left)
axs[1, 0].plot(x, y3)
axs[1, 0].set_title("Inverted Quadratic")

# Fourth subplot (bottom-right)
axs[1, 1].plot(x, y4)
axs[1, 1].set_title("Inverted Linear")

# Add a title for the entire figure
fig.suptitle("Example of 2x2 Subplots")

# Adjust the layout to avoid overlapping elements
plt.tight_layout()

# Display the subplots
plt.show()
