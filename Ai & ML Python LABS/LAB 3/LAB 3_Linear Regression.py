import numpy as np
# x_train is the input variable (size in 1000 square feet)
# y_train is the target (price in 1000s of dollars)

x_train = np.array([1.0,2.0])
y_train = np.array([300.0,500.0])

print(f"x_train = {x_train}")
print(f"y_train = {y_train}")

# m is the number of training examples
# .shape parameter
print(f"x_train.shape: {x_train.shape}")
m = x_train.shape[0]
print(f"Number of training examples is: {m}")

# m is the number of training examples
# len() function
m = len(x_train)
print(f"Number of training examples is: {m}")

# Training example `x_i, y_i` 

i = 0
x_i = x_train[i]
y_i = y_train[i]
print(f"(x^({i}), y^({i})) = ({x_i}, {y_i})")

# Change this to 1 to see (x^1, y^1)
j=1
x_j = x_train[j]
y_j = y_train[j]
print(f"x^({j}),y^({j}) = ({x_j},{y_j})")

# ----------------------------------------------------------------------------

# Plotting Data
import matplotlib.pyplot as plt

# Plot the data points
plt.scatter(x_train, y_train, marker='x', c='r')
# Set the title
plt.title("Housing Prices")
# Set the y-axis label
plt.ylabel('Price (in 1000s of dollars)')
# Set the x-axis label
plt.xlabel('Size (1000 sqft)')
plt.show()

