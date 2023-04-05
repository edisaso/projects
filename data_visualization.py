import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('https://raw.githubusercontent.com/edisaso/projects/main/trending.csv')
# Select rows where type is Movie, sort by popularity in descending order, and select top 5
tv_df = df[df['media_type'] == 'movie'].sort_values(by='popularity', ascending=False).drop_duplicates(subset='original_title').head(5)

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(tv_df['original_title'], tv_df['popularity'], color='blue')

# Add labels and title
ax.set_xlabel('Popularity')
ax.set_ylabel('Movie Title')
ax.set_title('Popularity of Top 5 Movies')

# Show the plot
plt.show()
