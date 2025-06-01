import streamlit as st
import requests

st.set_page_config(page_title="EUR/USD Signal Dashboard")
st.title("📉 EUR/USD Signal Dashboard")

API_KEY = "FK2HKXD52BOMUD12"
symbol = "EURUSD"
interval = "1min"
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={API_KEY}"

@st.cache_data(ttl=60)
def fetch_data():
    try:
        response = requests.get(url)
        if response.status_code != 200:
            st.error(f"❌ HTTP Error: {response.status_code}")
            return None
        data = response.json()
        if "Time Series" not in str(data):
            st.warning(f"⚠️ API Response Error: {data}")
            return None
        return data
    except Exception as e:
        st.error(f"🚨 Exception: {str(e)}")
        return None

data = fetch_data()
if data is None:
    st.warning("⚠️ تعذر جلب البيانات من API.")
else:
    st.success("✅ تم جلب البيانات بنجاح.")
