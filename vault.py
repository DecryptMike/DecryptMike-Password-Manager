from crypto_utils import load_key, encrypt_password, decrypt_password
import os
import json

MASTER_FILE = "master.key"
VAULT_FILE = "vault.json"

def verify_master_password():
    if not os.path.exists(MASTER_FILE):
        print("❌ Master password file not found. Run master_password.py first.")
        exit()

    key = load_key()

    with open(MASTER_FILE, "rb") as f:
        encrypted_pw = f.read()

    user_input = input("🔐 Enter master password to unlock vault: ").strip()

    try:
        decrypted_pw = decrypt_password(encrypted_pw, key).decode()
        if user_input != decrypted_pw:
            print("❌ Incorrect master password. Access denied.")
            exit()
    except Exception:
        print("❌ Error verifying master password.")
        exit()

# Load encryption key
key = load_key()

# Load existing vault or initialize
if os.path.exists(VAULT_FILE):
    with open(VAULT_FILE, "r") as f:
        vault_data = json.load(f)
else:
    vault_data = {}

def save_vault():
    with open(VAULT_FILE, "w") as f:
        json.dump(vault_data, f, indent=2)

def add_entry():
    site = input("Enter site name: ").strip()
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    encrypted_pw = encrypt_password(password.encode(), key)
    vault_data[site] = {
        "username": username,
        "password": encrypted_pw.decode()  # Store encrypted as string
    }

    save_vault()
    print(f"✅ Entry added for {site}")

def view_entries():
    if not vault_data:
        print("🔐 Vault is empty.")
        return

    for site, creds in vault_data.items():
        decrypted_pw = decrypt_password(creds["password"].encode(), key).decode()
        print(f"\n🌐 {site}")
        print(f"👤 Username: {creds['username']}")
        print(f"🔑 Password: {decrypted_pw}")

def main():
    while True:
        print("\n🔐 Password Vault")
        print("1. Add new entry")
        print("2. View saved entries")
        print("3. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    verify_master_password()
    main()
