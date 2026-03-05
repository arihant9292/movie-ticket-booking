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


# --------------------------
# Sidebar Navigation
# --------------------------
menu = st.sidebar.radio("Navigation", ["🎟 Book Ticket", "📊 Admin Dashboard"])

# =====================================================
# BOOK TICKET PAGE
# =====================================================
if menu == "🎟 Book Ticket":

    st.title("🎬 Movie Ticket Booking System")

    col1, col2 = st.columns(2)

    with col1:
        movie = st.selectbox("Select Movie", ["Pushpa 2", "Animal", "Jawan", "RRR", "Conjuring", "Nun2"])
        date = st.date_input("Select Date")
        time = st.selectbox("Select Show Time", 
                            ["10:00 AM", "2:00 PM", "6:00 PM", "9:00 PM"])
        name = st.text_input("Your Name")

    with col2:
        tickets = st.number_input("Number of Tickets", 1, 5)
        price_per_ticket = 200
        total_price = tickets * price_per_ticket
        st.info(f"Total Price: ₹{total_price}")

    # --------------------------
    # Seat Layout
    # --------------------------
    st.subheader("🪑 Select Your Seats")

    selected_seats = []

    for row in ["A", "B", "C", "D", "E"]:
        cols = st.columns(8)
        for i, col in enumerate(cols):
            seat_id = f"{row}{i+1}"
            if st.session_state.seats[seat_id]:
                col.button(seat_id, disabled=True)
            else:
                if col.button(seat_id):
                    selected_seats.append(seat_id)

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

