import streamlit as st
import streamlit_authenticator as stauth

def login_system():
    names = ["Admin User"]
    usernames = ["admin"]
    passwords = ["admin123"]

    # Hash passwords
    hashed_passwords = stauth.Hasher(passwords).generate()

    config = {
        "credentials": {
            "usernames": {
                usernames[0]: {
                    "name": names[0],
                    "password": hashed_passwords[0]
                }
            }
        },
        "cookie": {
            "name": "toweladmincookie",
            "key": "random_key_xyz123",
            "expiry_days": 1
        },
        "preauthorized": {
            "emails": []
        }
    }

    authenticator = stauth.Authenticate(
        config["credentials"],
        cookie_name=config["cookie"]["name"],
        key=config["cookie"]["key"],
        cookie_expiry_days=config["cookie"]["expiry_days"],
    )

    name, auth_status, username = authenticator.login("Login", "main")
    return authenticator, name, auth_status, username