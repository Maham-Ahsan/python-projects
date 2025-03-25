import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "America/Los_Angeles",
    "America/Chicago",
    "America/Toronto",
    "Europe/London",
    "Europe/Paris",
    "Europe/Berlin",
    "Europe/Rome",
    "Europe/Madrid",
    "Europe/Moscow",
    "Asia/Dubai",
    "Asia/Tokyo",
    "Asia/Shanghai",
    "Asia/Kolkata",
    "Asia/Singapore",
    "Asia/Bangkok",
    "Australia/Sydney",
    "Australia/Melbourne",
    "Australia/Perth",
    "Africa/Johannesburg",
]

st.title("Time Zone App")

selected_timezone = st.multiselect("Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"])

st.subheader("Selected Timezones")
for tz in selected_timezone:

    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")

    st.write(f"**{tz}**: {current_time}")

st.subheader("Convert Time Between TimeZones")

current_time = st.time_input("Current Time", value=datetime.now().time())

from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)

to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

if st.button("Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))

    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")
    st.success(f"Converted Time in {to_tz}: {converted_time}")