import streamlit as st
import pandas as pd
from sorting_algorithms import heap_sort
from searching_algorithms import binary_search

st.set_page_config(page_title="IPL Cricket Stats Analyzer", layout="wide")

st.title("🏏 IPL Cricket Stats Analyzer")
st.write("Analyze IPL player statistics using Searching and Sorting Algorithms.")

uploaded_file = st.file_uploader("Upload IPL Players CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("data/ipl_players.csv")

st.subheader("📊 Player Data")
st.dataframe(df)

# Sorting Section
st.subheader("🔽 Sort Players")
sort_key = st.selectbox("Select column to sort:", ["Runs", "Wickets", "Matches"])
if st.button("Apply Heap Sort"):
    data = df.to_dict('records')
    sorted_data = heap_sort(data, sort_key)
    sorted_df = pd.DataFrame(sorted_data)
    st.dataframe(sorted_df)
    st.bar_chart(sorted_df.set_index("Player")[sort_key])

# Searching Section
st.subheader("🔍 Search Player")
search_name = st.text_input("Enter Player Name:")
if st.button("Search"):
    data = df.to_dict('records')
    data_sorted = sorted(data, key=lambda x: x['Player'].lower())  # needed for binary search
    result = binary_search(data_sorted, search_name, 'Player')
    if result:
        st.success(f"Player Found: {result}")
    else:
        st.error("Player not found!")

st.info("This project demonstrates Heap Sort and Binary Search algorithms for IPL data analysis.")
