import pandas as pd
from matplotlib import pyplot as plt
import math
from tkinter import filedialog
import tkinter as tk

# Create a Tkinter root window (it won't be shown)
root = tk.Tk()
root.withdraw()  # Hide the root window

# Use file dialog to select the CSV file
file_path = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV files", "*.csv")])

# Read the CSV file
df = pd.read_csv(file_path)

# Convert Date and Time columns to datetime format
df['Timestamp'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], errors='coerce')  # Change 'time' to 'Time'

# Drop rows with NaN in 'Timestamp'
df = df.dropna(subset=['Timestamp'])

# Group data by tenths of a second and sum DLC
grouped_data = df.groupby(df['Timestamp'].dt.floor('100ms')).agg({'DLC': 'sum'}).reset_index()

# Calculate the bus load
busload = [(8 * n + 64 + math.floor((54 + (8 * n - 1)) / 4)) / 250000 for n in grouped_data['DLC']]

# Find the index and value of the maximum bus load
max_index = busload.index(max(busload))
max_value = max(busload)

# Find the index and value of the minimum bus load
min_index = busload.index(min(busload))
min_value = min(busload)

# Plot the graph
fig, ax = plt.subplots(figsize=(10, 5))  # Adjust the figure size here
ax.plot(range(len(grouped_data)), busload, label='Bus Load')
ax.axhline(y=max_value, color='r', linestyle='--', label='Max Bus Load')
ax.axhline(y=min_value, color='g', linestyle='--', label='Min Bus Load')
ax.axhline(y=sum(busload) / len(busload), color='b', linestyle='--', label='Average Bus Load')

# Annotate the highest bus load percentage
max_dlc_index = grouped_data['DLC'].idxmax()
max_percentage = (grouped_data['DLC'].loc[max_dlc_index] / (250000 / 8)) * 100
ax.text(max_index, max_value, f'Highest Bus Load: {max_percentage:.2f}%',
        horizontalalignment='right', verticalalignment='bottom')

# Annotate the average bus load percentage
avg_percentage = (grouped_data['DLC'].mean() / (250000 / 8)) * 100
ax.text(len(grouped_data) // 2, sum(busload) / len(busload), f'Average Bus Load: {avg_percentage:.2f}%',
        horizontalalignment='right', verticalalignment='bottom')

# Annotate the minimum bus load percentage
min_dlc_index = grouped_data['DLC'].idxmin()
min_percentage = (grouped_data['DLC'].loc[min_dlc_index] / (250000 / 8)) * 100
ax.text(min_index, min_value, f'Minimum Bus Load: {min_percentage:.2f}%',
        horizontalalignment='left', verticalalignment='top')

ax.set(xlabel='Time (in tenths of seconds)', ylabel='Bus Load (ISOBUS 250kb/s)',
       title='Bus Load over Time')
ax.grid()

# Adjust the frame size without stretching the graph
plt.subplots_adjust(right=0.75)

# Move the legend outside the graph
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.show()
