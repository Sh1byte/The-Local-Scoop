# Day 2 Backgrounds
image bg market_plaza = im.Scale("gui/day2_plaza/plaza_front/plaza_front.jpg", 1920, 1072)
image bg ruined_stall = im.Scale("gui/day2_plaza/ruined_stall/burned_stall.jpg", 1920, 1072)
image bg cashier_with_letter = im.Scale("gui/day2_plaza/ruined_stall/cashier_with_letter.jpg", 1920, 1072)
image bg cashier_without_letter = im.Scale("gui/day2_plaza/ruined_stall/cashier_without_letter.jpg", 1920, 1072)
image bg bakery_stall = im.Scale("gui/day2_plaza/bakery/inside_bakery.jpg", 1920, 1072)
image bg electric_shop = im.Scale("gui/day2_plaza/electric_shop/inside_electric_shop.jpg", 1920, 1072)

define vendor = Character("Vendor", color="#cccccc")
define shopper = Character("Shopper", color="#cccccc")
define baker = Character("Baker", color="#cccccc")
define musician = Character("Street Musician", color="#cccccc")
define electronic_man = Character("Electronics Technician", color="#cccccc")

default day2_clue = ""
default day2_item = ""
default day2_witness = ""
default evidence_letter = False
default blurry_photo_obtained = False

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

# ==========================================
# 1. MARKET PLAZA FRONT (HUB)
# ==========================================
label day2_investigation_hub:
    scene bg market_plaza
    call screen day2_market_investigation
    $ clicked_object = _return

    # ITEMS IN PLAZA FRONT
    if clicked_object == "lottery":
        "It's a winning scratch ticket dropped on the pavement."
        if "The Dropped Lottery Ticket" not in day2_items_found:
            $ day2_items_found.append("The Dropped Lottery Ticket")
            $ inventory_bag_items.append("The Dropped Lottery Ticket")
        jump day2_investigation_hub

    elif clicked_object == "cigar":
        "A half-smoked, imported cigar was dropped nearby."
        if "The Expensive Cigar" not in day2_items_found:
            $ day2_items_found.append("The Expensive Cigar")
            $ inventory_bag_items.append("The Expensive Cigar")
        jump day2_investigation_hub

    # WITNESSES IN PLAZA FRONT
    elif clicked_object == "shopper":
        shopper "She caused the fire herself for insurance money!"
        if "Shopper 1" not in day2_witnesses_found:
            $ day2_witnesses_found.append("Shopper 1")
        jump day2_investigation_hub

    elif clicked_object == "musician":
        musician "I saw a freak lightning strike from a clear sky!"
        if "Street Musician 1" not in day2_witnesses_found:
            $ day2_witnesses_found.append("Street Musician 1")
        jump day2_investigation_hub

    elif clicked_object == "arthur":
        arthur "Back off, rookie! I'm interviewing these people first."
        jump day2_investigation_hub

    # NAVIGATION TO SUB-AREAS
    elif clicked_object == "ruined_stall":
        jump day2_ruined_stall
    elif clicked_object == "bakery":
        jump day2_bakery
    elif clicked_object == "electric_shop":
        jump day2_electric_shop
    elif clicked_object == "newsroom":
        jump day2_newspaper_minigame
    else:
        jump day2_investigation_hub

# ==========================================
# 2. THE RUINED FRUIT STAND
# ==========================================
label day2_ruined_stall:
    scene bg ruined_stall
    call screen day2_ruined_stall_environment
    $ clicked_object = _return

    if clicked_object == "gascan":
        "It reeks of accelerant."
        if "The Scorched Gas Can" not in day2_clues_found:
            $ day2_clues_found.append("The Scorched Gas Can")
        jump day2_ruined_stall

    elif clicked_object == "toycar":
        "Sad collateral damage."
        if "The Melted Toy Car" not in day2_clues_found:
            $ day2_clues_found.append("The Melted Toy Car")
        jump day2_ruined_stall

    elif clicked_object == "camera":
        if "The Melted Camera" not in inventory_bag_items:
            $ inventory_bag_items.append("The Melted Camera")
        "I spot a damaged security camera in the debris."
        "If I bring this to the man at the Town Electronics Shop, he might be able to recover a photo from it."
        jump day2_ruined_stall

    elif clicked_object == "cashier":
        jump day2_cashier_closeup

    elif clicked_object == "vendor":
        vendor "I stopped paying protection money... and they burned my shop!"
        if "Vendor 1" not in day2_witnesses_found:
            $ day2_witnesses_found.append("Vendor 1")
        jump day2_ruined_stall

    elif clicked_object == "return_to_plaza":
        jump day2_investigation_hub
    else:
        jump day2_ruined_stall

