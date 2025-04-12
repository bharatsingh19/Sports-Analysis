#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 12:47:22 2025

@author: icaptain
"""

# Creating the dataset manually from the provided image/text
import pandas as pd

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
    "Runs": [41, 20, 15, 28, 101, 46, 2, 8, 22, 100, 11, 84, 15, 56, 79, 45, 8, 3, 42, 27, 41, 23, 42, 8, 45, 28, 16, 2, 5, 1],
    "Balls": [36, 15, 17, 29, 129, 52, 7, 11, 38, 111, 14, 98, 17, 67, 98, 62, 12, 4, 61, 30, 47, 29, 34, 6, 45, 24, 20, 1, 8, 1],
    "Strike Rate": [113.89, 133.33, 88.24, 96.55, 78.29, 88.46, 28.57, 72.73, 57.89, 90.09, 78.57, 85.71, 88.24, 83.58, 80.61, 72.58, 66.67, 75, 68.85, 90, 87.23, 79.31, 123.53, 133.33, 100, 116.67, 80, 200, 62.5, 100]
}

# Convert to DataFrame
df = pd.DataFrame(data)


# Compute Batting Average (Total Runs / Number of Innings)
batting_avg = df.groupby("Batsman")["Runs"].sum() / df.groupby("Batsman")["Batsman"].count()

# Compute Average Strike Rate per player
avg_strike_rate = df.groupby("Batsman")["Strike Rate"].mean()

# Combine into a new DataFrame
batting_stats = pd.DataFrame({"Batting Average": batting_avg, "Average Strike Rate": avg_strike_rate})

# Display the computed statistics
batting_stats.sort_values(by="Batting Average", ascending=False)

import matplotlib.pyplot as plt
import numpy as np

runs=data["Runs"]
Batsman=data["Batsman"]
# Create scatter plot
plt.figure(figsize=(14, 12))
plt.scatter(Batsman, runs, color='blue', alpha=0.6, edgecolors='black', label='Data Points')

# Add labels and title
plt.xlabel("Batsmans")
plt.ylabel("Runs")
plt.title("Runs scored by batsmans")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

# Show plot
plt.show()
