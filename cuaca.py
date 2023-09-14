import streamlit as st
import requests
import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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

# Membuat DataFrame dari data temperatur per jam
df = pd.DataFrame(hourly_temperatures)
df['time'] = pd.to_datetime(df['startTime'])
df.set_index('time', inplace=True)

# Membuat grafik temperatur
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['values.temperature'], mode='lines', name='Temperatur (°C)'))
fig.update_layout(
    title="Grafik Temperatur Setiap Jam",
    xaxis_title="Waktu",
    yaxis_title="Temperatur (°C)",
)

# Menampilkan grafik temperatur
st.plotly_chart(fig)

# Menampilkan gambar temperatur
st.image("https://your-image-url.com/temperature_image.png", caption="Contoh Gambar Temperatur", use_container_width=True)
