# display_webpage.py
import subprocess
import time

# Define the URL of the webpage you want to display
webpage_url = "http://your-website.com"

# Set the start and end times (24-hour format)
start_time = "07:00"
end_time = "21:00"

while True:
    current_time = time.strftime("%H:%M")
    if start_time <= current_time < end_time:
        subprocess.run(["chromium-browser", "--start-fullscreen", webpage_url])
    else:
        # Close the browser if it's open outside the scheduled time
        subprocess.run(["pkill", "chromium-browser"])
    time.sleep(60)  # Check the time every minute