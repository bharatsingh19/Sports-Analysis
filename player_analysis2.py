#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 07:24:55 2025

@author: icaptain
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Creating the dataset manually
data = {
    "Batsman": [
        "Rohit Sharma", "Rohit Sharma", "Rohit Sharma", "Rohit Sharma",
        "Shubman Gill", "Shubman Gill", "Shubman Gill", "Shubman Gill",
        "Virat Kohli", "Virat Kohli", "Virat Kohli", "Virat Kohli",
        "Shreyas Iyer", "Shreyas Iyer", "Shreyas Iyer", "Shreyas Iyer",
        "Axar Patel", "Axar Patel", "Axar Patel", "Axar Patel",
        "KL Rahul", "KL Rahul", "KL Rahul",
        "Hardik Pandya", "Hardik Pandya", "Hardik Pandya",
        "Ravindra Jadeja", "Ravindra Jadeja",
        "Mohammed Shami", "Kuldeep Yadav"
    ],
    "Runs": [41, 20, 15, 28, 101, 46, 2, 8, 22, 100, 11, 84, 15, 56, 79, 45, 
             8, 3, 42, 27, 41, 23, 42, 8, 45, 28, 16, 2, 5, 1]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Assign a unique color to each batsman
batsmen = df["Batsman"].unique()
colors = plt.cm.tab10(np.linspace(0, 1, len(batsmen)))  # Using tab10 colormap

# Create scatter plot
plt.figure(figsize=(14, 8))
for batsman, color in zip(batsmen, colors):
    subset = df[df["Batsman"] == batsman]
    plt.scatter(subset["Batsman"], subset["Runs"], color=color, label=batsman, alpha=0.7, edgecolors='black')

# Add labels and title
plt.xlabel("Batsman", fontsize=12)
plt.ylabel("Runs", fontsize=12)
plt.title("Scatter Plot of Runs by Batsman", fontsize=14)
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.legend(title="Batsmen", bbox_to_anchor=(1.05, 1), loc='upper left')  # Legend outside the plot
plt.grid(True, linestyle='--', alpha=0.5)

# Show plot
plt.show()