image bg warehouse = im.Scale("gui/warehouse/warehouse_front.png", 1920, 1072)
image bg warehouse_back = im.Scale("gui/warehouse/bg_warehouse_back.png", 1920, 1072)
image bg warehouse_office = im.Scale("gui/day1_office/bg_office.png", 1920, 1072)
image bg inside_warehouse = im.Scale("gui/day1_inside_warehouse/bg_inside_warehouse.png", 1920, 1072)
define vance = Character("Editor Vance", color="#b30000")
define arthur = Character("Arthur", color="#ff9900")
define watchman = Character("Watchman", color="#cccccc")
define fisherman = Character("Fisherman", color="#cccccc")
define driver = Character("Delivery Driver", color="#cccccc")
define jogger = Character("Jogger", color="#cccccc")

default day1_clue = ""
default day1_item = ""
default day1_witness = ""
default evidence_lighter = False

default day1_clues_found = []
default day1_items_found = []
default day1_witnesses_found = []
default day1_clicked_points = []
default inventory_bag_items = []

label stage1_briefing:
    scene bg newsroom 
    vance "Listen up, rookie. I don't want you digging into the rising crime rate. That's an order."
    vance "Head down to the riverside shipping warehouse. Someone vandalized it. Get a simple quote and come back."
    
    scene bg warehouse
    arthur "Well, look who finally showed up. Stay out of my way, rookie."
    jump day1_investigation_hub

label day1_investigation_hub:
    call screen day1_warehouse_investigation
    $ clicked_object = _return
    $ day1_clicked_points.append(clicked_object)
    
    if clicked_object == "paint_can":
        "It smells like industrial-grade spray paint."
        $ day1_clues_found.append("The Smashed Paint Can")
        jump day1_investigation_hub
    elif clicked_object == "whiskey":
        "Just a cheap bottle left by a homeless person."
        $ day1_clues_found.append("The Broken Whiskey Bottle")
        jump day1_investigation_hub
    elif clicked_object == "pizza":
        "Empty food boxes scattered around."
        $ day1_clues_found.append("The Torn Pizza Box")
        jump day1_investigation_hub
        
    elif clicked_object == "keyring":
        "I see something hanging on a fence... It's a Janitor's Keyring."
        $ day1_items_found.append("The Janitor's Keyring")
        $ inventory_bag_items.append("The Janitor's Keyring")
        jump day1_investigation_hub
    elif clicked_object == "watch":
        "There's a Broken Pocket Watch in the water."
        $ day1_items_found.append("The Broken Pocket Watch")
        $ inventory_bag_items.append("The Broken Pocket Watch")
        jump day1_investigation_hub
    elif clicked_object == "collar":
        "A Lost Dog Collar lies in the dirt."
        $ day1_items_found.append("The Lost Dog Collar")
        $ inventory_bag_items.append("The Lost Dog Collar")
        jump day1_investigation_hub
        
    elif clicked_object == "lighter":
        "It's a Brass Lighter engraved with a skull and crossed wrenches."
        $ evidence_lighter = True 
        jump day1_investigation_hub
        
    elif clicked_object == "watchman":
        watchman "I saw them... men in heavy leather jackets marking the warehouse as their territory."
        $ day1_witnesses_found.append("Watchman 1")
        jump day1_investigation_hub
    elif clicked_object == "warehouse_graffiti":
        "The graffiti looks fresh. Someone wanted to mark this place as their territory."
        jump day1_investigation_hub
    elif clicked_object == "warehouse_windows":
        "They destroyed even the warehouse windows."
        jump day1_investigation_hub
    elif clicked_object == "warehouse_door":
        jump day1_warehouse_inside
    elif clicked_object == "warehouse_back":
        jump day1_warehouse_back
    elif clicked_object == "warehouse_office":
        jump day1_warehouse_office
    elif clicked_object == "fisherman":
        fisherman "I swear, the warehouse was attacked by angry teenagers!"
        $ day1_witnesses_found.append("Fisherman 1")
        jump day1_investigation_hub
    elif clicked_object == "driver":
        driver "It was a rival shipping company trying to steal business."
        $ day1_witnesses_found.append("Delivery Driver 1")
        jump day1_investigation_hub
    elif clicked_object == "jogger":
        jogger "I saw a glowing ghost damage the walls!"
        $ day1_witnesses_found.append("Jogger 1")
        jump day1_investigation_hub
        
    elif clicked_object == "newsroom":
        jump day1_newspaper_minigame

