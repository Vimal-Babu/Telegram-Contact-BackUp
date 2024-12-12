# Telegram Contacts Backup

A Python script to fetch Telegram contacts and save them to a CSV file.

## Features
- Uses the Telethon library to interact with Telegram.
- Fetches contacts and their details (name and phone number).
- Saves contact details into a CSV file (`telegram_contacts.csv`).

## Prerequisites
- Python 3.6 or higher.
- A Telegram API ID and Hash. [Get yours here](https://my.telegram.org/).

## Setup and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/telegram-contacts-backup.git
   cd telegram-contacts-backup

2. Create a virtual environment and activate it:
(for linux)
    python3 -m venv telegram_env
    source telegram_env/bin/activate

3. pip install -r requirements.txt

4. Add your API credentials to a .env file: 
       Create  a .env file in the root directory and add:

        API_ID=your_api_id
        API_HASH=your_api_hash
        PHONE_NUMBER=your_phone_number

5. Run the script:

    python MyTelegramScripts.py

Folder Structure
    telegram-contacts-backup/
├── telegram_env/             # Virtual environment (not pushed to Git)
├── MyTelegramScripts.py      # Main script
├── requirements.txt          # Dependencies
├── telegram_contacts.csv     # Output file
├── .env                      # API credentials (excluded from Git)
└── README.md                 # Project documentation

