from firebase.firebase_init import db

def test_fetch_orders():
    try:
        orders_ref = db.collection('orders')
        docs = orders_ref.stream()
        for doc in docs:
            print(doc.id, doc.to_dict())
        print("Firebase connection successful!")
    except Exception as e:
        print("Firebase connection failed:", e)

test_fetch_orders()
