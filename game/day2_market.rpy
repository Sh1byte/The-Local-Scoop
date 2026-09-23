define vendor = Character("Vendor", color="#cccccc")
define shopper = Character("Shopper", color="#cccccc")
define baker = Character("Baker", color="#cccccc")
define musician = Character("Street Musician", color="#cccccc")

default day2_clue = ""
default day2_item = ""
default day2_witness = ""
default evidence_letter = False

default day2_clues_found = []
default day2_items_found = []
default day2_witnesses_found = []
default day2_clicked_points = []

label day2_start:
    scene bg newsroom
    vance "Market plaza. Fruit stand burned to the ground in broad daylight. Go."
    scene bg market_plaza
    arthur "Go back to the office, rookie."
    jump day2_investigation_hub

label day2_investigation_hub:
    call screen day2_market_investigation
    $ clicked_object = _return
    $ day2_clicked_points.append(clicked_object)
    
    if clicked_object == "gascan":
        "It reeks of accelerant."
        $ day2_clues_found.append("The Scorched Gas Can")
        jump day2_investigation_hub
    elif clicked_object == "toycar":
        "Sad collateral damage."
        $ day2_clues_found.append("The Melted Toy Car")
        jump day2_investigation_hub
    elif clicked_object == "oil":
        "A greasy puddle near a stove."
        $ day2_clues_found.append("The Spilled Cooking Oil")
        jump day2_investigation_hub
        
    elif clicked_object == "camera":
        "I spot a damaged security camera in the debris."
        $ day2_items_found.append("The Melted Camera")
        $ inventory_bag_items.append("The Melted Camera")
        jump day2_investigation_hub
    elif clicked_object == "cigar":
        "A half-smoked, imported cigar was dropped nearby."
        $ day2_items_found.append("The Expensive Cigar")
        $ inventory_bag_items.append("The Expensive Cigar")
        jump day2_investigation_hub
    elif clicked_object == "lottery":
        "It's a winning scratch ticket."
        $ day2_items_found.append("The Dropped Lottery Ticket")
        $ inventory_bag_items.append("The Dropped Lottery Ticket")
        jump day2_investigation_hub
        
    elif clicked_object == "letter":
        "An extortion letter signed with the blue anchor stamp of The River Boys."
        $ evidence_letter = True 
        jump day2_investigation_hub
        
    elif clicked_object == "vendor":
        vendor "I stopped paying protection money... and they burned my shop!"
        $ day2_witnesses_found.append("Vendor 1")
        jump day2_investigation_hub
    elif clicked_object == "shopper":
        shopper "She caused the fire herself for insurance money!"
        $ day2_witnesses_found.append("Shopper 1")
        jump day2_investigation_hub
    elif clicked_object == "baker":
        baker "It was a targeted hit by rival bakers!"
        $ day2_witnesses_found.append("Baker 1")
        jump day2_investigation_hub
    elif clicked_object == "musician":
        musician "I saw a freak lightning strike from a clear sky!"
        $ day2_witnesses_found.append("Street Musician 1")
        jump day2_investigation_hub
        
    elif clicked_object == "newsroom":
        jump day2_newspaper_minigame

label day2_newspaper_minigame:
    scene bg newsroom
    "Time to review my Reporter's Notepad and write the market edition."

label select_day2_clue:
    "What was the most credible information I gathered at the market?"
    menu:
        "The Scorched Gas Can" if "The Scorched Gas Can" in day2_clues_found:
            "Description: Proves the fire was started intentionally with gasoline."
            menu:
                "Confirm this choice":
                    $ day2_clue = "The Scorched Gas Can"
                "Pick something else":
                    jump select_day2_clue
        "The Melted Toy Car" if "The Melted Toy Car" in day2_clues_found:
            "Description: Suggests a child might have been playing with matches."
            menu:
                "Confirm this choice":
                    $ day2_clue = "The Melted Toy Car"
                "Pick something else":
                    jump select_day2_clue
        "The Spilled Cooking Oil" if "The Spilled Cooking Oil" in day2_clues_found:
            "Description: Looks like a simple kitchen grease fire accident."
            menu:
                "Confirm this choice":
                    $ day2_clue = "The Spilled Cooking Oil"
                "Pick something else":
                    jump select_day2_clue

label select_day2_item:
    "What was the most credible object I gathered at the market?"
    menu:
        "The Melted Camera" if "The Melted Camera" in day2_items_found:
            "Description: Provides a blurry photo of the fire starting."
            menu:
                "Confirm this choice":
                    $ day2_item = "The Melted Camera"
                "Pick something else":
                    jump select_day2_item
        "The Expensive Cigar" if "The Expensive Cigar" in day2_items_found:
            "Description: Might trick people into blaming a wealthy politician."
            menu:
                "Confirm this choice":
                    $ day2_item = "The Expensive Cigar"
                "Pick something else":
                    jump select_day2_item
        "The Dropped Lottery Ticket" if "The Dropped Lottery Ticket" in day2_items_found:
            "Description: Misleads into a story about a lucky vendor getting robbed."
            menu:
                "Confirm this choice":
                    $ day2_item = "The Dropped Lottery Ticket"
                "Pick something else":
                    jump select_day2_item

label select_day2_witness:
    "Who had the most convincing story at the market?"
    menu:
        "Vendor" if "Vendor 1" in day2_witnesses_found:
            "Testimony: Stopped paying protection money; shop was burned in revenge."
            menu:
                "Confirm this choice":
                    $ day2_witness = "Vendor 1"
                "Pick something else":
                    jump select_day2_witness
        "Shopper" if "Shopper 1" in day2_witnesses_found:
            "Testimony: Claims the owner burned her own shop for insurance money."
            menu:
                "Confirm this choice":
                    $ day2_witness = "Shopper 1"
                "Pick something else":
                    jump select_day2_witness
        "Baker" if "Baker 1" in day2_witnesses_found:
            "Testimony: Blames a ruthless secret society of rival bakers."
            menu:
                "Confirm this choice":
                    $ day2_witness = "Baker 1"
                "Pick something else":
                    jump select_day2_witness
        "Street Musician" if "Street Musician 1" in day2_witnesses_found:
            "Testimony: Saw a freak lightning strike from a clear sky."
            menu:
                "Confirm this choice":
                    $ day2_witness = "Street Musician 1"
                "Pick something else":
                    jump select_day2_witness

label day2_api_execution:
    call calculate_day2_credibility
    python:
        article_result = sheetdb_client.fetch_newspaper_article(day2_clue, day2_item, day2_witness)
        daily_headline = article_result.get("headline", "Error: Story Not Found")
        daily_body = article_result.get("body", "Error: Check database connection.")
        
    "THE DAILY HERALD"
    "Headline: [daily_headline]"
    "[daily_body]"
    "Editor's Note: This article was rated as [daily_rating]!"
    "My total journalistic credibility is now [total_credibility_score]."
    jump day3_start