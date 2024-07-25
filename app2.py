import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

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

# Display the data
data = scrape_data()
if data.empty:
    st.write("No data found.")
else:
    st.write(data)

# Automatically refresh the app every 60 seconds
st_autorefresh = st.experimental_rerun
