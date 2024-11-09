# backend.py
import pickle

# Function to save user credentials in a binary file
def save_credentials(user_id, password):
    with open("id_and_password_records.dat", "ab") as file:
        pickle.dump({user_id: password}, file)

# Function to check login credentials
def check_credentials(user_id, password):
    try:
        with open("id_and_password_records.dat", "rb") as file:
            while True:
                try:
                    data = pickle.load(file)
                    if user_id in data and data[user_id] == password:
                        return True
                except EOFError:
                    break
    except FileNotFoundError:
        return False
    return False
