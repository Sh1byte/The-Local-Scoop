import requests

def fetch_newspaper_article(clue, item, witness, day="day1"):
    # Replace this with your actual SheetDB API URL from sheetdb.io
    base_api_url = "https://sheetdb.io/api/v1/czxhec0kt3a7k"
    
    # Appends the sheet tab parameter (e.g., ?sheet=day1, ?sheet=day2)
    api_url = f"{base_api_url}?sheet={day}"

    try:
        response = requests.get(api_url, timeout=5)
        data = response.json()

        # Normalize inputs (strip extra spaces and convert to lowercase)
        target_clue = str(clue).strip().lower()
        target_item = str(item).strip().lower()
        target_witness = str(witness).strip().lower()

        # Accept variations in naming or cached SheetDB values
        valid_items = {target_item}
        if target_item in ["missing blueprint", "the missing blueprint", "the janitor's keyring"]:
            valid_items.update(["missing blueprint", "the missing blueprint", "the janitor's keyring"])
        elif target_item in ["the melted camera", "blurry photograph", "blurry photograph of the fire starting"]:
            valid_items.update(["the melted camera", "blurry photograph", "blurry photograph of the fire starting"])

        # Loop through the spreadsheet rows to find the match
        for row in data:
            row_clue = str(row.get('Interactable_Object', '')).strip().lower()
            row_item = str(row.get('Obtainable_Item', '')).strip().lower()
            row_witness = str(row.get('Witness', '')).strip().lower()

            if (row_clue == target_clue and 
                row_item in valid_items and 
                row_witness == target_witness):
                return {
                    "headline": row.get('Headline'),
                    "body": row.get('Body')
                }

        return {"headline": "Editor's Note", "body": "The facts don't align. Story pulled."}

    except requests.exceptions.RequestException as e:
        return {"headline": "Network Error", "body": "Could not reach the printing press."}