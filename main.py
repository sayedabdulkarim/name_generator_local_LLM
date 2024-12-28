import streamlit as st

from langchain_helper import generate_restaurant_name_and_items

##render
st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American"))

if cuisine:
    response = generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(",")

    for item in menu_items:
        st.write("- ", item)
