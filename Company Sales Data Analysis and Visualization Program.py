# Company Sales Data Analysis and Visualization Program
# Created by: Ibrahim Yisau
# Date: May 27, 2024
#=======================================================================================================================
"""This script analyzes company sales data and generates visualizations to help understand sales trends. 
It calculates total profit and plots it over months, and also creates a subplot for bathing soap and facewash sales."""
#======================================================================================================================    
# Company Sales Data Analysis and Visualization
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('company_sales_data.csv')

# Exercise 1: Line Plot of Total Profit
# Calculate total profit
total_profit = data['total_profit']

# Create a line plot of total profit over months
plt.plot(total_profit)
plt.title('Total Profit Over Months')
plt.xlabel('Months')
plt.ylabel('Total Profit')
plt.show()

# Exercise 2: Subplot for Bathing Soap and Facewash
# Extract bathing soap and facewash sales data
bathingsoap = data['bathingsoap']
facewash = data['facewash']

# Create a subplot with two separate plots
fig, ax = plt.subplots(2, 1)

# Plot bathing soap sales
ax[0].plot(bathingsoap)
ax[0].set_title('Bathing Soap Sales')
ax[0].set_xlabel('Months')
ax[0].set_ylabel('Sales')

# Plot facewash sales
ax[1].plot(facewash)
ax[1].set_title('Facewash Sales')
ax[1].set_xlabel('Months')
ax[1].set_ylabel('Sales')

# Show the subplot
plt.show()
