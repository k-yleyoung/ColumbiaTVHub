from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import schedule
import time

app = Flask(__name__)

# Function to scrape text from a website
def scrape_text():

    from bs4 import BeautifulSoup
    import requests

    # Web scraping

    html_text = requests.get('https://www.columbiatribune.com/news/').text

    soup = BeautifulSoup(html_text, 'lxml')

    headline = soup.find('a', class_ = 'gnt_m_he')

    sub_headlines = soup.find_all('a', class_ = 'gnt_m_th_a')

    #print(f"MAIN HEADLINER: {headline.text}")

    #for subs, sub_headlines in enumerate(sub_headlines[:4]):
        #print(f"Sub-Headline {subs + 1}: {sub_headlines.text}")

    #Web scraping^^

    scraped_data = [
        {"Headliner": headline.text},
        {"Sub-Headline 1": sub_headlines[0].text},
        {"Sub-Headline 2": sub_headlines[1].text},
        {"Sub-Headline 3": sub_headlines[2].text},
        {"Sub-Headline 4": sub_headlines[3].text},

        # ... more scraped data
    ]

    # Return the scraped text
    return scraped_data

# Function to fetch local weather
def get_local_weather():
    #Fetching Weather

    api_key = "da4fbd7238251945fbabb50f5ec87828"

    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": "Columbia, US",  # Replace with the city and country
        "appid": "da4fbd7238251945fbabb50f5ec87828",
        "units": "imperial"  # Choose the desired units (metric, imperial, standard)
    }

    response = requests.get(base_url, params= params)

    temperature = humidity = weather_description = temp_max = temp_min = "N/A"

    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]
        temp_max = data["main"]["temp_max"]
        temp_min = data["main"]["temp_min"]
        print(f"Temperature: {temperature}°F")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description}")
        print(f"Temperature High: {temp_max}°F")
        print(f"Temperature Low: {temp_min}°F")
    else:
        print("Error:", response.status_code)
    #Fetching Weather^^

    weather_data = [
        {"Temperature": temperature},
        {"Humidity": humidity},
        {"Weather Description": weather_description},
        {"Temperature High": temp_max},
        {"Temperature Low": temp_min},

        # ... more scraped data
    ]
    # Return the weather information


    return weather_data

# Function to update data periodically
def update_data_periodically():
    # Define the schedule
    schedule.every(1).minutes.do(update_data)  # Update data every 1 minute

    # Run the scheduler in the background
    while True:
        schedule.run_pending()
        time.sleep(1)  # Sleep for 1 second to avoid high CPU usage

def update_data():
    scraped_data = scrape_text()
    weather_info = get_local_weather()
    app.config['SCRAPE_DATA'] = scraped_data
    app.config['WEATHER_DATA'] = weather_info  # Store weather data in the app config

@app.route('/')
def index():
    scraped_data = app.config.get('SCRAPE_DATA', [])
    weather_info = app.config.get('WEATHER_DATA', [])  # Retrieve weather data from app config
    return render_template('index.html', data=scraped_data, weather=weather_info)

if __name__ == '__main__':
    update_data()  # Populate the initial data
    import threading
    data_update_thread = threading.Thread(target=update_data_periodically)
    data_update_thread.daemon = True
    data_update_thread.start()
    app.run(host='0.0.0.0', port=8080)