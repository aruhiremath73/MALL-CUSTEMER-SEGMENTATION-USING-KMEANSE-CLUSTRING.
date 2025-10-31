import folium
from folium.plugins import HeatMap
import pandas as pd

# Load accident data
data = pd.read_csv("accidents.csv")

# Create base map centered around the first location
m = folium.Map(location=[data['latitude'].mean(), data['longitude'].mean()],
               zoom_start=13)

# Add heatmap layer
heat_data = [[row['latitude'], row['longitude'], row['severity']] for index, row in data.iterrows()]
HeatMap(heat_data).add_to(m)

# Save map as HTML
m.save("accident_heatmap.html")
