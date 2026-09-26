define medic = Character("Medic", color="#cccccc")
define engineer = Character("Train Engineer", color="#cccccc")
define hobo = Character("Hobo", color="#cccccc")
define tourist = Character("Tourist", color="#cccccc")

default day5_clue = ""
default day5_item = ""
default day5_witness = ""
default evidence_phone = False

default day5_clues_found = []
default day5_items_found = []
default day5_witnesses_found = []
default day5_clicked_points = []

label day5_path_a_start:
    scene bg rail_depot
    "The morning of the 5th day arrives. Arthur meets me at the old rail depot."
    jump day5_investigation_hub

label day5_investigation_hub:
    call screen day5_depot_investigation
    $ clicked_object = _return
    $ day5_clicked_points.append(clicked_object)
    
    if clicked_object == "tiretracks":
        "They show the exact escape route of the ambushed gangsters."
        $ day5_clues_found.append("The Bloody Tire Tracks")
        jump day5_investigation_hub
    elif clicked_object == "dogtracks":
        "Just stray animals drawn to the blood."
        $ day5_clues_found.append("The Wild Dog Tracks")
        jump day5_investigation_hub
    elif clicked_object == "oilpuddle":
        "Looks like normal car trouble."
        $ day5_clues_found.append("The Leaking Oil Puddle")
        jump day5_investigation_hub
        
    elif clicked_object == "ticketstub":
        "I found a Train Ticket Stub."
        $ day5_items_found.append("The Train Ticket Stub")
        $ inventory_bag_items.append("The Train Ticket Stub")
        jump day5_investigation_hub
    elif clicked_object == "wallet":
        "Just an Empty Wallet."
        $ day5_items_found.append("The Empty Wallet")
        $ inventory_bag_items.append("The Empty Wallet")
        jump day5_investigation_hub
    elif clicked_object == "toolbox":
        "Heavy junk left behind by a mechanic."
        $ day5_items_found.append("The Rusty Toolbox")
        $ inventory_bag_items.append("The Rusty Toolbox")
        jump day5_investigation_hub
        
    elif clicked_object == "phone":
        "A Burner Phone confirming a midnight dock war."
        $ evidence_phone = True 
        jump day5_investigation_hub
        
    elif clicked_object == "medic":
        medic "They forced me to treat a wounded gangster muttering about the docks!"
        $ day5_witnesses_found.append("Medic 1")
        jump day5_investigation_hub
    elif clicked_object == "engineer":
        engineer "That driver just fell off a moving cargo train."
        $ day5_witnesses_found.append("Train Engineer 1")
        jump day5_investigation_hub
    elif clicked_object == "hobo":
        hobo "The government is poisoning the water supply!"
        $ day5_witnesses_found.append("Hobo 1")
        jump day5_investigation_hub
    elif clicked_object == "tourist":
        tourist "I thought they were filming a zombie movie."
        $ day5_witnesses_found.append("Tourist 1")
        jump day5_investigation_hub
        
    elif clicked_object == "newsroom":
        jump day5_morning_newspaper

label day5_morning_newspaper:
    scene bg newsroom
    "Time to review my Reporter's Notepad and write the final story."

label select_day5_clue:
    "What was the most credible information I gathered at the rail depot?"
    menu:
        "The Bloody Tire Tracks" if "The Bloody Tire Tracks" in day5_clues_found:
            "Description: Exact escape route of the ambushed gangsters."
            menu:
                "Confirm this choice":
                    $ day5_clue = "The Bloody Tire Tracks"
                "Pick something else":
                    jump select_day5_clue
        "The Wild Dog Tracks" if "The Wild Dog Tracks" in day5_clues_found:
            "Description: Stray animals drawn to the blood."
            menu:
                "Confirm this choice":
                    $ day5_clue = "The Wild Dog Tracks"
                "Pick something else":
                    jump select_day5_clue
        "The Leaking Oil Puddle" if "The Leaking Oil Puddle" in day5_clues_found:
            "Description: Hides the fact there was a violent shootout."
            menu:
                "Confirm this choice":
                    $ day5_clue = "The Leaking Oil Puddle"
                "Pick something else":
                    jump select_day5_clue

