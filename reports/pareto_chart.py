import matplotlib.pyplot as plt

# Defect category and frequency data
categories = [
    "Input Validation",
    "Performance",
    "Data Refresh",
    "Database",
    "Search",
    "Navigation",
    "Calculation"
]

frequency = [2, 2, 2, 1, 1, 1, 1]

# Calculate cumulative percentage
total = sum(frequency)

cumulative = []
running_total = 0

for value in frequency:
    running_total += value
    cumulative.append((running_total / total) * 100)

# Create figure
fig, ax1 = plt.subplots(figsize=(11, 6))

# Bar chart
bars = ax1.bar(categories, frequency)

ax1.set_xlabel("Defect Category")
ax1.set_ylabel("Number of Defects")
ax1.set_title(
    "Pareto Analysis – Restaurant Billing System\n"
    "Q05: Reduce Response Time"
)

ax1.tick_params(axis="x", rotation=35)

# Add frequency labels
for bar, value in zip(bars, frequency):
    ax1.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.05,
        str(value),
        ha="center"
    )

# Cumulative percentage line
ax2 = ax1.twinx()

ax2.plot(
    categories,
    cumulative,
    marker="o"
)

ax2.set_ylabel("Cumulative Percentage")
ax2.set_ylim(0, 110)

# Add 80% reference line
ax2.axhline(
    y=80,
    linestyle="--",
    linewidth=1
)

# Add 80% label
ax2.text(
    len(categories) - 1,
    82,
    "80% reference",
    ha="right"
)

# Improve layout
plt.tight_layout()

# Save chart
output_file = "reports/pareto_chart.png"
plt.savefig(output_file, dpi=200, bbox_inches="tight")

print("=" * 50)
print("Pareto Chart Generated Successfully")
print("=" * 50)
print(f"Saved to: {output_file}")

# Display chart
plt.show()