label day2_cashier_closeup:
    if not evidence_letter:
        scene bg cashier_with_letter
    else:
        scene bg cashier_without_letter

    call screen day2_cashier_environment
    $ clicked_object = _return

    if clicked_object == "letter":
        $ evidence_letter = True
        scene bg cashier_without_letter
        "An extortion letter signed with the blue anchor stamp of The River Boys."
        jump day2_cashier_closeup
    elif clicked_object == "back_to_stall":
        jump day2_ruined_stall
    else:
        jump day2_ruined_stall

# ==========================================
# 3. THE BAKERY STALL
# ==========================================
label day2_bakery:
    scene bg bakery_stall
    call screen day2_bakery_environment
    $ clicked_object = _return

    if clicked_object == "oil":
        "A greasy puddle near a stove."
        if "The Spilled Cooking Oil" not in day2_clues_found:
            $ day2_clues_found.append("The Spilled Cooking Oil")
        jump day2_bakery

    elif clicked_object == "baker":
        baker "It was a targeted hit by rival bakers!"
        if "Baker 1" not in day2_witnesses_found:
            $ day2_witnesses_found.append("Baker 1")
        jump day2_bakery

    elif clicked_object == "return_to_plaza":
        jump day2_investigation_hub
    else:
        jump day2_bakery

# ==========================================
# 4. TOWN ELECTRONICS SHOP
# ==========================================
label day2_electric_shop:
    scene bg electric_shop
    call screen day2_electric_shop_environment
    $ clicked_object = _return

    if clicked_object == "electronic_man":
        if "The Melted Camera" in inventory_bag_items:
            if not blurry_photo_obtained:
                "I hand the broken camera over to the electronics technician."
                electronic_man "Give me a moment... The casing is completely melted, but the memory chip inside is still readable!"
                $ blurry_photo_obtained = True
                if "The Melted Camera" not in day2_items_found:
                    $ day2_items_found.append("The Melted Camera")
                if "Blurry Photograph" not in inventory_bag_items:
                    $ inventory_bag_items.append("Blurry Photograph")
                $ renpy.notify("Evidence added: Blurry Photograph.")
                call screen day2_blurry_photo_overlay
                "The recovered blurry photo clearly shows the fire starting! It's now recorded in my evidence for the report."
            else:
                electronic_man "Here is the blurry photograph I recovered from that melted camera."
                call screen day2_blurry_photo_overlay
        else:
            electronic_man "If you find any damaged electronics or cameras, bring them to me and I'll recover the data."
        jump day2_electric_shop

    elif clicked_object == "return_to_plaza":
        jump day2_investigation_hub
    else:
        jump day2_electric_shop

# ==========================================
# DAY 2 NEWSPAPER MINIGAME
# ==========================================
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
        "Blurry photograph of the fire starting" if "The Melted Camera" in day2_items_found:
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
        article_result = sheetdb_client.fetch_newspaper_article(day2_clue, day2_item, day2_witness, "day2")
        daily_headline = article_result.get("headline", "Error: Story Not Found")
        daily_body = article_result.get("body", "Error: Check database connection.")
       
    "THE DAILY HERALD"
    "Headline: [daily_headline]"
    "[daily_body]"
    "Editor's Note: This article was rated as [daily_rating]!"
    "My total journalistic credibility is now [total_credibility_score]."
    jump day3_start