import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('your_dataset.csv')
# Display the first few rows of the dataset
print(data.head())
# Basic data analysis
print("Summary statistics:")
print(data.describe())
print("Missing values:")
print(data.isnull().sum())
# Data visualization
# Example: Plotting a histogram of a numerical column
plt.hist(data['numerical_column'], bins=20)
