from telethon.sync import TelegramClient
from dotenv import load_dotenv
import csv,os
load_dotenv()

# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your actual API ID and hash
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE_NUMBER') # Enter your phone number (with country code)

# Initialize the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

# Start the client and log in
client.start(phone_number)

# Fetch dialogs (which include contacts) and save them to a CSV file
with client:
    #contacts = client.get_dialogs()get_contacts()
    
    dialogs = client.get_dialogs() 
    
    

    # Open a CSV file to save contacts
    with open("telegram_contacts.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone Number"])

        # Write each contact's details to the CSV
        for dialog in dialogs:
            if dialog.is_user:
                contact = dialog.entity
                name = f"{contact.first_name or ''} {contact.last_name or ''}".strip()
                phone = contact.phone or "Not available"
                writer.writerow([name, phone])    

print("Contacts have been saved to telegram_contacts.csv.")
