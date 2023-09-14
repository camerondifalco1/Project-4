import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('C:/Users/CDiFa/OneDrive/Uni - Data Analytics/Project 4/Project 4 - 2/housing.csv')

# Display basic info about the data
print(df.info())

# Basic Statistics
print(df.describe())

# Histograms for numerical columns
df.hist(figsize=(12, 12))
plt.show()

# Scatterplot for longitude and latitude (possibly showing location clusters)
sns.scatterplot(x='longitude', y='latitude', data=df, hue='ocean_proximity', palette='viridis')
plt.show()

# Boxplot for housing_median_age based on ocean_proximity
sns.boxplot(x='ocean_proximity', y='housing_median_age', data=df)
plt.show()

# Correlation Heatmap
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()

# Scatterplot for median_income vs median_house_value
sns.scatterplot(x='median_income', y='median_house_value', data=df)
plt.show()
