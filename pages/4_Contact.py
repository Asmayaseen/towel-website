import streamlit as st
from components import header, footer

st.set_page_config(page_title="Contact Us", layout="wide")
header.show()

# --- Custom CSS for Styling ---
st.markdown("""
<style>

.contact-title {
    font-size: 2.5em;
    font-weight: bold;
    color: #8B4513;
    margin-bottom: 15px;
    background: linear-gradient(to right, #fdfcfb, #e2d1c3);
    padding: 40px;
    border-radius: 20px;
    margin-top: 30px;
    box-shadow: 0px 6px 18px rgba(0, 0, 0, 0.05);
    font-family: 'Segoe UI', sans-serif;
}
.contact-description {
    font-size: 1.2em;
    color: #5c4033;
    margin-bottom: 30px;
}
input, textarea {
    font-size: 1.1em !important;
}
.stButton > button {
    background-color: #8B4513;
    color: white;
    border-radius: 25px;
    padding: 10px 25px;
    font-weight: 600;
    font-size: 1.1em;
    transition: background-color 0.3s ease;
}
.stButton > button:hover {
    background-color: #5c4033;
}
</style>
""", unsafe_allow_html=True)

# --- Layout ---
st.markdown("<div class='contact-container'>", unsafe_allow_html=True)
st.markdown("<div class='contact-title'>📞 Contact Us</div>", unsafe_allow_html=True)
st.markdown("<div class='contact-description'>Feel free to reach out for bulk orders, custom designs, or general inquiries. We're happy to help! 🧺💬</div>", unsafe_allow_html=True)

with st.form("contact_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("👤 Your Name")
    with col2:
        email = st.text_input("📧 Email Address")

    message = st.text_area("💬 Your Message", height=150)

    submitted = st.form_submit_button("📨 Send Message")

    if submitted:
        if name and email and message:
            st.success("✅ Thank you! Your message has been sent successfully.")
        else:
            st.error("❗ Please fill in all fields before submitting.")

st.markdown("</div>", unsafe_allow_html=True)

footer.show()
