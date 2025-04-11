from crypto_utils import generate_key, save_key, load_key, encrypt_password
import os

MASTER_FILE = "master.key"

def set_master_password():
    if os.path.exists(MASTER_FILE):
        print("⚠️ Master password already set.")
        return

    password = input("🔐 Create a master password: ").strip()
    key = load_key()
    encrypted_pw = encrypt_password(password.encode(), key)

    with open(MASTER_FILE, "wb") as f:
        f.write(encrypted_pw)

    print("✅ Master password set and encrypted!")

if __name__ == "__main__":
    set_master_password()
