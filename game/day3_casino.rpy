define dealer = Character("Dealer", color="#cccccc")
define cleaner = Character("Cleaner", color="#cccccc")
define waitress = Character("Waitress", color="#cccccc")
define drunk = Character("Drunk Patron", color="#cccccc")

default day3_clue = ""
default day3_item = ""
default day3_witness = ""
default evidence_ledger = False

default day3_clues_found = []
default day3_items_found = []
default day3_witnesses_found = []
default day3_clicked_points = []

label day3_start:
    scene bg newsroom
    vance "Both of you, drop the gang story entirely!"
    scene bg casino_basement
    arthur "Look, this is getting deadly. We are a team now."
    jump day3_investigation_hub

label day3_investigation_hub:
    call screen day3_casino_investigation
    $ clicked_object = _return
    $ day3_clicked_points.append(clicked_object)
    
    if clicked_object == "bullethole":
        "Over fifty bullet holes scar the masonry."
        $ day3_clues_found.append("The Bullet-Riddled Wall")
        jump day3_investigation_hub
    elif clicked_object == "cards":
        "Decks of crooked playing cards littered everywhere."
        $ day3_clues_found.append("The Scattered Marked Cards")
        jump day3_investigation_hub
    elif clicked_object == "jukebox":
        "Broken glass and loose wiring."
        $ day3_clues_found.append("The Smashed Jukebox")
        jump day3_investigation_hub
        
    elif clicked_object == "vippass":
        "It's a VIP Pass to a local club."
        $ day3_items_found.append("The VIP Pass")
        $ inventory_bag_items.append("The VIP Pass")
        jump day3_investigation_hub
    elif clicked_object == "earring":
        "A fake diamond earring on the floor."
        $ day3_items_found.append("The Diamond Earring")
        $ inventory_bag_items.append("The Diamond Earring")
        jump day3_investigation_hub
    elif clicked_object == "creditcard":
        "A stolen plastic credit card."
        $ day3_items_found.append("The Stolen Credit Card")
        $ inventory_bag_items.append("The Stolen Credit Card")
        jump day3_investigation_hub
        
    elif clicked_object == "ledger":
        "A Bloody Ledger listing illegal weapon purchases."
        $ evidence_ledger = True 
        jump day3_investigation_hub
        
    elif clicked_object == "dealer":
        dealer "The Iron Syndicate raided us because this place is owned by The River Boys!"
        $ day3_witnesses_found.append("Dealer 1")
        jump day3_investigation_hub
    elif clicked_object == "cleaner":
        cleaner "The police raided the place in secret and took all the money!"
        $ day3_witnesses_found.append("Cleaner 1")
        jump day3_investigation_hub
    elif clicked_object == "waitress":
        waitress "An angry ghost haunts the basement!"
        $ day3_witnesses_found.append("Waitress 1")
        jump day3_investigation_hub
    elif clicked_object == "drunk":
        drunk "A rival casino owner drove a bulldozer into the wall!"
        $ day3_witnesses_found.append("Drunk Patron 1")
        jump day3_investigation_hub
        
    elif clicked_object == "newsroom":
        jump day3_newspaper_minigame

default backroom_items_found = []
default safe_unlocked = False

label backroom:
    scene bg backroom
    
    call screen backroom_environment
    $ clicked_object = _return

    if clicked_object == "safe":
        jump safe_close_up
    
    jump backroom

label safe_close_up:
    scene bg safe_close_up
    "I can see the safe on the shelf, along with a piece of paper."
    
    call screen safe_closeup_environment
    $ clicked_object = _return

    if clicked_object == "safe_interact":
        if safe_unlocked:
            jump opened_safe_view
        else:
            jump safe_minigame
    elif clicked_object == "clue_paper":
        "The paper reads: '3 - 1 - 3'"
        jump safe_close_up
    elif clicked_object == "back":
        # Jump back to your main investigation hub
        jump day3_investigation_hub 

label safe_minigame:
    $ safe_current_digit = 0
    $ safe_entered_code = ""

label safe_minigame_loop:
    # Use the exact file path for the background
    scene expression "gui/day3_casino/backroom/safe/safe.png"
    
    call screen safe_puzzle_screen(safe_current_digit, safe_entered_code)
    $ action = _return

    if action == "turn_right":
        $ safe_current_digit = (safe_current_digit - 1) % 10
        jump safe_minigame_loop
        
    elif action == "turn_left":
        $ safe_current_digit = (safe_current_digit + 1) % 10
        jump safe_minigame_loop
        
    elif action == "enter_digit":
        $ safe_entered_code += str(safe_current_digit)
        
        if len(safe_entered_code) == 3:
            if safe_entered_code == "313":
                $ safe_unlocked = True
                "Click. The heavy mechanism unlocks."
                jump opened_safe_view
            else:
                "Bzzt. Wrong combination. The dial resets."
                $ safe_entered_code = ""
                jump safe_minigame_loop
        jump safe_minigame_loop
        
    elif action == "exit":
        jump safe_close_up

