import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Load the Excel file 
df = pd.read_excel(r'E:\5th Semester Data\AI & ML\repo\Ai & ML Python LABS\LAB 5\Housing.xlsx')
print(df)

# Assuming you want to extract columns named 'Column1' and 'Column2'
extracted_columns = df[['price','area','bedrooms','bathrooms','stories']]

# Show the extracted columns 
print(extracted_columns)

# If you want to save the extracted columns to a new Excel file 
# extracted_columns.to_excel('Extracted_columns.xlsx', index  = False)

# 1.2 View the Dataset
ar1 = np.array(extracted_columns)
x1 = ar1[:,1]
y1 = ar1[:,0]


# plt.scatter(y1,x1)
# plt.title("Housing Prices")
# plt.xlabel ("Size(Sqft)")
# plt.ylabel("Price(1000's)")
# plt.show()

x2 = ar1[:,2]
# y2 = ar1[:,0]

# plt.scatter(x2,y1)
# plt.title("Housing Prices")
# plt.xlabel("bedrooms")
# plt.ylabel("Price(1000's)")
# plt.show()

x3 = ar1[:,3]
# y3 = ar1[:,0]

x4 = ar1[:,4]
# y4 = ar1[:,0]

plt.subplot(1,2,1)
plt.scatter(x1,y1)

plt.subplot(1,2,2)
plt.scatter(x2,y1)

plt.subplot(2,2,3)
plt.scatter(x3,y1)

plt.subplot(2,2,4)
plt.scatter(x4,y1)

plt.show()