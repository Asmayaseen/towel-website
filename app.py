import streamlit as st
from firebase.firebase_init import db
from firebase_admin import firestore
from components import header, footer
import uuid
from datetime import datetime

# Page config
st.set_page_config(page_title="🛍️ Towel Shop", layout="wide", page_icon="🛒")

# Show header
header.show()

# Sidebar navigation
page = st.sidebar.selectbox("✨ Navigate to", ["🛒 Order Form", "📊 Admin Dashboard"])

# Initialize session state
if "cart" not in st.session_state:
    st.session_state.cart = []

if page == "🛒 Order Form":
    st.title("🛍️ Towel Order Form")
    st.markdown("---")

    # Product selection
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
        {"name": "🌈 Fancy Design", "price": 450, "img": "assets/fancy design.jpg"},
        {"name": "🧸 High Quality Bathrobe", "price": 600, "img": "assets/highquality bathrob.jpg"},
        {"name": "🛁 Soft Towels", "price": 750, "img": "assets/soft-towel.jpg"},
    ]
    
    st.subheader("🏷️ Add Items to Cart")
    cols = st.columns(3)
    for i, product in enumerate(products):
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"**{product['name']}**")
                st.markdown(f"💰 Price: Rs. {product['price']}")
                quantity = st.number_input("Quantity", min_value=1, value=1, key=f"qty_{i}")
                if st.button(f"➕ Add to Cart", key=f"add_{i}"):
                    st.session_state.cart.append({
                        "item": product["name"],
                        "qty": quantity,
                        "price": product["price"]
                    })
                    st.success("✅ Item added to cart!")
                    st.rerun()

    # Cart display
    if st.session_state.cart:
        st.subheader("🛒 Your Shopping Cart")
        st.markdown("---")
        total = 0
        for i, product in enumerate(st.session_state.cart):
            cols = st.columns([4, 2, 2, 1])
            with cols[0]:
                st.markdown(f"**{product['item']}**")
            with cols[1]:
                st.markdown(f"Price: Rs. {product['price']}")
            with cols[2]:
                st.markdown(f"Qty: {product['qty']}")
            with cols[3]:
                if st.button("🗑️", key=f"remove_{i}"):
                    st.session_state.cart.pop(i)
                    st.rerun()
            total += product["price"] * product["qty"]
            st.markdown("---")
        st.markdown(f"### 🧾 Total Amount: Rs. {total}")
        
        # Order form
        st.subheader("📦 Shipping Details")
        with st.form("order_form", border=True):
            name = st.text_input("👤 Your Name")
            phone = st.text_input("📱 Phone Number (10 digits)", max_chars=10)
            address = st.text_area("🏠 Delivery Address")

            submitted = st.form_submit_button("🚀 Place Order")
            
            if submitted:
                if not all([name, phone, address]):
                    st.error("❌ Please fill all fields")
                elif not phone.isdigit() or len(phone) != 10:
                    st.error("❌ Please enter a valid 10-digit phone number")
                else:
                    try:
                        order_id = str(uuid.uuid4())[:8]
                        order_data = {
                            "order_id": order_id,
                            "name": name,
                            "phone": phone,
                            "address": address,
                            "cart": st.session_state.cart,
                            "total": total,
                            "status": "pending",
                            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
                        db.collection("orders").document(order_id).set(order_data)
                        st.session_state.cart = []
                        st.balloons()
                        st.success(f"🎉 Order placed successfully! Your Order ID is **{order_id}**")
                    except Exception as e:
                        st.error(f"❌ Error placing order: {str(e)}")
    else:
        st.info("🛒 Your cart is empty. Add some products!")

elif page == "📊 Admin Dashboard":
    st.title("📊 Admin Dashboard")
    st.markdown("---")
    
    try:
        # Get sorted orders (newest first)
        orders_ref = db.collection("orders").order_by("timestamp", direction=firestore.Query.DESCENDING)
        docs = orders_ref.stream()
        
        orders = []
        for doc in docs:
            order_data = doc.to_dict()
            order_data["doc_id"] = doc.id  # Add document ID
            orders.append(order_data)
        
        if orders:
            for order in orders:
                order_id = order.get("order_id", order.get("doc_id", "N/A"))
                status = order.get("status", "pending").upper()
                
                with st.expander(f"📦 Order #{order_id} - {status}", expanded=False):
                    cols = st.columns(2)
                    with cols[0]:
                        st.markdown(f"**📅 Date:** {order.get('timestamp', 'N/A')}")
                        st.markdown(f"**👤 Customer:** {order.get('name', 'N/A')}")
                    with cols[1]:
                        st.markdown(f"**📱 Phone:** {order.get('phone', 'N/A')}")
                        st.markdown(f"**💰 Total:** Rs. {order.get('total', 0)}")
                    
                    st.markdown("**🏠 Address:**")
                    st.info(order.get("address", "N/A"))
                    
                    st.markdown("**🛒 Items:**")
                    for item in order.get("cart", []):
                        st.markdown(f"- {item.get('qty', 0)} ✕ {item.get('item', 'Unknown')} @ Rs. {item.get('price', 0)}")
                    
                    # Status update
                    st.markdown("---")
                    current_status = order.get("status", "pending")
                    new_status = st.selectbox(
                        "🔄 Update Status",
                        ["pending", "processing", "shipped", "delivered", "cancelled"],
                        index=["pending", "processing", "shipped", "delivered", "cancelled"].index(current_status),
                        key=f"status_{order_id}"
                    )
                    
                    if st.button("💾 Save Status", key=f"update_{order_id}"):
                        try:
                            db.collection("orders").document(order["doc_id"]).update({
                                "status": new_status,
                                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            })
                            st.success("✅ Status updated successfully!")
                            st.rerun()
                        except Exception as e:
                            st.error(f"❌ Failed to update status: {str(e)}")
        else:
            st.info("📭 No orders found in the database")
            
    except Exception as e:
        st.error(f"❌ Error loading orders: {str(e)}")

# Show footer
footer.show()