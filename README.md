Bus Load Analysis Tool

This Python script analyzes and visualizes the bus load from a CSV file containing Controller Area Network (CAN) data. It utilizes Pandas for data manipulation and Matplotlib for visualization.
Prerequisites

    Python 3.x
    Pandas library (pip install pandas)
    Matplotlib (pip install matplotlib)

Usage

    Ensure Python, Pandas, and Matplotlib are installed.
    Run the script.

bash

python bus_load_analyzer.py

    A file dialog window will prompt you to select a CSV file containing CAN data.
    The script will analyze the data, calculate the bus load, and display a graphical representation of the bus load over time.

Code Explanation

    Imports necessary libraries: Pandas, Matplotlib, and math.
    Prompts the user to select a CSV file using a file dialog.
    Reads the CSV file into a Pandas DataFrame.
    Converts 'Date' and 'Time' columns to a single 'Timestamp' column in datetime format.
    Groups data by tenths of a second and aggregates the Data Length Code (DLC).
    Calculates the bus load based on the aggregated DLC values.
    Plots a graph representing the bus load over time, with annotations for maximum, minimum, and average bus loads.

Note

    Ensure the CSV file contains columns named 'Date' and 'Time' representing the timestamp information.
    The script calculates bus load assuming an ISOBUS 250kb/s system.

Files

    bus_load_analyzer.py: Python script to analyze and visualize bus load.
    Sample CSV file: Not included. The script prompts the user to select a CSV file.
    No specific output file is generated. The script displays the bus load graph.

License

This project is licensed under MIT License.
