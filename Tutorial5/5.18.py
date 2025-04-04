import pandas as pd
import matplotlib.pyplot as plt

weather_data = pd.read_csv("weather.csv")

# 1) Print first 10 rows of weather data
print("First 10 Rows of Weather Data:\n", weather_data.head(10))

# 2) Find the maximum and minimum temperature
highest_temp = weather_data["temperature"].max()
lowest_temp = weather_data["temperature"].min()
print("\nMaximum Temperature:", highest_temp)
print("Minimum Temperature:", lowest_temp)

# 3) List the places with temperature less than 28°C
cool_places = weather_data[weather_data["temperature"] < 28]["place"].unique()
print("\nPlaces with Temperature Less Than 28°C:\n", cool_places)

# 4) List the places with weather = “Cloudy”
overcast_places = weather_data[weather_data["weather"] == "Cloudy"]["place"].unique()
print("\nPlaces with Cloudy Weather:\n", overcast_places)

# 5) Sort and display each weather type and its frequency
weather_counts = weather_data["weather"].value_counts()
print("\nWeather Frequency:\n", weather_counts)

# 6) Create a bar plot to visualize temperature of each day
plt.figure(figsize=(10, 5))
plt.bar(weather_data["date"], weather_data["temperature"], color="blue")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trend Over Time")
plt.xticks(rotation=45)  
plt.show()
