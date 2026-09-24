import requests

def fetch_newspaper_article(clue, item, witness, day="day1"):
    # Replace this with your actual SheetDB API URL from sheetdb.io
    base_api_url = "https://sheetdb.io/api/v1/czxhec0kt3a7k"
    
    # Appends the sheet tab parameter (e.g., ?sheet=day1, ?sheet=day2)
    api_url = f"{base_api_url}?sheet={day}"

    try:
        response = requests.get(api_url, timeout=5)
        data = response.json()

        # Loop through the spreadsheet rows to find the exact match
        for row in data:
            if (row.get('Interactable_Object') == clue and 
                row.get('Obtainable_Item') == item and 
                row.get('Witness') == witness):
                return {
                    "headline": row.get('Headline'),
                    "body": row.get('Body')
                }

        return {"headline": "Editor's Note", "body": "The facts don't align. Story pulled."}

    except requests.exceptions.RequestException as e:
        return {"headline": "Network Error", "body": "Could not reach the printing press."}