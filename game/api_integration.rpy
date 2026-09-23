# 1. Initialize the Python environment and import Josh's script
init python:
    import sys
    import os
    
    # Add the api_core folder to Ren'Py's system path so it can find the file
    api_path = os.path.join(renpy.config.gamedir, "api_core")
    if api_path not in sys.path:
        sys.path.append(api_path)
        
    import sheetdb_client

# 2. Update the Day 1 minigame label to fire the API call
label day1_newspaper_minigame:
    scene bg newsroom
    "Time to review my Reporter's Notepad and write the evening edition."
    
    # Pass your Ren'Py variables directly into Josh's Python function
    python:
        article_result = sheetdb_client.fetch_newspaper_article(day1_clue, day1_item, day1_witness)
        
        # Extract the returned JSON data into Ren'Py variables for display
        daily_headline = article_result.get("headline", "Error: Story Not Found")
        daily_body = article_result.get("body", "Error: Check database connection.")
        
    # Display the dynamic API result to the player
    "THE DAILY HERALD"
    "Headline: [daily_headline]"
    "[daily_body]"
    
    # Seamlessly transition to the next day
    jump day2_start