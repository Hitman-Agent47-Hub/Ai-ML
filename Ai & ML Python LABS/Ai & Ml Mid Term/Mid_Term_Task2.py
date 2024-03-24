import pandas as pd
import numpy as np
# either use raw string or \\ backlashes with the file path
data = pd.read_excel(r"C:\Users\Lenovo\Desktop\New folder\Dataset1.xlsx")
print(data)

# # 1) Extract the input features automatically
# # Assuming all columns except the target variable are input features
# x = data.drop(columns=[' Unnamed: 9'])

# # 2) Determine the number of training examples
# num_examples = len(data)

# # 3) Extract the target variable
# y = data[' Unnamed: 9']

# # 4) Using your implementation from Part 1, compute the cost and model parameters
# def compute_cost(x, y, theta):
#     m = len(y)  # Number of training examples
#     J = 0
    
#     # Compute hypothesis/predictions
#     h = np.dot(x, theta)
    
#     # Compute cost
#     J = (1/(2*m)) * np.sum(np.square(h - y))
    
#     return J

# def gradient_descent(x, y, theta, alpha, num_iters):
#     m = len(y)  # Number of training examples
#     J_history = np.zeros(num_iters)
    
#     for iter in range(num_iters):
#         # Compute hypothesis/predictions
#         h = np.dot(x, theta)
        
#         # Compute gradient
#         grad = (1/m) * np.dot(X.T, (h - y))
        
#         # Update parameters
#         theta = theta - alpha * grad
        
#         # Save the cost J in every iteration
#         J_history[iter] = compute_cost(X, y, theta)
    
#     return theta, J_history

# # Initialize model parameters
# theta = np.zeros(x.shape[1] + 1)  # Add one for the intercept term

# # Add a column of ones to X for the intercept term
# X = np.c_[np.ones((len(x), 1)), x]

# # Set hyperparameters
# alpha = 0.01  # Learning rate
# num_iters = 1000  # Number of iterations

# # Perform gradient descent to obtain the optimal parameters
# theta, J_history = gradient_descent(X, y, theta, alpha, num_iters)

# # Print the learned parameters
# print("Learned parameters (theta):", theta)

# # Compute the cost function for the learned parameters
# cost = compute_cost(X, y, theta)
# print("Cost function computed using learned parameters:", cost)