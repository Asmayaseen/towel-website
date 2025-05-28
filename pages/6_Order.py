import streamlit as st
from firebase.orders import save_order_to_firebase

st.title("📦 Place Your Order")

name = st.text_input("Name")
phone = st.text_input("Phone")
address = st.text_area("Address")

if "cart" not in st.session_state:
    st.session_state.cart = []

if st.button("Submit Order"):
    if name and phone and address:
        order_data = {
            "name": name,
            "phone": phone,
            "address": address,
            "cart": st.session_state.cart
        }
        save_order_to_firebase(order_data)
        st.success("🎉 Order Placed Successfully!")
    else:
        st.error("Please fill in all fields.")
