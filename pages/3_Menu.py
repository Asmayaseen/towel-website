import streamlit as st
from components import header, footer

st.set_page_config(page_title="Menu", layout="wide")
header.show()

# Initialize cart if not exists
if "cart" not in st.session_state:
    st.session_state.cart = []

# CSS Styling
st.markdown("""
<style>
.menu-container {
    background: linear-gradient(to right, #e0f7fa, #b2ebf2);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 8px 15px rgba(0,0,0,0.1);
    margin-top: 25px;
    font-family: 'Segoe UI', sans-serif;
}
.menu-title {
    text-align: center;
    font-size: 2.8em;
    color: #00796b;
    font-weight: 700;
    margin-bottom: 30px;
}
.product-card {
    background: white;
    border-radius: 15px;
    padding: 15px;
    text-align: center;
    box-shadow: 0 6px 10px rgba(0,0,0,0.07);
    transition: transform 0.2s ease;
}
.product-card:hover {
    transform: scale(1.05);
}
.product-name {
    font-size: 1.4em;
    font-weight: 600;
    color: #004d40;
    margin: 10px 0 5px 0;
}
.product-price {
    font-size: 1.2em;
    font-weight: 500;
    color: #00796b;
    margin-bottom: 15px;
}
.add-btn {
    background-color: #00796b;
    color: white;
    border: none;
    padding: 10px 18px;
    border-radius: 25px;
    cursor: pointer;
    font-weight: 600;
    transition: background-color 0.3s ease;
}
.add-btn:hover {
    background-color: #004d40;
}
</style>
""", unsafe_allow_html=True)

products = [
    {"name": "🤍 Bath Mate", "price": 500, "img": "assets/bath-mat.jpg"},
    {"name": "💙 Green Towel Set", "price": 600, "img": "assets/towel-sets-2.jpg"},
    {"name": "🧺 Luxury Cotton Towel", "price": 900, "img": "assets/towel-sets.jpg"},
    {"name": "🌈 Colorful Towels sets", "price": 450, "img": "assets/towelset-3.jpg"},
    {"name": "🧸 Cartoon Kids Towels", "price": 600, "img": "assets/towelset.jpg"},
    {"name": "🛁 Soft Bath Towels", "price": 750, "img": "assets/towel6.jpg"},
    {"name": "🤍 4PC Face Towel Sets", "price": 500, "img": "assets/4PCFaceTowelSets.jpg"},
    {"name": "💙 6PC Combed Towel Sets", "price": 600, "img": "assets/6PCcombedtowelsets.jpg"},
    {"name": "🧺 Bridal Towel Gift Sets", "price": 900, "img": "assets/BridalTowelGiftSets.jpg"},
    {"name": "🌈 fancy design", "price": 450, "img": "assets/fancy design.jpg"},
    {"name": "🧸 highquality bathrob", "price": 600, "img": "assets/highquality bathrob.jpg"},
    {"name": "🛁 Soft Towels", "price": 750, "img": "assets/soft-towel.jpg"},
]

st.markdown("<div class='menu-container'>", unsafe_allow_html=True)
st.markdown("<div class='menu-title'>🧺 Our Towel Collection</div>", unsafe_allow_html=True)

cols = st.columns(3)
for idx, product in enumerate(products):
    with cols[idx % 3]:
        st.markdown("<div class='product-card'>", unsafe_allow_html=True)
        st.image(product["img"], use_container_width=True)
        st.markdown(f"<div class='product-name'>{product['name']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='product-price'>Rs. {product['price']}</div>", unsafe_allow_html=True)
        if st.button(f"🛒 Add to Cart", key=f"add_{product['name']}"):
            # Check if product already in cart
            found = False
            for item in st.session_state.cart:
                if item['item'] == product['name']:
                    item['qty'] += 1
                    found = True
                    break
            if not found:
                st.session_state.cart.append({"item": product['name'], "price": product['price'], "qty": 1})
            st.success(f"{product['name']} added to cart!")
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
footer.show()
