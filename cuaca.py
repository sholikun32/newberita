import streamlit as st
import requests
import json

# Fungsi untuk mendapatkan data cuaca dari API Tomorrow.io
def get_hourly_weather(api_key, latitude, longitude):
    url = f"https://api.tomorrow.io/v4/timelines?location={latitude},{longitude}&fields=temperature&timesteps=1h&units=metric&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

# Menampilkan judul aplikasi
st.title("Perkiraan Cuaca Setiap Jam di Semarang")

# Mendapatkan API key Tomorrow.io (ganti dengan API key Anda)
api_key = "rzNAAHgYeddgMbZf5nWaTC6gnn4q2rM3"

# Mendapatkan data cuaca setiap jam dari API Tomorrow.io
latitude = -6.9667  # Ganti dengan latitude Semarang
longitude = 110.4167  # Ganti dengan longitude Semarang
weather_data = get_hourly_weather(api_key, latitude, longitude)

# Mengambil data temperatur per jam
hourly_temperatures = weather_data['data']['timelines'][0]['intervals']

# Menampilkan data temperatur setiap jam
st.subheader("Temperatur Setiap Jam")
for interval in hourly_temperatures:
    time = interval['startTime']
    temperature = interval['values']['temperature']
    st.write(f"{time}: {temperature}°C")
