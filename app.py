import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fungsi untuk melakukan web scraping dari Google News
def scrape_google_news(query, location):
    base_url = "https://news.google.com"
    news_url = f"{base_url}/search?q={query}+kesehatan+{location}&hl=id-ID&gl=ID&ceid=ID%3Aid"
    response = requests.get(news_url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("h3", class_="ipQwMb ekueJc RD0gLb")
    news_data = []

    for article in articles:
        title = article.get_text()
        link = article.a["href"]

        # Dapatkan deskripsi dan nama situs/web dari setiap artikel
        article_url = f"{base_url}{link[1:]}"
        article_response = requests.get(article_url)
        article_soup = BeautifulSoup(article_response.text, "html.parser")
        
        description = article_soup.find("meta", {"name": "description"})
        site_name = article_soup.find("meta", {"property": "og:site_name"})
        
        if description:
            description = description["content"]
        else:
            description = ""
        
        if site_name:
            site_name = site_name["content"]
        else:
            site_name = ""
        
        news_data.append({
            "title": title,
            "link": f"{base_url}{link}",
            "description": description,
            "site_name": site_name
        })

    return news_data

# Streamlit UI
st.title("Berita Tren Kesehatan di Kota Semarang")
query = st.text_input("Masukkan kata kunci berita", "covid-19")
location = st.text_input("Lokasi (misal: Semarang)", "Semarang")

if st.button("Cari Berita"):
    if not query or not location:
        st.warning("Mohon isi kata kunci berita dan lokasi.")
    else:
        st.info(f"Mencari berita tentang '{query} kesehatan {location}'...")
        news_data = scrape_google_news(query, location)

        if news_data:
            st.success("Berita ditemukan!")

            # Membuat DataFrame dari data berita
            df = pd.DataFrame(news_data)

            # Menampilkan tabel
            st.table(df)
        else:
            st.warning("Tidak ada berita yang ditemukan.")

# Visualisasi grafik dan Word Cloud (seperti sebelumnya)

# Menampilkan footer
st.text("Dibuat oleh [Nama Anda]")
