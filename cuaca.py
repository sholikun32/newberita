import streamlit as st
import requests
from datetime import datetime

# Fungsi untuk mendapatkan data cuaca
def get_weather_data(api_key, latitude, longitude):
    url = f'https://api.tomorrow.io/v4/weather/forecast?location={latitude},{longitude}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

# Fungsi untuk menampilkan data cuaca saat ini
def display_current_weather(data):
    current_weather = data['current']
    temperature = current_weather['temperature']
    weather_description = current_weather['weather']['description']
    st.write(f"**Cuaca saat ini:** {weather_description}")
    st.write(f"**Suhu saat ini:** {temperature}°C")

# Fungsi untuk menampilkan prediksi cuaca satu minggu ke depan
def display_weekly_forecast(data):
    daily_forecast = data['daily']['data']
    st.write("**Prediksi Cuaca Minggu Ini:**")
    for day_data in daily_forecast:
        date = datetime.utcfromtimestamp(day_data['time']).strftime('%Y-%m-%d')
        temperature_min = day_data['temperatureMin']
        temperature_max = day_data['temperatureMax']
        weather_description = day_data['weather']['description']
        st.write(f"**Tanggal:** {date}")
        st.write(f"**Cuaca:** {weather_description}")
        st.write(f"**Suhu Min:** {temperature_min}°C")
        st.write(f"**Suhu Max:** {temperature_max}°C")
        st.write("---")

# Judul dan deskripsi aplikasi
st.title("Aplikasi Prediksi Cuaca Semarang")
st.write("Aplikasi ini menampilkan cuaca saat ini dan prediksi cuaca satu minggu ke depan untuk kota Semarang.")

# Gantilah 'YOUR_API_KEY' dengan API key Tomorrow.io Anda
api_key = 'YOUR_API_KEY'
latitude = -6.9716  # Koordinat lintang Semarang
longitude = 110.4256  # Koordinat bujur Semarang

# Mendapatkan data cuaca dari API
weather_data = get_weather_data(api_key, latitude, longitude)

# Menampilkan data cuaca saat ini
display_current_weather(weather_data)

# Menampilkan prediksi cuaca satu minggu ke depan
display_weekly_forecast(weather_data)
