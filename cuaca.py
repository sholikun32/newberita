import streamlit as st
import requests
import json

# URL dan API Key Tomorrow.io
url = 'https://api.tomorrow.io/v4/weather/forecast'
api_key = 'YOUR_API_KEY'  # Gantilah dengan API Key Anda sendiri
location = '42.3478,-71.0466'  # Koordinat Semarang

# Fungsi untuk mendapatkan data cuaca dari API Tomorrow.io
def get_weather_data(api_key, location):
    params = {
        'location': location,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

# Mengambil data cuaca dari API
weather_data = get_weather_data(api_key, location)

# Menampilkan judul aplikasi
st.title('Perkiraan Cuaca dan Prediksi Cuaca Seminggu ke Depan di Semarang')

# Menampilkan data cuaca saat ini
current_weather = weather_data.get('current', {})
if current_weather:
    st.subheader('Cuaca saat ini')
    st.write(f'Temperatur: {current_weather.get("temperature")} °C')
    st.write(f'Kelembaban: {current_weather.get("humidity")}%')
    st.write(f'Cuaca: {current_weather.get("weather").get("description")}')

# Menampilkan prediksi cuaca satu minggu ke depan
daily_forecast = weather_data.get('daily', {}).get('data', [])
if daily_forecast:
    st.subheader('Prediksi Cuaca 1 Minggu ke Depan')
    for day in daily_forecast:
        date = day.get('time')
        temperature_high = day.get('temperatureHigh')
        temperature_low = day.get('temperatureLow')
        weather_description = day.get('weather').get('description')
        st.write(f'Date: {date}')
        st.write(f'Temperature High: {temperature_high} °C')
        st.write(f'Temperature Low: {temperature_low} °C')
        st.write(f'Weather: {weather_description}')
        st.write('---')
else:
    st.warning('Data prediksi cuaca tidak tersedia.')

# Menambahkan tautan ke sumber data
st.markdown('[Sumber Data](https://www.tomorrow.io/weather-api/)')
