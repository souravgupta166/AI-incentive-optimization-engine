import pandas as pd
import numpy as np

np.random.seed(42)

n_users = 100000

segments = np.random.choice(
    ["genuine_gamer", "casual_user", "reward_hunter"],
    size=n_users,
    p=[0.4, 0.35, 0.25]
)

data = []

for i, segment in enumerate(segments):

    if segment == "genuine_gamer":
        reward = np.random.uniform(2, 10)
        session_time = np.random.uniform(30, 120)
        retention = np.random.choice([1, 0], p=[0.85, 0.15])
        dependency = np.random.randint(10, 40)

    elif segment == "casual_user":
        reward = np.random.uniform(5, 15)
        session_time = np.random.uniform(10, 60)
        retention = np.random.choice([1, 0], p=[0.55, 0.45])
        dependency = np.random.randint(40, 70)

    else:
        reward = np.random.uniform(10, 30)
        session_time = np.random.uniform(2, 20)
        retention = np.random.choice([1, 0], p=[0.25, 0.75])
        dependency = np.random.randint(70, 100)

    data.append([
        i + 1,
        segment,
        round(reward, 2),
        round(session_time, 2),
        retention,
        dependency
    ])

df = pd.DataFrame(
    data,
    columns=[
        "user_id",
        "segment",
        "reward_amount",
        "avg_session_time",
        "retention_30d",
        "reward_dependency_score"
    ]
)

df.to_csv("data/users.csv", index=False)

print(df.head())
print("Dataset created successfully")