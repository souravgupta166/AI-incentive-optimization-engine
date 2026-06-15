# Reward Waste Detector

# Question:

# Which users are receiving more rewards than necessary?

# Example:

# User	Current Reward	Predicted Safe Reward	Savings
# 123	€20	€14	€6
# 456	€15	€12	€3
# 789	€25	€15	€10

import pandas as pd

df = pd.read_csv("data/reward_dependency_v2.csv")

print("\nTotal Users")
print(len(df))

print("\nCurrent Reward Spend")
print(df["reward_amount"].sum())

print("\nTotal Profit")
print(df["profit"].sum())

print("\nAverage Dependency Score")
print(df["reward_dependency_score"].mean())

high_dependency = df[df["reward_dependency_score"] > 70]

print("\nHigh Dependency Users")
print(len(high_dependency))

print("\nPotential Reward Waste")
print(high_dependency["reward_amount"].sum())

# I want to analyze
# "Can you prove I can save €512K without hurting retention?"