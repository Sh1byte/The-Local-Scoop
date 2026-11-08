import requests
import json
import os

def fetch_newspaper_article(clue, item, witness, day="day1"):
    api_url = f"https://sheetdb.io/api/v1/czxhec0kt3a7k?sheet={day}"
    backup_file = os.path.join(os.path.dirname(__file__), f"offline_backup_{day}.json")
    data = None

    try:
        response = requests.get(api_url, timeout=3)
        if response.status_code == 200:
            fetched_data = response.json()
            if isinstance(fetched_data, list):
                data = fetched_data
                with open(backup_file, "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=4)
    except (requests.exceptions.RequestException, ValueError):
        pass

    if data is None:
        if os.path.exists(backup_file):
            with open(backup_file, "r", encoding="utf-8") as file:
                data = json.load(file)
        else:
            return {"headline": "Network Error", "body": "Could not reach the printing press."}

    target_clue = str(clue).strip().lower()
    target_item = str(item).strip().lower()
    target_witness = str(witness).strip().lower()
    blueprint_aliases = {"missing blueprint", "the janitor's keyring"}

    for row in data:
        if not isinstance(row, dict):
            continue
        row_clue = str(row.get("Interactable_Object", "")).strip().lower()
        row_item = str(row.get("Obtainable_Item", "")).strip().lower()
        row_witness = str(row.get("Witness", "")).strip().lower()

        clue_match = (row_clue == target_clue)
        item_match = (
            True if (target_item in blueprint_aliases and row_item in blueprint_aliases)
            else (row_item == target_item)
        )
        witness_match = (row_witness == target_witness or f"({target_witness})" in row_witness)

        if clue_match and item_match and witness_match:
            return {
                "headline": row.get("Headline", "Error: Headline Missing"),
                "body": row.get("Body", "Error: Body Missing")
            }

    return {"headline": "Editor's Note", "body": "The facts don't align. Story pulled."}