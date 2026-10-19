import requests
import json
import os

def fetch_newspaper_article(clue, item, witness, day="day1"):
    base_api_url = "https://sheetdb.io/api/v1/czxhec0kt3a7k"
    api_url = f"{base_api_url}?sheet={day}"
    
    # Ensures the backup file saves in the exact same folder as this script
    backup_file = os.path.join(os.path.dirname(__file__), f"offline_backup_{day}.json")

    try:
        # 1. Try to fetch the live data from SheetDB
        response = requests.get(api_url, timeout=3)
        data = response.json()

        # 2. If successful, silently update the local backup file
        with open(backup_file, "w") as file:
            json.dump(data, file, indent=4)

    except requests.exceptions.RequestException:
        # 3. NO INTERNET: Catch the error and look for a local backup
        if os.path.exists(backup_file):
            with open(backup_file, "r") as file:
                data = json.load(file)
        else:
            # 4. No internet AND no backup exists yet
            return {"headline": "Network Error", "body": "Could not reach the printing press."}

    # Normalize inputs to prevent case/spacing mismatches
    target_clue = str(clue).strip().lower()
    target_item = str(item).strip().lower()
    target_witness = str(witness).strip().lower()

    # Loop through the data (whether live or offline) to find the match
    for row in data:
        if (str(row.get('Interactable_Object', '')).strip().lower() == target_clue and 
            str(row.get('Obtainable_Item', '')).strip().lower() == target_item and 
            str(row.get('Witness', '')).strip().lower() == target_witness):
            return {
                "headline": row.get('Headline'),
                "body": row.get('Body')
            }

    # This belongs to the FIRST function, so it must stay here
    return {"headline": "Editor's Note", "body": "The facts don't align. Story pulled."}


def prefetch_all_backups():
    days = ["day1", "day2", "day3", "day4", "day5"]
    base_api_url = "https://sheetdb.io/api/v1/czxhec0kt3a7k"
    
    for day in days:
        api_url = f"{base_api_url}?sheet={day}"
        backup_file = os.path.join(os.path.dirname(__file__), f"offline_backup_{day}.json")
        
        try:
            # Silently fetch and cache the data for each day
            response = requests.get(api_url, timeout=3)
            with open(backup_file, "w") as file:
                json.dump(response.json(), file, indent=4)
        except requests.exceptions.RequestException:
            # If there's no internet when the game opens, it just ignores the error
            # and relies on whatever backups were already saved previously.
            pass