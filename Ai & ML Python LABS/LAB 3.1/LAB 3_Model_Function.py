import numpy as np
import matplotlib.pyplot as plt
x_train = np.array([1.0,2.0])
y_train = np.array([300.0,500.0])

print(f"x_train = {x_train}")
print(f"y_train = {y_train}")

# Model Function
# f(w,b)(X^(i)) = w*x^(i)+b

w =100
b= 100
print (f"w: {w}")
print (f"b: {b}")

def compute_model_output(x_train,w,b): 
 """ 
 Computes the prediction of a linear model 
 Args: 
 x (ndarray (m,)): Data, m examples 
 w,b (scalar) : model parameters 
 Returns 
 y (ndarray (m,)): target values 
 """ 
x_train = np.array([1.0,2.0])
y_train = np.array([300.0,500.0])

w =100
b= 100

 
tmp_f_wb = compute_model_output(x_train, w, b) 
# Plot our model prediction 
plt.scatter(x_train, tmp_f_wb, c='b',label='Our Prediction') 
# Plot the data points 
plt.scatter(x_train, y_train, marker='x', c='r',label='Actual Values') 
# Set the title 
plt.title("Housing Prices") 
# Set the y-axis label 
plt.ylabel('Price (in 1000s of dollars)') 
# Set the x-axis label 
plt.xlabel('Size (1000 sqft)') 
plt.legend() 
plt.show() 
