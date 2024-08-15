import streamlit as st

# Title
st.title("Download Time Estimator")

# Heading
st.header("Estimate the Time Remaining for Your Download")

# User inputs
total_size_gb = st.number_input("Total Size (GB)", value=66.4)
downloaded_mb = st.number_input("Downloaded (MB)", value=980)
download_speed = st.number_input("Download Speed (MB/s)", value=6.02)

# Convert total size to MB (1 GB = 1024 MB)
total_size_mb = total_size_gb * 1024