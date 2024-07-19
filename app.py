import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

@st.cache_data(ttl=60)
def fetch_news():
    try:
        url_site = "https://www.shahrekhabar.com/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D9%88%D8%B1%D8%B2%D8%B4%DB%8C"
        site = requests.get(url_site)
        soup = BeautifulSoup(site.text, 'html.parser')

        UL = soup.find_all('ul', {'class': 'news-list-items clearfix'})
        if len(UL) > 1:
            LI = UL[1].find_all('li')
            LI_LIST = [li.a.text for li in LI]
            return pd.DataFrame({'تیتر خبر': LI_LIST})
        else:
            return pd.DataFrame(columns=['تیتر خبر'])
    except Exception as e:
        st.error(f"Error fetching news: {e}")
        return pd.DataFrame(columns=['تیتر خبر'])

st.title('Real-time News Headlines')
st.header("News")

df = fetch_news()
st.table(df)
