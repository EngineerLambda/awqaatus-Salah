import streamlit as st
import os
from scrape_time import load_data, split_thirds

st.set_page_config(page_title="Awqaatus Salah", page_icon="🌙")
st.title("Awqaatus Salah - by engineer λ")
st.markdown("Data source: [Islamic Finder](https://www.islamicfinder.org/)")

with st.spinner("Loading date and time from source..."):
    url = os.getenv("SOURCE_URL")
    data = load_data(url)
    thirds = split_thirds(data)

st.subheader("🗓️ Dates")
col1, col2 = st.columns((1, 1))
with col1:
    date = data.get("oyinbo_date")
    st.metric(
        label="Date",
        value=date,
        delta=None,
        help="Today's date according to the Gregorian Calendar (Solar).",
        border=True          
        )
with col2:
    hijra_date = data.get("hijra_date")
    st.metric(
        label="Hijri Date",
        value=hijra_date,
        delta=None,
        help="Today's date according to the Islamic Calendar (Lunar).",
        border=True          
        )
st.divider()
st.subheader("⏰ Salah times for the day")
cols_1, cols_2 = st.columns((1, 1))
with cols_1:
    fajr_time = data.get("fajr_time")
    st.metric(
        label="Fajr",
        value=fajr_time,
        delta=None,
        help="Time for Fajr prayer.",
        border=True          
        )
    zuhr_time = data.get("zhur_time")
    st.metric(
        label="Zuhr",
        value=zuhr_time,
        delta=None,
        help="Time for Zuhr prayer.",
        border=True          
        )
    maghrib_time = data.get("maghrib_time")
    st.metric(
        label="Maghrib",
        value=maghrib_time,
        delta=None,
        help="Time for Maghrib prayer.",
        border=True          
        )
    
with cols_2:
    sunrise_time = data.get("sunrise_time")
    st.metric(
        label="Sunrise",
        value=sunrise_time,
        delta=None,
        help="Time of sunrise.",
        border=True          
        )
    
    
    asr_time = data.get("asr time")
    st.metric(
        label="Asr",
        value=asr_time,
        delta=None,
        help="Time for Asr prayer.",
        border=True          
        )
    isha_time = data.get("isha_time")
    st.metric(
        label="Isha",
        value=isha_time,
        delta=None,
        help="Time for Isha prayer.",
        border=True          
        )
    
st.divider()
st.subheader("🕒 The thirds of the Night")


first_third = thirds["first_third"]
st.metric(
    label="First third",
    value=f"{first_third[0]} - {first_third[1]}",
    delta=None,
    help="First third of the night.",
    border=True          
    )

second_third = thirds["second_third"]
st.metric(
    label="Second third",
    value=f"{second_third[0]} - {second_third[1]}",
    delta=None,
    help="Second third of the night.",
    border=True          
    )

last_third = thirds["last_third"]
st.metric(
    label="Last third",
    value=f"{last_third[0]} - {last_third[1]}",
    delta=None,
    help="Last third of the night.",
    border=True          
    )                       
    