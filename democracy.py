import pandas as pd
import matplotlib.pyplot as plt

# Sample data: Country, Democracy Rank (from democracymatrix.com 2020), Democracy Score (0-1),
# Approx HDI (2024/2025), Happiness Score (2025 report)
data = {
    'Country': ['Denmark', 'Norway', 'Finland', 'Sweden', 'Germany', 'Switzerland', 'Netherlands',
                'New Zealand', 'Belgium', 'Costa Rica', 'Spain', 'Australia', 'Estonia', 'Ireland',
                'United Kingdom', 'Canada', 'United States', 'Uruguay', 'South Korea', 'Japan'],
    'Democracy_Rank': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16, 17, 24, 36, 27, 20, 25],
    'Democracy_Score': [0.958, 0.956, 0.946, 0.946, 0.944, 0.934, 0.93, 0.928, 0.925, 0.914,
                        0.912, 0.904, 0.903, 0.898, 0.892, 0.86, 0.811, 0.847, 0.883, 0.857],
    'HDI': [0.948, 0.961, 0.940, 0.947, 0.942, 0.962, 0.946, 0.937, 0.931, 0.809,
            0.905, 0.946, 0.890, 0.945, 0.926, 0.929, 0.921, 0.809, 0.925, 0.925],  # Approx recent values
    'Happiness': [7.58, 7.30, 7.74, 7.34, 7.03, 7.24, 7.32, 7.12, 6.89, 7.07,
                  7.07, 7.06, 6.95, 7.09, 6.92, 7.03, 6.39, 6.62, 6.06, 6.06]  # Approx 2025 scores
}

df = pd.DataFrame(data)

# Sort by Democracy Rank for visualization
df_sorted = df.sort_values('Democracy_Rank')

# 1. Bar chart of Democracy Score by Rank
plt.figure(figsize=(12, 6))
plt.bar(df_sorted['Country'], df_sorted['Democracy_Score'], color='skyblue')
plt.xticks(rotation=90)
plt.title('Democracy Score by Country (Sorted by Democracy Matrix Rank)')
plt.ylabel('Democracy Score (0-1)')
plt.tight_layout()
plt.show()

# 2. Scatter: Democracy vs HDI
plt.figure(figsize=(10, 6))
plt.scatter(df['Democracy_Score'], df['HDI'], color='green')
for i, row in df.iterrows():
    plt.text(row['Democracy_Score'] + 0.001, row['HDI'], row['Country'], fontsize=9)
plt.xlabel('Democracy Score')
plt.ylabel('HDI')
plt.title('Democracy Score vs Human Development Index')
plt.grid(True)
plt.show()

# 3. Scatter: Democracy vs Happiness
plt.figure(figsize=(10, 6))
plt.scatter(df['Democracy_Score'], df['Happiness'], color='orange')
for i, row in df.iterrows():
    plt.text(row['Democracy_Score'] + 0.001, row['Happiness'], row['Country'], fontsize=9)
plt.xlabel('Democracy Score')
plt.ylabel('Happiness Score')
plt.title('Democracy Score vs Happiness Score')
plt.grid(True)
plt.show()

# 4. Correlation
print("Correlations:")
print(df[['Democracy_Score', 'HDI', 'Happiness']].corr())