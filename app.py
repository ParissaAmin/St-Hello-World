import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
from streamlit_autorefresh import st_autorefresh

# New code for fetching and displaying news
st.header("News")

def fetch_news():
    url_site = "https://www.shahrekhabar.com/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D9%88%D8%B1%D8%B2%D8%B4%DB%8C"
    site = requests.get(url_site)
    soup = BeautifulSoup(site.text, 'html.parser')

    UL = soup.find_all('ul', {'class': 'news-list-items clearfix'})

    if len(UL) > 1:
        LI = UL[1].find_all('li')

        LI_LIST = []
        for i in range(len(LI)):
            LI_LIST.append(LI[i].a.text)

        df = pd.DataFrame()
        df['تیتر خبر'] = LI_LIST
        return df
    else:
        return pd.DataFrame(columns=['تیتر خبر'])

# Streamlit app
st.title('Real-time News Headlines')

# Create a placeholder for the DataFrame
placeholder = st.empty()

# Auto-refresh every 60 seconds
count = st_autorefresh(interval=60000, key="datarefresh")

# Fetch and display the news headlines
df = fetch_news()
with placeholder.container():
    st.table(df)
