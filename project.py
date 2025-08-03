import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Sample air quality data with current date
data = {
    'city': ['delhi', 'mumbai', 'kolkata', 'chennai', 'banglore', 'hyderabad', 'pune', 'ahemdabad', 'jaipur', 'lucknow'],
    'date': [pd.to_datetime(datetime.today().date())] * 10,
    'no2': [80, 50, 60, 40, 30, 70, 45, 65, 90, 55],
    'so2': [30, 20, 25, 15, 10, 25, 18, 28, 35, 22],
    'pm25': [150, 90, 110, 70, 60, 130, 85, 120, 160, 100]
}

air_quality_df = pd.DataFrame(data)

# 1. Basic data exploration
print("\n📊 First 5 Rows:")
print(air_quality_df.head())
print("\nℹ️ DataFrame Info:")
print(air_quality_df.info())

print("#" * 100)

# 2. PM2.5 Analysis
average_pm25 = air_quality_df['pm25'].mean()
print("\n🌫️ Average PM2.5 across cities:", average_pm25)

print("#" * 100)

# 3. City with highest NO2 levels
city_highest_no2 = air_quality_df.loc[air_quality_df['no2'].idxmax(), 'city']
print("\n🏙️ City with highest NO2 Levels:", city_highest_no2)

print("#" * 100)

# 4. Correlation between PM2.5 and NO2
correlation_pm25_no2 = air_quality_df['pm25'].corr(air_quality_df['no2'])
print("\n📈 Correlation between PM2.5 and NO2:", correlation_pm25_no2)

print("#" * 200)

# 5. Bar chart of PM2.5 Levels by city
plt.figure(figsize=(12, 6))
sns.barplot(x='city', y='pm25', data=air_quality_df, palette='coolwarm')
plt.title('PM2.5 Levels by City')
plt.xlabel('City')
plt.ylabel('PM2.5 (µg/m³)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pm25_by_city.png')  # 🔽 Save plot as image
plt.show()

# 6. Scatter plot of PM2.5 vs NO2
plt.figure(figsize=(8, 6))
sns.scatterplot(x='pm25', y='no2', hue='city', data=air_quality_df, s=100)
plt.title('PM2.5 vs NO2 Levels')
plt.xlabel('PM2.5 (µg/m³)')
plt.ylabel('NO2 (µg/m³)')
plt.tight_layout()
plt.savefig('pm25_vs_no2_scatter.png')  # 🔽 Save plot as image
plt.show()

# 7. Heatmap of correlations between pollutants
plt.figure(figsize=(6, 4))
pollutants = air_quality_df[['pm25', 'no2', 'so2']]
correlation_matrix = pollutants.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='YlGnBu', linewidths=0.5)
plt.title('Correlation Between Pollutants')
plt.tight_layout()
plt.savefig('pollutant_correlation_heatmap.png')  # 🔽 Save heatmap
plt.show()

# 8. Export DataFrame to CSV
air_quality_df.to_csv('air_quality_data.csv', index=False)
print("\n✅ Data exported to air_quality_data.csv")
