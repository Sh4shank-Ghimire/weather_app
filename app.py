import requests

api_key = "1accdc3e72f48c416993185dcd5c87c6"

user = input("Enter a city: ")

weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={user}&appid={api_key}&units=metric")
data = weather_data.json()
print(data)

weather = {
    "Weather" : data["weather"][0]["main"],
    "Description" : data["weather"][0]["description"],
    "Temperature" : data["main"]["temp"]
}

print(f"Weather = {weather['Weather']}, Description: {weather['Description']}, Temperature: {weather["Temperature"]}")