import streamlit as st
import requests

# Judul aplikasi
st.title("Aplikasi Prakiraan Cuaca Kota Semarang")

# Koordinat lokasi Kecamatan Semarang Utara
latitude = -6.9866
longitude = 110.4314

# API Key
api_key = "rzNAAHgYeddgMbZf5nWaTC6gnn4q2rM3"

# URL API
url = f"https://api.tomorrow.io/v4/weather/forecast?location={latitude},{longitude}&apikey={api_key}"

# Mengambil data cuaca dari API
response = requests.get(url)

# Memeriksa apakah permintaan berhasil atau tidak
if response.status_code == 200:
    data = response.json()

    # Menampilkan informasi cuaca
    st.subheader("Informasi Cuaca")
    st.write(f"Lokasi: {data['location']['name']}, {data['location']['country']}")

    # Menampilkan prakiraan cuaca
    st.subheader("Prakiraan Cuaca")
    for forecast in data['data']['timelines'][0]['intervals']:
        time = forecast['startTime']
        temperature = forecast['values']['temperature']
        precipitation = forecast['values']['precipitationIntensity']
        st.write(f"Waktu: {time}, Temperatur: {temperature}°C, Intensitas Presipitasi: {precipitation} mm/h")

else:
    st.error("Gagal mengambil data cuaca. Silakan coba lagi nanti.")
