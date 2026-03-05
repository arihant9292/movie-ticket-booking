import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Movie Ticket Booking", layout="wide")

# --------------------------
# Dummy Database
# --------------------------
if "bookings" not in st.session_state:
    st.session_state.bookings = []

if "seats" not in st.session_state:
    rows = ["A", "B", "C", "D", "E"]
    cols = range(1, 9)
    st.session_state.seats = {f"{r}{c}": False for r in rows for c in cols}


import streamlit as st

st.title("🎬 Movie Ticket Booking System")

# Movie selection
movies = ["Avengers", "Jawan", "Inception", "Interstellar", "conjuring", "spiderman"]
movie = st.selectbox("Select Movie", movies)

# Show time
time = st.selectbox("Select Show Time", ["10 AM", "1 PM", "4 PM", "7 PM"])

# Seat layout
st.subheader("Select Your Seats")

rows = ["A","B","C","D"]
cols = range(1,6)

selected_seats = []

for r in rows:
    cols_layout = st.columns(5)
    for i,c in enumerate(cols):
        seat = f"{r}{c}"
        if cols_layout[i].checkbox(seat):
            selected_seats.append(seat)

st.write("Selected Seats:", selected_seats)

# Ticket price
price = 150
total = price * len(selected_seats)

st.write("Total Price: ₹", total)

# Booking
name = st.text_input("Enter Your Name")

if st.button("Book Ticket"):
    if name == "":
        st.warning("Enter your name")
    elif len(selected_seats) == 0:
        st.warning("Please select seats")
    else:
        st.success("Booking Confirmed 🎉")
        st.write("Name:", name)
        st.write("Movie:", movie)
        st.write("Show Time:", time)
        st.write("Seats:", selected_seats)
        st.write("Total Paid: ₹", total)




   # --------------------------
    # Payment Section
    # --------------------------
    st.subheader("💳 Payment")

    payment_method = st.radio("Select Payment Method",
                              ["UPI", "Credit Card", "Debit Card"])

    if payment_method == "UPI":
        upi_id = st.text_input("Enter UPI ID")

    if payment_method in ["Credit Card", "Debit Card"]:
        card_number = st.text_input("Card Number")
        expiry = st.text_input("Expiry Date")
        cvv = st.password_input("CVV")

    
    # --------------------------
    # Booking Button
    # --------------------------
    if st.button("Confirm Booking"):

        if len(selected_seats) != tickets:
            st.error("Please select exact number of seats!")
        elif name == "":
            st.error("Please enter your name")
        else:
            for seat in selected_seats:
                st.session_state.seats[seat] = True

            booking_data = {
                "Name": name,
                "Movie": movie,
                "Date": date,
                "Time": time,
                "Seats": selected_seats,
                "Tickets": tickets,
                "Total Price": total_price,
                "Payment Method": payment_method,
                "Booking Time": datetime.now()
            }

            st.session_state.bookings.append(booking_data)

            st.success("🎉 Booking Confirmed!")
            st.balloons()


# =====================================================
# ADMIN DASHBOARD
# =====================================================
if menu == "📊 Admin Dashboard":

    st.title("📊 Admin Dashboard")

    if len(st.session_state.bookings) == 0:
        st.warning("No bookings yet!")
    else:
        df = pd.DataFrame(st.session_state.bookings)

        st.subheader("📋 All Bookings")
        st.dataframe(df)

        st.subheader("📈 Total Revenue")
        total_revenue = df["Total Price"].sum()
        st.success(f"₹ {total_revenue}")

        st.subheader("🎬 Movie-wise Bookings")
        movie_counts = df["Movie"].value_counts()
        st.bar_chart(movie_counts)

        if st.button("Reset All Bookings"):
            st.session_state.bookings = []
            st.success("All bookings cleared!")

 



