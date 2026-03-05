import streamlit as st

# Page Title
st.set_page_config(page_title="Movie Ticket Booking", page_icon="🎬", layout="centered")

st.title("🎬 Movie Ticket Booking System")

# Movie List
movies = {
    "Avengers: Endgame": 150,
    "Pathaan": 120,
    "Jawan": 130,
    "Inception": 140,
    "Interstellar": 160,
    "conjuring": 350
}

# Select Movie
movie = st.selectbox("Select Movie", list(movies.keys()))

# Select Show Time
show_time = st.selectbox("Select Show Time", ["10:00 AM", "1:00 PM", "4:00 PM", "7:00 PM", "10:00 PM"])

# Number of Tickets
tickets = st.number_input("Number of Tickets", min_value=1, max_value=10, step=1)

# Customer Name
name = st.text_input("Enter Your Name")

# Price Calculation
price_per_ticket = movies[movie]
total_price = price_per_ticket * tickets

st.write(f"💰 Price per ticket: ₹{price_per_ticket}")
st.write(f"🧾 Total Amount: ₹{total_price}")

# Booking Button
if st.button("Book Ticket"):
    if name == "":
        st.warning("Please enter your name!")
    else:
        st.success("🎉 Booking Confirmed!")
        st.write("----- Booking Details -----")
        st.write(f"Name: {name}")
        st.write(f"Movie: {movie}")
        st.write(f"Show Time: {show_time}")
        st.write(f"Tickets: {tickets}")

        st.write(f"Total Paid: ₹{total_price}")