label day1_warehouse_back:
    scene bg warehouse_back
    call screen day1_warehouse_back_environment
    scene bg warehouse
    jump day1_investigation_hub

label day1_warehouse_inside:
    scene bg inside_warehouse
    call screen day1_warehouse_inside_environment
    scene bg warehouse
    jump day1_investigation_hub

label day1_warehouse_office:
    scene bg warehouse_office
    call screen day1_warehouse_office_environment
    scene bg warehouse
    jump day1_investigation_hub

label day1_newspaper_minigame:
    scene bg newsroom
    "Time to review my Reporter's Notepad and write the evening edition."

label select_day1_clue:
    "What was the most credible information I gathered at the warehouse?"
    menu:
        "The Smashed Paint Can" if "The Smashed Paint Can" in day1_clues_found:
            "Description: Industrial-grade spray paint. Proof of a coordinated, planned job."
            menu:
                "Confirm this choice":
                    $ day1_clue = "The Smashed Paint Can"
                "Pick something else":
                    jump select_day1_clue
        "The Broken Whiskey Bottle" if "The Broken Whiskey Bottle" in day1_clues_found:
            "Description: A cheap bottle left to make the crime look like a random drunk's doing."
            menu:
                "Confirm this choice":
                    $ day1_clue = "The Broken Whiskey Bottle"
                "Pick something else":
                    jump select_day1_clue
        "The Torn Pizza Box" if "The Torn Pizza Box" in day1_clues_found:
            "Description: Garbage meant to frame local teenagers for the vandalism."
            menu:
                "Confirm this choice":
                    $ day1_clue = "The Torn Pizza Box"
                "Pick something else":
                    jump select_day1_clue

label select_day1_item:
    "What was the most credible object I gathered at the warehouse?"
    menu:
        "The Janitor's Keyring" if "The Janitor's Keyring" in day1_items_found:
            "Description: Unlocks restricted offices containing vandalized blueprints."
            menu:
                "Confirm this choice":
                    $ day1_item = "The Janitor's Keyring"
                "Pick something else":
                    jump select_day1_item
        "The Broken Pocket Watch" if "The Broken Pocket Watch" in day1_items_found:
            "Description: An expensive watch with zero connection to the actual crime."
            menu:
                "Confirm this choice":
                    $ day1_item = "The Broken Pocket Watch"
                "Pick something else":
                    jump select_day1_item
        "The Lost Dog Collar" if "The Lost Dog Collar" in day1_items_found:
            "Description: A dirty pet collar that will lead to a completely fake story."
            menu:
                "Confirm this choice":
                    $ day1_item = "The Lost Dog Collar"
                "Pick something else":
                    jump select_day1_item

label select_day1_witness:
    "Who had the most convincing story at the warehouse?"
    menu:
        "Watchman" if "Watchman 1" in day1_witnesses_found:
            "Testimony: Saw men in heavy leather jackets marking the warehouse as territory."
            menu:
                "Confirm this choice":
                    $ day1_witness = "Watchman 1"
                "Pick something else":
                    jump select_day1_witness
        "Fisherman" if "Fisherman 1" in day1_witnesses_found:
            "Testimony: Swears the warehouse was attacked by angry teenagers."
            menu:
                "Confirm this choice":
                    $ day1_witness = "Fisherman 1"
                "Pick something else":
                    jump select_day1_witness
        "Delivery Driver" if "Delivery Driver 1" in day1_witnesses_found:
            "Testimony: Claims it was a rival shipping company trying to steal business."
            menu:
                "Confirm this choice":
                    $ day1_witness = "Delivery Driver 1"
                "Pick something else":
                    jump select_day1_witness
        "Jogger" if "Jogger 1" in day1_witnesses_found:
            "Testimony: Insists they saw a glowing ghost damaging the walls."
            menu:
                "Confirm this choice":
                    $ day1_witness = "Jogger 1"
                "Pick something else":
                    jump select_day1_witness

label day1_api_execution:
    call calculate_day1_credibility
    python:
        article_result = sheetdb_client.fetch_newspaper_article(day1_clue, day1_item, day1_witness)
        daily_headline = article_result.get("headline", "Error: Story Not Found")
        daily_body = article_result.get("body", "Error: Check database connection.")
        
    "THE DAILY HERALD"
    "Headline: [daily_headline]"
    "[daily_body]"
    "Editor's Note: This article was rated as [daily_rating]!"
    "My total journalistic credibility is now [total_credibility_score]."
    jump day2_start