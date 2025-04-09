#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 07:10:02 2025

@author: icaptain
"""
import pandas as pd
import numpy as np

# Players and their total runs
players = {
    "Rohit Sharma": [41, 20, 15, 28],
    "Shubman Gill": [101, 46, 2, 8],
    "Virat Kohli": [22, 100, 11, 84],
    "Shreyas Iyer": [15, 56, 79, 45],
    "KL Rahul": [41, 23, 42],
    "Hardik Pandya": [8, 45, 28],
    "Ravindra Jadeja": [16, 2],
    "Axar Patel": [8, 3, 42, 27]
}

# Calculate mean and standard deviation for each player
results = {}
for player, scores in players.items():
    mean = np.mean(scores)
    std_dev = np.std(scores, ddof=1)  # Sample standard deviation
    cv = (std_dev / mean) * 100 if mean != 0 else 0  # Coefficient of Variation (%)
    consistency = 1 / cv if cv != 0 else 0  # Consistency measure
    results[player] = {"Mean": mean, "Std Dev": std_dev, "CV": cv, "Consistency": consistency}
    
results = pd.DataFrame(results)
results
