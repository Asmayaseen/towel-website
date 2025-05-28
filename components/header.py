import streamlit as st

def show():
    st.markdown("""
    <style>
    .nav-header {
        background-color: #E0FFE0;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        font-family: 'Segoe UI', sans-serif;
    }

    .nav-header a {
        text-decoration: none;
        margin: 0 20px;
        font-size: 1.2em;
        color: #2E8B57;
        font-weight: 600;
        transition: color 0.3s;
    }

    .nav-header a:hover {
        color: #1E5631;
        text-decoration: underline;
    }
    </style>

    <div class='nav-header'>
        🏠 <a href="/">Home</a> |
        ℹ️ <a href="/About">About</a> |
        🧺 <a href="/Menu">Menu</a> |
        📞 <a href="/Contact">Contact</a> |
        🛒 <a href="/Cart">Cart</a> |
        📦 <a href="/Order">Order</a> |
        
    </div>
    """, unsafe_allow_html=True)
