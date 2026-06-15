# User
#     ↓
# Dependency Analysis
#     ↓
# Reward Reduction Simulation
#     ↓
# Retention Impact Estimation
#     ↓
# Recommended Reward
#     ↓
# Expected Savings

# This becomes:

# "AI-Powered Incentive Budget Optimizer"

# Now that's something a company might actually use.

# Problem Statement

# Current state:

# All users receive rewards based on offer completion.

# Unknown:

# Who can safely receive less reward?

# Business risk:

# Reward overspending.

# Business goal:

# Reduce reward spend without reducing retention.

# question:
# "Who has high dependency?"

# causal inference
# experimentation
# measurement
# uplift modelling

# Uplift Model for Reward Reduction

# Groups:

# Group	Reward Cut
# Control	No cut
# Treatment A	-20%
# Treatment B	-40%

# Measure:

# Retention
# Profit
# Revenue

import pandas as pd

df = pd.read_csv("data/reward_dependency_v2.csv")

def recommend_reward(row):
    if row["reward_dependency_score"] < 40:
        return row["reward_cut_40"], "REDUCE_40"
    elif row["reward_dependency_score"] < 70:
        return row["reward_cut_20"], "REDUCE_20"
    else:
        return row["reward_amount"], "KEEP"

df[["suggested_reward", "recommendation"]] = df.apply(
    lambda row: pd.Series(recommend_reward(row)),
    axis=1
)

df["estimated_savings"] = df["reward_amount"] - df["suggested_reward"]

total_current_spend = df["reward_amount"].sum()
total_suggested_spend = df["suggested_reward"].sum()
total_savings = df["estimated_savings"].sum()

print("\nReward Optimizer Summary")
print("------------------------")
print(f"Current Reward Spend: €{total_current_spend:,.2f}")
print(f"Suggested Reward Spend: €{total_suggested_spend:,.2f}")
print(f"Estimated Savings: €{total_savings:,.2f}")
print(f"Savings Percentage: {(total_savings / total_current_spend) * 100:.2f}%")

print("\nRecommendation Breakdown:")
print(df["recommendation"].value_counts())

df.to_csv("data/reward_optimizer_output.csv", index=False)

print("\nOutput saved to data/reward_optimizer_output.csv")