import requests
import streamlit as st

# Get NASA API data
nasa_api_key = "J50jMhkniQZYpuxDYWD9Od3bHujg08rmfr88xvkY"
nasa_APOD_api = f"https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}"
get_NASA_APOD = requests.get(nasa_APOD_api)

# Convert APOD data to variables
nasa_APOD = get_NASA_APOD.json()

nasa_PotD_title = str(nasa_APOD["title"])
nasa_PotD_url = nasa_APOD["url"]
nasa_PotD_text = str(nasa_APOD["explanation"])

# Get PotD image
filepath_PoTD = "nasaPotD.jpg"
nasa_PotD_image = requests.get(nasa_PotD_url)
with open(filepath_PoTD, "wb") as file:
    file.write(nasa_PotD_image.content)

# Build web page in StreamLit
st.title(nasa_PotD_title.title())
st.image("nasaPotD.jpg")
st.write(nasa_PotD_text)



