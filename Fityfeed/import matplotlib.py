import matplotlib.pyplot as plt
import seaborn as sns

# Data for the chart
weeks = [
    "week 1", "week 2", "week 3", "week 4", "week 5", "week 6", "week 7", 
    "week 8", "week 9", "week 10", "week 11", "week 12", "week 13", 
    "week 14", "week 15"
]
activities = [
    "Basics of Python", "Basics of Python", "Basics of Python", 
    "Learnt about Transformers", "Learnt about Transformers", 
    "Learnt about Document QA", "Learnt about Document QA", 
    "Learnt about Document QA", "Annotations on images", "Annotations on images", 
    "Annotations on images", "Annotations on images", "Annotations on images", 
    "Creating Dataset", "Training Model"
]

# Generate y positions for each week and activity
y_positions = list(range(len(weeks)))

# Use a pastel color palette from seaborn
palette = sns.color_palette("pastel", n_colors=len(set(activities)))

# Map activities to their corresponding colors
activity_colors = {activity: palette[i] for i, activity in enumerate(set(activities))}

# Create the Gantt chart
fig, ax = plt.subplots(figsize=(12, 6))

for i, (week, activity) in enumerate(zip(weeks, activities)):
    ax.barh(
        y_positions[i], 1, left=i, color=activity_colors[activity],
        edgecolor="black", label=activity if activity not in ax.get_legend_handles_labels()[1] else ""
    )

# Customize aesthetics
ax.set_yticks(y_positions)
ax.set_yticklabels(weeks, fontsize=8)
ax.set_xlabel("Weeks", fontsize=10)
ax.set_title("15-Week Internship Gantt Chart", fontsize=14, fontweight="bold")

# Add grid lines for clarity
ax.xaxis.grid(True, linestyle="--", alpha=0.5)
ax.yaxis.grid(True, linestyle="--", alpha=0.5)

# Add a legend
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))  # Remove duplicate labels
ax.legend(by_label.values(), by_label.keys(), title="Activities", loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=3)

# Final layout adjustments and show the plot
plt.tight_layout()
plt.show()
