import os
import time

import requests
from earthquake import Earthquake
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Get URL to send requests from environment variables
URL = os.getenv("URL")

# Get period of requests in seconds from environment variables
period = float(os.getenv("PERIOD"))

# Create an Earthquake object to keep track of the latest earthquake
current_earthquake = Earthquake()

# Start an infinite loop to continuously check for new earthquake data
while True:

    # Send a GET request to the specified URL
    r = requests.get(URL)

    # Parse HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(r.content, "html.parser")

    # Find relevant table body containing all earthquakes
    contents = soup.find("tbody").findNext("tr").contents

    # Extract texts content of the first 7 element
    data = [contents[i].text for i in range(7)]

    # Create a new Earthquake object with the extracted data
    new_earthquake = Earthquake(data)

    # Check if the date of the new earthquake is different from the current earthquake
    if new_earthquake.getDate() != current_earthquake.getDate():

        # Update current earthquake with the new earthquake
        current_earthquake = new_earthquake

        # Format new earthquake information and print it
        information = "Date: {}, Latitude: {}, Longitude: {}, Depth: {}, Type: {}, Magnitude: {}, Location: {}".format(
            current_earthquake.getDate(),
            current_earthquake.getLatitude(),
            current_earthquake.getLongitude(),
            current_earthquake.getDepth(),
            current_earthquake.getType(),
            current_earthquake.getMagnitude(),
            current_earthquake.getLocation(),
        )

        print("New earthquake information:")
        print(information)

    else:
        # Format current earthquake information and print it
        information = "Date: {}, Latitude: {}, Longitude: {}, Depth: {}, Type: {}, Magnitude: {}, Location: {}".format(
            current_earthquake.getDate(),
            current_earthquake.getLatitude(),
            current_earthquake.getLongitude(),
            current_earthquake.getDepth(),
            current_earthquake.getType(),
            current_earthquake.getMagnitude(),
            current_earthquake.getLocation(),
        )

        print("There is no new earthquake. Latest earthquake information:")
        print(information)
    time.sleep(period)
