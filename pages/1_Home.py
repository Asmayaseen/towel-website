import streamlit as st

# Initialize session state key
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ---------------- HOME PAGE ----------------
if st.session_state.page == "Home":
    st.markdown(
        """
        <style>
        .banner {
            background-color: #D0F0C0;
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            margin-bottom: 25px;
        }
        .banner h1 {
            font-size: 3em;
            color: #2E8B57;
            font-family: 'Comic Sans MS', cursive;
        }
        .banner p {
            font-size: 1.3em;
            color: #444;
        }
        .item-card {
            background-color: #f1f1f1;
            color: #333;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0px 4px 6px rgba(0,0,0,0.05);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class='banner'>
        <h1>🛁 Towel Paradise</h1>
        <p>Wrap Yourself in Softness – Premium Towels Delivered to Your Doorstep!</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("assets/soft-towel.jpg", caption="Luxury Bath Towel Set 🤍", use_container_width=True)
        st.markdown("<div class='item-card'><strong>Rs. 850</strong></div>", unsafe_allow_html=True)

    with col2:
        st.image("assets/color-towels.jpg", caption="Colorful Hand Towels 🌈", use_container_width=True)
        st.markdown("<div class='item-card'><strong>Rs. 450</strong></div>", unsafe_allow_html=True)

    with col3:
        st.image("assets/kids-towel.jpg", caption="Cartoon Kids Towels 🧸", use_container_width=True)
        st.markdown("<div class='item-card'><strong>Rs. 600</strong></div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### ✨ Limited Time Offer: Flat 10% off on all orders!")

    if st.button("🛍️ Shop Towels Now"):
        st.session_state.page = "Products"
        st.rerun()
