import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
df = pd.DataFrame({"x": range(10), "y": [v**2 for v in range(10)]})

# Matplotlib
plt.figure(figsize=(8, 6))
plt.plot(df["x"], df["y"], marker="o", color="teal", linewidth=2, label="y = x²")
plt.title("Matplotlib Line Plot", fontsize=14)
plt.xlabel("X", fontsize=12)
plt.ylabel("Y", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("matplotlib_improved.png")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="x", y="y", color="crimson", s=100)
plt.title("Seaborn Scatter Plot", fontsize=14)
plt.xlabel("X", fontsize=12)
plt.ylabel("Y", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

fig = px.line(
    df, x="x", y="y", title="Plotly Interactive Line Chart",
    markers=True,
    labels={"x": "X", "y": "Y = x**2"}
)
fig.update_traces(line=dict(color="royalblue", width=3))
fig.update_layout(title_font_size=18)
fig.show()
