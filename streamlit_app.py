import streamlit as st
import requests

st.set_page_config(page_title="EUR/USD Signal App", layout="centered")

st.title("📉 EUR/USD Signal Dashboard")

API_KEY = "FK2HKXD52BOMUD12"
symbol = "EURUSD"
interval = "1min"
url = f"https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=EUR&to_symbol=USD&interval={interval}&apikey={API_KEY}"

@st.cache_data(ttl=60)
def fetch_data():
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    try:
        time_series = data[f"Time Series FX ({interval})"]
        latest_timestamp = list(time_series.keys())[0]
        latest_data = time_series[latest_timestamp]
        close_price = float(latest_data["4. close"])
        return {
            "timestamp": latest_timestamp,
            "close": close_price
        }
    except KeyError:
        return None

data = fetch_data()

if data:
    st.markdown(f"**Date:** {data['timestamp']}")
    st.markdown(f"**Close:** {data['close']}")
    
    # مثال على إشارة بسيطة جداً
    if data["close"] > 1.09:
        st.success("📈 Final Signal: BUY")
    elif data["close"] < 1.08:
        st.error("📉 Final Signal: SELL")
    else:
        st.info("📍 Final Signal: NO TRADE")

else:
    st.warning("⚠️ تعذر جلب البيانات من API.")
