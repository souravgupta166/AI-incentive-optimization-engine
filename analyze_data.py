import pandas as pd

df = pd.read_csv("data/users.csv")

print("\nShape:")
print(df.shape)

print("\nSegment Distribution:")
print(df["segment"].value_counts())

print("\nAverage Dependency Score:")
print(df.groupby("segment")["reward_dependency_score"].mean())

--Comment:
--Input:

--Current Reward = €20

--System predicts:

--Can reduce to €16
--Expected retention drop = 2%
--Profit increase = 14%