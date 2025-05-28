from firebase.firebase_init import db
from google.cloud.firestore_v1.base_document import DocumentSnapshot
from datetime import datetime
from typing import List, Dict, Optional

# Constants for order status
ORDER_STATUSES = {
    "PENDING": "pending",
    "PROCESSING": "processing",
    "SHIPPED": "shipped",
    "DELIVERED": "delivered",
    "CANCELLED": "cancelled"
}

def get_all_orders(sort_by: str = "timestamp", descending: bool = True) -> List[Dict]:
    """Get all orders with optional sorting"""
    try:
        orders_ref = db.collection('orders')
        if sort_by:
            direction = firestore.Query.DESCENDING if descending else firestore.Query.ASCENDING
            orders_ref = orders_ref.order_by(sort_by, direction=direction)
            
        docs = orders_ref.stream()
        return [{**doc.to_dict(), "id": doc.id} for doc in docs]
    except Exception as e:
        print(f"Error fetching orders: {str(e)}")
        return []

def save_order_to_firebase(order_data: Dict) -> Optional[str]:
    """Save new order and return document ID"""
    try:
        if not order_data.get("timestamp"):
            order_data['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        if not order_data.get("status"):
            order_data['status'] = ORDER_STATUSES["PENDING"]
            
        _, doc_ref = db.collection('orders').add(order_data)
        print(f"Order saved successfully! ID: {doc_ref.id}")
        return doc_ref.id
    except Exception as e:
        print(f"Error saving order: {str(e)}")
        return None

def get_order_by_id(order_id: str) -> Optional[Dict]:
    """Get single order by document ID"""
    try:
        doc = db.collection('orders').document(order_id).get()
        return doc.to_dict() if doc.exists else None
    except Exception as e:
        print(f"Error fetching order {order_id}: {str(e)}")
        return None

def update_order_status(order_id: str, new_status: str) -> bool:
    """Update order status with validation"""
    try:
        if new_status not in ORDER_STATUSES.values():
            print(f"Invalid status: {new_status}")
            return False
            
        db.collection('orders').document(order_id).update({
            "status": new_status,
            "last_updated": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        print(f"Order {order_id} status updated to {new_status}")
        return True
    except Exception as e:
        print(f"Error updating order {order_id}: {str(e)}")
        return False

def delete_order(order_id: str) -> bool:
    """Delete an order by ID"""
    try:
        db.collection('orders').document(order_id).delete()
        print(f"Order {order_id} deleted successfully")
        return True
    except Exception as e:
        print(f"Error deleting order {order_id}: {str(e)}")
        return False