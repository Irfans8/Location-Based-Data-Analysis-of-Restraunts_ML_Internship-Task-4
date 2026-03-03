import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load data
df = pd.read_csv('Dataset .csv')

# 2. Restaurant Distribution by City
print("--- Task 4: Location-based Analysis ---")
city_counts = df['City'].value_counts().head(10)
print("\nTop 10 Cities with the most restaurants:")
print(city_counts)

# Visualization 1: Top 10 Cities
plt.figure(figsize=(12, 6))
sns.barplot(x=city_counts.index, y=city_counts.values, palette='viridis')
plt.title('Top 10 Cities with Highest Restaurant Concentration')
plt.xlabel('City')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=45)
plt.show()

# 3. Average Rating by City
# We group by City and calculate the mean rating
city_ratings = df.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False).head(10)

# Visualization 2: Best Rated Cities
plt.figure(figsize=(12, 6))
sns.barplot(x=city_ratings.index, y=city_ratings.values, palette='magma')
plt.title('Top 10 Cities with Highest Average Ratings')
plt.xlabel('City')
plt.ylabel('Average Aggregate Rating')
plt.xticks(rotation=45)
plt.show()

# 4. Latitude & Longitude Distribution
# This acts as a simple scatter plot "map" of restaurant locations
plt.figure(figsize=(10, 8))
plt.scatter(df['Longitude'], df['Latitude'], alpha=0.5, c=df['Aggregate rating'], cmap='coolwarm')
plt.colorbar(label='Aggregate Rating')
plt.title('Geographical Distribution of Restaurants colored by Rating')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()