import streamlit as st
from components import header, footer

# Page Configuration
st.set_page_config(page_title="About Us", layout="wide")

# Show Header
header.show()

# Custom CSS for styling
st.markdown("""
<style>

.about-title {
    font-size: 3em;
    font-weight: 700;
    color: #2E8B57;
    margin-bottom: 30px;
    font-family: 'Segoe UI', sans-serif;
    text-align: center;
    text-shadow: 1px 1px 2px #ccc;
    background: linear-gradient(to bottom right, #f0fff0, #e0ffe0);
    padding: 40px;
    border-radius: 20px;
    margin-top: 30px;
    box-shadow: 0px 6px 18px rgba(0, 0, 0, 0.05);
}
.about-text {
    font-size: 1.2em;
    color: #333;
    line-height: 1.8;
    font-family: 'Segoe UI', sans-serif;
    padding-right: 15px;
}
</style>
""", unsafe_allow_html=True)

# Main About Us Container
st.markdown("<div class='about-container'>", unsafe_allow_html=True)

# About Us Title inside container
st.markdown("<div class='about-title'>About Us 🧼</div>", unsafe_allow_html=True)

# Columns layout
col1, col2 = st.columns([1.3, 1])

with col1:
    st.markdown("""
    <div class='about-text'>
    👨‍👩‍👧‍👦 We are a <strong>family-run business</strong> passionately crafting premium towels and bath essentials.<br><br>
    ✨ Our mission is to blend <strong>comfort, quality, and affordability</strong> in every thread — so you feel <i>pampered</i> every day.<br><br>
    🌍 Based in Pakistan 🇵🇰, we proudly serve both <strong>local & international</strong> markets — bringing <i>softness</i> to every home 🏡.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image("assets/about-us.jpg", caption="🧺 Our Premium Towel Collection", use_container_width=True)

# Close container div
st.markdown("</div>", unsafe_allow_html=True)

# Show Footer
footer.show()
