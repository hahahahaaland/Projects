import pandas as pd

df = pd.read_csv("students.csv")

result = (
    df[df["score"] > 70]
    .sort_values(by="score", ascending=False)
)

print(result[["name", "score"]])
