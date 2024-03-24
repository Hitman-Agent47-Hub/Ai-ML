import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the dataset
x = np.array([[1, 86226, 1, 1, 1, 2017, 1956, 5],
              [2, 13248, 2, 2, 1, 2021, 1330, 5],
              [3, 60343, 2, 2, 1, 2016, 2494, 5],
              [4, 2696, 2, 2, 2, 2018, 1199, 5],
              [5, 69414, 2, 1, 1, 2016, 1199, 5],
              [6, 49719, 2, 2, 1, 2017, 1197, 5],
              [6, 43688, 2, 2, 2, 2017, 1197, 5],
              [7, 14470, 1, 1, 1, 2021, 1498, 5],
              [8, 21429, 2, 2, 1, 2015, 1497, 5],
              [2, 31750, 2, 2, 2, 2017, 1498, 5],
              [9, 38203, 2, 1, 1, 2017, 1197, 5],
              [8, 110284, 2, 2, 1, 2014, 1497, 5],
              [10, 10381, 2, 1, 2, 2020, 1197, 5],
              [1, 32378, 2, 2, 1, 2019, 1368, 5],
              [8, 38906, 2, 1, 1, 2020, 1498, 5],
              [11, 59313, 2, 2, 2, 2016, 1197, 5],
              [12, 85627, 1, 1, 1, 2017, 1396, 5]])

y = np.array([10.03, 12.83, 16.40, 7.77, 5.15, 7.66, 7.58, 11.60, 6.99, 7.53, 6.43, 5.43, 8.62, 16.78, 10.03, 5.63, 6.67])

# Initialize parameters
theta = np.zeros((x.shape[1]))
alpha = 0.01
num_iters = 1000

# Compute the cost function
def compute_cost(x, y, theta):
    m = len(y)
    h = np.dot(x, theta)
    J = (1 / (2 * m)) * np.sum(np.square(h - y))
    return J

# Perform gradient descent to obtain the optimal parameters
def gradient_descent(x, y, theta, alpha, num_iters):
    m = len(y)
    J_history = np.zeros(num_iters)
    
    for iter in range(num_iters):
        h = np.dot(x, theta)
        gradient = (1 / m) * np.dot(x.T, (h - y))
        theta = theta - (alpha * gradient)
        J_history[iter] = compute_cost(x, y, theta)
    
    return theta, J_history

# Feature Scaling (optional)
# Feature Scaling (optional)
std_dev = x[:, 1:].std(axis=0)
std_dev[std_dev == 0] = 1  # Avoid division by zero, replace zero values with 1
x[:, 1:] = (x[:, 1:] - x[:, 1:].mean(axis=0)) / std_dev


# Obtain optimal parameters
theta, J_history = gradient_descent(x, y, theta, alpha, num_iters)

# Compute the cost using learned parameters
cost = compute_cost(x, y, theta)

# Plotting the cost function over iterations
plt.plot(range(num_iters), J_history, 'b')
plt.xlabel('Iterations')
plt.ylabel("Cost J")
plt.title('Cost Function over Iterations')

# Check convergence
convergence_threshold = 1e-5  # Set convergence threshold
converged = False

for i in range(1, len(J_history)):
    if abs(J_history[i] - J_history[i-1]) < convergence_threshold:
        converged = True
        print("Algorithm converged after", i, "iterations.")
        break

if not converged:
    print("Algorithm did not converge within the specified threshold.")

# Define a grid of theta values
theta0_vals = np.linspace(-10, 10, 100)
theta1_vals = np.linspace(-1, 4, 100)
theta0_mesh, theta1_mesh = np.meshgrid(theta0_vals, theta1_vals)

# Compute corresponding cost values over the grid
cost_mesh = np.zeros((len(theta0_vals), len(theta1_vals)))
for i in range(len(theta0_vals)):
    for j in range(len(theta1_vals)):
        theta_tmp = np.array([theta0_vals[i], 0, theta1_vals[j], 0, 0, 0, 0, 0])  # Ensure theta_tmp matches the dimensions of X
        cost_mesh[i, j] = compute_cost(x, y, theta_tmp)

# Plot the cost function surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(theta0_mesh, theta1_mesh, cost_mesh, cmap='viridis')
ax.set_xlabel('Theta0')
ax.set_ylabel('Theta1')
ax.set_zlabel('Cost')
plt.title('Cost Function Surface')
plt.show()

# Print the learned parameters
print("Learned parameters (theta):", theta)
print("Cost function computed using learned parameters:", cost)
