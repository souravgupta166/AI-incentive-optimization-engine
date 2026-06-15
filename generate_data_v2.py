# --Comment: 

# --User Information:
# country
# device
# acquisition_source
# Offer Information:
# offer_category
# reward_amount
# advertiser_payout
# Business Metrics:
# user_revenue
# profit
# Experimental Metrics:
# reward_reduction_20
# reward_reduction_40
# retention_after_reduction
# New target:

# Instead of:

# reward_dependency_score

# we predict:

# retention_after_reward_cut

# This becomes a causal/business problem.

# --Architecture we'll build
# Dataset
#     ↓
# Reward Dependency Model
#     ↓
# Reward Reduction Simulator
#     ↓
# Streamlit Dashboard
#     ↓
# LinkedIn Case Study

import pandas as pd
import numpy as np

np.random.seed(42)

n_users = 100000

countries = ["US", "UK", "Germany", "India", "Brazil"]
devices = ["Android", "iOS"]
sources = ["TikTok", "Meta", "Google", "Organic"]
segments = ["genuine_gamer", "casual_user", "reward_hunter"]

data = []

for user_id in range(1, n_users + 1):
    segment = np.random.choice(segments, p=[0.4, 0.35, 0.25])

    country = np.random.choice(countries)
    device = np.random.choice(devices, p=[0.7, 0.3])
    acquisition_source = np.random.choice(sources, p=[0.35, 0.3, 0.25, 0.1])

    if segment == "genuine_gamer":
        reward_amount = np.random.uniform(2, 8)
        avg_session_time = np.random.uniform(35, 120)
        offers_completed = np.random.randint(2, 8)
        retention_30d = np.random.choice([1, 0], p=[0.82, 0.18])
        reward_dependency_score = np.random.randint(10, 40)

    elif segment == "casual_user":
        reward_amount = np.random.uniform(6, 16)
        avg_session_time = np.random.uniform(12, 60)
        offers_completed = np.random.randint(1, 5)
        retention_30d = np.random.choice([1, 0], p=[0.55, 0.45])
        reward_dependency_score = np.random.randint(40, 70)

    else:
        reward_amount = np.random.uniform(12, 30)
        avg_session_time = np.random.uniform(2, 25)
        offers_completed = np.random.randint(1, 4)
        retention_30d = np.random.choice([1, 0], p=[0.28, 0.72])
        reward_dependency_score = np.random.randint(70, 100)

    advertiser_payout = reward_amount * np.random.uniform(1.4, 3.2)
    user_revenue = advertiser_payout * retention_30d
    profit = user_revenue - reward_amount

    reward_cut_20 = reward_amount * 0.8
    reward_cut_40 = reward_amount * 0.6

    if reward_dependency_score < 40:
        retention_after_20_cut = np.random.choice([1, 0], p=[0.78, 0.22])
        retention_after_40_cut = np.random.choice([1, 0], p=[0.62, 0.38])
    elif reward_dependency_score < 70:
        retention_after_20_cut = np.random.choice([1, 0], p=[0.55, 0.45])
        retention_after_40_cut = np.random.choice([1, 0], p=[0.35, 0.65])
    else:
        retention_after_20_cut = np.random.choice([1, 0], p=[0.25, 0.75])
        retention_after_40_cut = np.random.choice([1, 0], p=[0.10, 0.90])

    data.append([
        user_id,
        country,
        device,
        acquisition_source,
        segment,
        round(reward_amount, 2),
        avg_session_time,
        offers_completed,
        retention_30d,
        reward_dependency_score,
        round(advertiser_payout, 2),
        round(user_revenue, 2),
        round(profit, 2),
        round(reward_cut_20, 2),
        round(reward_cut_40, 2),
        retention_after_20_cut,
        retention_after_40_cut
    ])

df = pd.DataFrame(data, columns=[
    "user_id",
    "country",
    "device",
    "acquisition_source",
    "segment",
    "reward_amount",
    "avg_session_time",
    "offers_completed",
    "retention_30d",
    "reward_dependency_score",
    "advertiser_payout",
    "user_revenue",
    "profit",
    "reward_cut_20",
    "reward_cut_40",
    "retention_after_20_cut",
    "retention_after_40_cut"
])

df.to_csv("data/reward_dependency_v2.csv", index=False)

print(df.head())
print("\nDataset created: data/reward_dependency_v2.csv")
print("Shape:", df.shape)