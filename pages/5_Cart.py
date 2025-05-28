import streamlit as st
from components import header, footer

st.set_page_config(page_title="Your Cart", layout="wide")
header.show()

st.title("🛒 Your Cart")

if "cart" not in st.session_state or not st.session_state.cart:
    st.info("🧺 Your cart is currently empty. Add items from the menu.")
else:
    total = 0
    st.markdown("---")
    for idx, item in enumerate(st.session_state.cart):
        subtotal = item["qty"] * item["price"]
        total += subtotal
        st.markdown(f"### {item['item']}")
        st.write(f"🔢 Quantity: {item['qty']}  |  💰 Rs. {item['price']} each  |  📦 Subtotal: Rs. {subtotal}")

        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("➖ Remove One", key=f"remove_{idx}"):
                if item["qty"] > 1:
                    item["qty"] -= 1
                else:
                    st.session_state.cart.pop(idx)
                st.experimental_rerun()
        with col2:
            if st.button("❌ Remove All", key=f"delete_{idx}"):
                st.session_state.cart.pop(idx)
                st.experimental_rerun()
        st.markdown("---")

    st.subheader(f"🧾 Total Amount: Rs. {total}")
    if st.button("✅ Proceed to Checkout"):
        st.success("Redirecting to order page... (simulate)")

footer.show()
