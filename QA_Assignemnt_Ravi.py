# QA Engineer Intern_Assignment Round
# Ravi Prakash Singh
# Date = 2023-08-01

import requests


def get_weather_data():
    url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data. Exiting...")
        exit()

def get_weather_info(data, date):
    for item in data['list']:
        if item['dt_txt'].startswith(date):
            return item['main']['temp']
    return None

def get_wind_speed(data, date):
    for item in data['list']:
        if item['dt_txt'].startswith(date):
            return item['wind']['speed']
    return None

def get_pressure(data, date):
    for item in data['list']:
        if item['dt_txt'].startswith(date):
            return item['main']['pressure']
    return None

def main():
    data = get_weather_data()
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            date = input("Enter the date in format 'YYYY-MM-DD': ")
            temp = get_weather_info(data, date)
            if temp is not None:
                print(f"Temperature on {date}: {temp} K")
            else:
                print("Data not available for the provided date.")
        elif choice == 2:
            date = input("Enter the date in format 'YYYY-MM-DD': ")
            wind_speed = get_wind_speed(data, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Data not available for the provided date.")
        elif choice == 3:
            date = input("Enter the date in format 'YYYY-MM-DD': ")
            pressure = get_pressure(data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Data not available for the provided date.")
        elif choice == 0:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()