label select_day5_item:
    "What was the most credible object I gathered at the rail depot?"
    menu:
        "The Train Ticket Stub" if "The Train Ticket Stub" in day5_items_found:
            "Description: Proves the gangs were planning to leave town."
            menu:
                "Confirm this choice":
                    $ day5_item = "The Train Ticket Stub"
                "Pick something else":
                    jump select_day5_item
        "The Empty Wallet" if "The Empty Wallet" in day5_items_found:
            "Description: A pickpocket's discarded trash."
            menu:
                "Confirm this choice":
                    $ day5_item = "The Empty Wallet"
                "Pick something else":
                    jump select_day5_item
        "The Rusty Toolbox" if "The Rusty Toolbox" in day5_items_found:
            "Description: Adds nothing to the investigation."
            menu:
                "Confirm this choice":
                    $ day5_item = "The Rusty Toolbox"
                "Pick something else":
                    jump select_day5_item

label select_day5_witness:
    "Who had the most convincing story at the rail depot?"
    menu:
        "Medic" if "Medic 1" in day5_witnesses_found:
            "Testimony: Forced to treat a wounded gangster talking about a midnight dock war."
            menu:
                "Confirm this choice":
                    $ day5_witness = "Medic 1"
                "Pick something else":
                    jump select_day5_witness
        "Train Engineer" if "Train Engineer 1" in day5_witnesses_found:
            "Testimony: Claims the driver simply fell off a moving cargo train."
            menu:
                "Confirm this choice":
                    $ day5_witness = "Train Engineer 1"
                "Pick something else":
                    jump select_day5_witness
        "Hobo" if "Hobo 1" in day5_witnesses_found:
            "Testimony: Believes the government is poisoning the water supply."
            menu:
                "Confirm this choice":
                    $ day5_witness = "Hobo 1"
                "Pick something else":
                    jump select_day5_witness
        "Tourist" if "Tourist 1" in day5_witnesses_found:
            "Testimony: Thought the shootout was just a movie set."
            menu:
                "Confirm this choice":
                    $ day5_witness = "Tourist 1"
                "Pick something else":
                    jump select_day5_witness

label day5_api_execution:
    call calculate_day5_credibility
    python:
        article_result = sheetdb_client.fetch_newspaper_article(day5_clue, day5_item, day5_witness, "day5")
        daily_headline = article_result.get("headline", "Error: Story Not Found")
        daily_body = article_result.get("body", "Error: Check database connection.")
        
    "THE DAILY HERALD"
    "Headline: [daily_headline]"
    "[daily_body]"
    "Editor's Note: This article was rated as [daily_rating]!"
    "My final journalistic credibility is [total_credibility_score]."
    jump day5_path_a_climax
    
label day5_path_a_climax:
    scene bg docks_midnight
    "We hide on a hill overlooking the docks as the two gangs arrive."
    menu:
        "Tell Arthur to sneak down closer for a picture":
            "Arthur moves in and is killed in the crossfire."
            "THE DAILY HERALD"
            "Headline: Tragedy at the Docks: Syndicate War Claims the Life of Local Reporter"
            "Ending 1: The Dark Path Unlocked."
            return
        "Grab Arthur’s arm and stop him":
            "We stay hidden and survive, publishing a co-authored expose."
            "THE DAILY HERALD"
            "Headline: The Midnight Bust: River Boys and Iron Syndicate Exposed"
            "Ending 2: The Redemption Path Unlocked."
            return

label day5_path_b_start:
    scene bg police_station
    with fade
    "Arthur tackled Vance to the ground, saving my life during the bank robbery."
    if evidence_lighter and evidence_letter and evidence_ledger:
        "Together, we dump all our hard evidence on the Police Chief's desk."
        scene bg docks_midnight
        "Dozens of police cars surround the docks, arresting both gangs before a shot is fired."
        "Ending 3: The Clean Sweep Unlocked."
        return
    else:
        "We survived, but I didn't gather enough hard evidence to take down Editor Vance."
        return