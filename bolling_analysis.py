#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 14:58:30 2025

@author: icaptain
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data (Assuming CSV format for ease of use)
file_path = "/Users/icaptain/Desktop/Bowling.csv"  # Change this to your file path
df = pd.read_csv(file_path)

# Convert Overs to Balls for accurate calculations
df['Balls'] = df['O'] * 6

# Group by Bowler to sum stats
bowler_stats = df.groupby('Bowling').agg({
    'Balls': 'sum',
    'R': 'sum',
    'W': 'sum',
    'O': 'sum'
}).reset_index()

# Calculate Metrics
bowler_stats['Bowling Average'] = bowler_stats['R'] / bowler_stats['W']
bowler_stats['Strike Rate'] = bowler_stats['Balls'] / bowler_stats['W']
bowler_stats['Economy Rate'] = bowler_stats['R'] / bowler_stats['O']

# Replace Inf values (for cases where Wickets = 0)
bowler_stats.replace([float('inf'), -float('inf')], 0, inplace=True)

# Print Data
print(bowler_stats)

# Visualization
plt.figure(figsize=(12, 5))
sns.barplot(x='Bowling', y='Bowling Average', data=bowler_stats, palette='viridis')
plt.xticks(rotation=45)
plt.title('Bowling Average of Players')
plt.ylabel('Average Runs per Wicket')
plt.show()

plt.figure(figsize=(12, 5))
sns.barplot(x='Bowling', y='Strike Rate', data=bowler_stats, palette='coolwarm')
plt.xticks(rotation=45)
plt.title('Bowler Strike Rates')
plt.ylabel('Balls per Wicket')
plt.show()

plt.figure(figsize=(12, 5))
sns.barplot(x='Bowling', y='Economy Rate', data=bowler_stats, palette='magma')
plt.xticks(rotation=45)
plt.title('Bowler Economy Rates')
plt.ylabel('Runs per Over')
plt.show()
