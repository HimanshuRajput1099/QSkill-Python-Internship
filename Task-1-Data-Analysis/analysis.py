import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

print("First 5 Rows:")
print(df.head())

# Average Math Score
avg_math = df["math_score"].mean()
print("\nAverage Math Score:", avg_math)

# Bar Chart
gender_avg = df.groupby("gender")["math_score"].mean()

plt.figure(figsize=(5,4))
gender_avg.plot(kind="bar")
plt.title("Average Math Score by Gender")
plt.ylabel("Math Score")
plt.savefig("bar_chart.png")
plt.show()

# Scatter Plot
plt.figure(figsize=(5,4))
plt.scatter(df["reading_score"], df["writing_score"])
plt.xlabel("Reading Score")
plt.ylabel("Writing Score")
plt.title("Reading vs Writing Scores")
plt.savefig("scatter_plot.png")
plt.show()

# Heatmap
corr = df[["math_score","reading_score","writing_score"]].corr()

plt.figure(figsize=(5,4))
plt.imshow(corr)
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Heatmap")
plt.savefig("heatmap.png")
plt.show()