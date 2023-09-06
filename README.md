# ColumbiaTVHub
A webpage displaying Columbia, Missouri's weather and news.

The goal of this website was to display local news headlines and weather data all in plain text on my TV. 
In order to display this data on my TV I needed something to connect to my TV to run the code and display the information.
In my case, I decided to use a raspberry pi 400. On a code level, I needed to build something to scrape the web for local news headlines
and I also needed to retreive local weather data. In order to find local news headlines, I decided to use the beautifulsoup4 
python web scraping library. This allowed me to parse through the html elements to display on my TV. To display Columbia Missouri's weather,
I used the openweathermap API. Originally, I tried to build a GUI with python's tkinter library, but it was much easier to display 
the data on a basic HTML/CSS webpage. "openScript.py" is to be ran at the same time as app.py in order to open the webpage at 7am and
close the webpage at 9pm. 

Video demonstration: https://youtube.com/shorts/kuPyDRtRveA?
