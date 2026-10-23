import requests
import json
import os

def fetch_newspaper_article(clue, item, witness, day="day1"):
    base_api_url = "https://sheetdb.io/api/v1/czxhec0kt3a7k"
    api_url = f"{base_api_url}?sheet={day}"
    
    # Ensures the backup file saves in the exact same folder as this script
    backup_file = os.path.join(os.path.dirname(__file__), f"offline_backup_{day}.json")
    data = None

    try:
        # 1. Try to fetch the live data from SheetDB
        response = requests.get(api_url, timeout=3)
        if response.status_code == 200:
            fetched_data = response.json()
            if isinstance(fetched_data, list):
                data = fetched_data
                # 2. If successful and valid list, silently update the local backup file
                with open(backup_file, "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=4)
    except (requests.exceptions.RequestException, ValueError):
        pass

    # 3. NO INTERNET or API error: Fall back to local backup
    if data is None:
        if os.path.exists(backup_file):
            with open(backup_file, "r", encoding="utf-8") as file:
                data = json.load(file)
        else:
            # 4. No internet AND no backup exists yet
            return {"headline": "Network Error", "body": "Could not reach the printing press."}

    # Normalize inputs to prevent case/spacing mismatches
    target_clue = str(clue).strip().lower()
    target_item = str(item).strip().lower()
    target_witness = str(witness).strip().lower()

    # Handle Day 1 item alias ("Missing blueprint" <-> "The Janitor's Keyring")
    blueprint_aliases = {"missing blueprint", "the janitor's keyring"}

    # Loop through the data (whether live or offline) to find the match
    for row in data:
        if not isinstance(row, dict):
            continue

        row_clue = str(row.get('Interactable_Object', '')).strip().lower()
        row_item = str(row.get('Obtainable_Item', '')).strip().lower()
        row_witness = str(row.get('Witness', '')).strip().lower()

        clue_match = (row_clue == target_clue)

        if target_item in blueprint_aliases and row_item in blueprint_aliases:
            item_match = True
        else:
            item_match = (row_item == target_item)

        # Matches exact witness ("vendor 1") OR prefixed witness ("key witness (vendor 1)")
        witness_match = (
            row_witness == target_witness or
            f"({target_witness})" in row_witness
        )

        if clue_match and item_match and witness_match:
            return {
                "headline": row.get('Headline', 'Error: Headline Missing'),
                "body": row.get('Body', 'Error: Body Missing')
            }

    return {"headline": "Editor's Note", "body": "The facts don't align. Story pulled."}

def prefetch_all_backups():
    days = ["day1", "day2", "day3", "day5"]
    base_api_url = "https://sheetdb.io/api/v1/czxhec0kt3a7k"
    
    for day in days:
        api_url = f"{base_api_url}?sheet={day}"
        backup_file = os.path.join(os.path.dirname(__file__), f"offline_backup_{day}.json")
        
        try:
            response = requests.get(api_url, timeout=3)
            if response.status_code == 200:
                fetched_data = response.json()
                if isinstance(fetched_data, list):
                    with open(backup_file, "w", encoding="utf-8") as file:
                        json.dump(fetched_data, file, indent=4)
        except (requests.exceptions.RequestException, ValueError):
            pass