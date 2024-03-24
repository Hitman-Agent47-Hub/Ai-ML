import numpy as np
import matplotlib.pyplot as plt

x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])

print(f"x_train = {x_train}")
print(f"y_train = {y_train}")

# Model Function
# f(w,b)(X^(i)) = w*x^(i)+b

w = 100
b = 100
print(f"w: {w}")
print(f"b: {b}")

def compute_model_output(x, w, b):
    """ 
    Computes the prediction of a linear model 
    Args: 
    x (ndarray (m,)): Data, m examples 
    w,b (scalar) : model parameters 
    Returns 
    y (ndarray (m,)): target values 
    """
    return w * x + b

# print(compute_model_output(x_train,w,b))

# Compute model output
tmp_f_wb = compute_model_output(x_train, w, b)

# Plot our model prediction 
plt.scatter(x_train, tmp_f_wb, c='b', label='Our Prediction') 
# Plot the data points 
plt.scatter(x_train, y_train, marker='x', c='r', label='Actual Values') 
# Set the title 
plt.title("Housing Prices") 
# Set the y-axis label 
plt.ylabel('Price (in 1000s of dollars)') 
# Set the x-axis label 
plt.xlabel('Size (1000 sqft)') 
plt.legend() 
plt.show() 

# Challenge Question 
# Try experimenting with different values of w and b. What should the values be for a line that fits 
# our data?

x_i = 1.2
w_1 = 200
b_1 = 100
print("x = ",x_i)
print("w_1 = ",w_1)
print("b_1 = ",b_1)
cost_1200sqft  =compute_model_output(x_i,w_1, b_1)
print(f"${cost_1200sqft:.0f} thousand dollars") 

