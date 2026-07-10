import pandas as pd

df = pd.read_csv("students.csv")

high_scores = df[df["score"] > 70]

high_scores = high_scores.sort_values(
    by="score",
    ascending=False
)

print(high_scores[["name", "score"]])