import streamlit as st
import requests
import json

# Fungsi untuk mendapatkan data cuaca dari API Tomorrow.io
def get_weather_data(api_key, latitude, longitude):
    url = f"https://api.tomorrow.io/v4/weather/forecast?location={latitude},{longitude}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

# Menampilkan judul aplikasi
st.title("Perkiraan Cuaca dan Prediksi Cuaca di Semarang")

# Mendapatkan API key Tomorrow.io (ganti dengan API key Anda)
api_key = "rzNAAHgYeddgMbZf5nWaTC6gnn4q2rM3"

# Mendapatkan data cuaca dari API Tomorrow.io
latitude = -6.9667  # Ganti dengan latitude Semarang
longitude = 110.4167  # Ganti dengan longitude Semarang
weather_data = get_weather_data(api_key, latitude, longitude)

# Menampilkan data cuaca saat ini
current_weather = weather_data['current']
st.subheader("Cuaca Saat Ini")
st.write(f"Temperatur: {current_weather['temperature']}°C")
st.write(f"Kelembaban: {current_weather['humidity']}%")
st.write(f"Kondisi Cuaca: {current_weather['weather']['description']}")

# Menampilkan prediksi cuaca satu minggu ke depan
st.subheader("Prediksi Cuaca 1 Minggu ke Depan")
daily_forecast = weather_data['daily']['data']
for day in daily_forecast:
    date = day['time']
    temperature_low = day['temperatureLow']
    temperature_high = day['temperatureHigh']
    weather_description = day['weather']['description']
    st.write(f"{date}:")
    st.write(f"  Temperatur Rendah: {temperature_low}°C")
    st.write(f"  Temperatur Tinggi: {temperature_high}°C")
    st.write(f"  Kondisi Cuaca: {weather_description}")