label opened_safe_view:
    scene bg opened_safe
    
    call screen opened_safe_environment
    $ clicked_object = _return

    if clicked_object == "bloody_ledger":
        if "Bloody Ledger" not in backroom_items_found:
            $ backroom_items_found.append("Bloody Ledger")
            "I found the bloody ledger inside the safe."
            # Set the day 3 ledger evidence flag to True
            $ evidence_ledger = True 
        else:
            "The safe is empty now."
        jump opened_safe_view
        
    elif clicked_object == "back":
        jump safe_close_up

label day3_newspaper_minigame:
    scene bg newsroom
    "Time to review my Reporter's Notepad and write the casino edition."

label select_day3_clue:
    "What was the most credible information I gathered at the casino?"
    menu:
        "The Bullet-Riddled Wall" if "The Bullet-Riddled Wall" in day3_clues_found:
            "Description: Proves heavy military firepower was used in the attack."
            menu:
                "Confirm this choice":
                    $ day3_clue = "The Bullet-Riddled Wall"
                "Pick something else":
                    jump select_day3_clue
        "The Scattered Marked Cards" if "The Scattered Marked Cards" in day3_clues_found:
            "Description: Suggests a fight purely between cheating gamblers."
            menu:
                "Confirm this choice":
                    $ day3_clue = "The Scattered Marked Cards"
                "Pick something else":
                    jump select_day3_clue
        "The Smashed Jukebox" if "The Smashed Jukebox" in day3_clues_found:
            "Description: Makes the scene look like a routine drunken bar brawl."
            menu:
                "Confirm this choice":
                    $ day3_clue = "The Smashed Jukebox"
                "Pick something else":
                    jump select_day3_clue

label select_day3_item:
    "What was the most credible object I gathered at the casino?"
    menu:
        "The VIP Pass" if "The VIP Pass" in day3_items_found:
            "Description: Grants access to restricted areas to overhear crucial leads."
            menu:
                "Confirm this choice":
                    $ day3_item = "The VIP Pass"
                "Pick something else":
                    jump select_day3_item
        "The Diamond Earring" if "The Diamond Earring" in day3_items_found:
            "Description: Misleads into writing a story about a jewel heist."
            menu:
                "Confirm this choice":
                    $ day3_item = "The Diamond Earring"
                "Pick something else":
                    jump select_day3_item
        "The Stolen Credit Card" if "The Stolen Credit Card" in day3_items_found:
            "Description: Distracts with a boring local identity theft angle."
            menu:
                "Confirm this choice":
                    $ day3_item = "The Stolen Credit Card"
                "Pick something else":
                    jump select_day3_item

label select_day3_witness:
    "Who had the most convincing story at the casino?"
    menu:
        "Dealer" if "Dealer 1" in day3_witnesses_found:
            "Testimony: The Iron Syndicate raided the casino because it belongs to rival River Boys."
            menu:
                "Confirm this choice":
                    $ day3_witness = "Dealer 1"
                "Pick something else":
                    jump select_day3_witness
        "Cleaner" if "Cleaner 1" in day3_witnesses_found:
            "Testimony: Claims the police ran a secret raid and took all the cash."
            menu:
                "Confirm this choice":
                    $ day3_witness = "Cleaner 1"
                "Pick something else":
                    jump select_day3_witness
        "Waitress" if "Waitress 1" in day3_witnesses_found:
            "Testimony: Insists an angry ghost haunts the basement."
            menu:
                "Confirm this choice":
                    $ day3_witness = "Waitress 1"
                "Pick something else":
                    jump select_day3_witness
        "Drunk Patron" if "Drunk Patron 1" in day3_witnesses_found:
            "Testimony: A rival owner drove a bulldozer straight through the masonry."
            menu:
                "Confirm this choice":
                    $ day3_witness = "Drunk Patron 1"
                "Pick something else":
                    jump select_day3_witness

label day3_api_execution:
    call calculate_day3_credibility
    python:
        article_result = sheetdb_client.fetch_newspaper_article(day3_clue, day3_item, day3_witness, "day3")
        daily_headline = article_result.get("headline", "Error: Story Not Found")
        daily_body = article_result.get("body", "Error: Check database connection.")
        
    "THE DAILY HERALD"
    "Headline: [daily_headline]"
    "[daily_body]"
    "Editor's Note: This article was rated as [daily_rating]!"
    "My total journalistic credibility is now [total_credibility_score]."
    jump day4_start