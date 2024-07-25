import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
import time
import threading

st.title("News Headlines Scraper")

# Function to scrape data
def scrape_data():
    url_site = "https://www.shahrekhabar.com/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D9%88%D8%B1%D8%B2%D8%B4%DB%8C"
    site = requests.get(url_site)
    soup = BeautifulSoup(site.text, 'html.parser')

    UL = soup.find_all('ul', {'class': 'news-list-items clearfix'})

    if not UL:
        return pd.DataFrame(columns=['تیتر خبر'])

    LI = UL[1].find_all('li')
    LI_LIST = [li.a.text for li in LI]

    df = pd.DataFrame({'تیتر خبر': LI_LIST})
    return df

# Function to update data in a separate thread
def update_data():
    while True:
        data = scrape_data()
        st.session_state.data = data
        time.sleep(60)

# Initialize session state
if 'data' not in st.session_state:
    st.session_state.data = scrape_data()

# Start the data update thread
if 'thread_started' not in st.session_state:
    st.session_state.thread_started = True
    threading.Thread(target=update_data, daemon=True).start()

# Display the data
if st.session_state.data.empty:
    st.write("No data found.")
else:
    st.write(st.session_state.data)
