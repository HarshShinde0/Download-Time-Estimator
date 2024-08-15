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

# Calculate the remaining amount to download
remaining_mb = total_size_mb - downloaded_mb

# Calculate time remaining in seconds
time_remaining_seconds = remaining_mb / download_speed

# Convert seconds to hours, minutes, and seconds
hours = int(time_remaining_seconds // 3600)
minutes = int((time_remaining_seconds % 3600) // 60)
seconds = int(time_remaining_seconds % 60)

# Display the result
st.write(f"Time remaining: {hours} hours, {minutes} minutes, and {seconds} seconds")
