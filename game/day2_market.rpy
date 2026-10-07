transform day2_plaza_origin:
    xpos 0
    ypos 0
    xanchor 0
    yanchor 0

# ALL backgrounds natively 1920x1072. No scaling applied!
image bg market_plaza = "gui/day2_plaza/plaza_front/plaza_front.png"
image bg ruined_stall = "gui/day2_plaza/market_stalls/bg_market_stall.png"
image bg extortion_letter = "gui/day2_plaza/market_stalls/ruined_stalls/extortion_letter.png"
image bg cashier_with_letter = "gui/day2_plaza/market_stalls/ruined_stalls/bg_ruined_stall.png"
image bg cashier_without_letter = "gui/day2_plaza/market_stalls/ruined_stalls/without_note.png"
image bg bakery_stall = "gui/day2_plaza/bakery/bg_inside_bakery.png"
image bg bakery_kitchen = "gui/day2_plaza/bakery/kitchen/bg_kitchen.png"
image bg electric_shop = "gui/day2_plaza/electric_shop/bg_inside_electronics.png"
image bg townhall = "gui/day2_plaza/townhall/bg_townhall.png"
image bg townhall_inside = "gui/day2_plaza/townhall/inside_townhall/townhall_inside.png"
image bg bench = "gui/day2_plaza/bench/bg_bench.png"
image bg bench_bread = "gui/day2_plaza/bench/bg_bench_bread.jpg"
image bg another_stall = im.Scale("gui/day2_plaza/market_stalls/another_stall/bg_anotherstall.png", 1920, 1072)

define vendor = Character("Vendor", color="#cccccc")
define shopper = Character("Shopper", color="#cccccc")
define baker = Character("Baker", color="#cccccc")
define bakery_clerk = Character("Bakery Clerk", color="#cccccc")
define bakery_customer = Character("Customer", color="#cccccc")
define musician = Character("Street Musician", color="#cccccc")
define electronic_man = Character("Electronics Technician", color="#cccccc")
define photographer = Character("Photographer", color="#cccccc")

default day2_clue = ""
default day2_item = ""
default day2_witness = ""
default evidence_letter = False
default blurry_photo_obtained = False
default cat_fed = False
default photographer_interviewed = False

default day2_clues_found = []
default day2_items_found = []
default day2_witnesses_found = []
default day2_clicked_points = []

label day2_start:
    # Clear out unused items from Day 1 Bag (Keeping the Brass Lighter)
    python:
        for item in ["The Broken Pocket Watch", "The Lost Dog Collar"]:
            if item in inventory_bag_items:
                inventory_bag_items.remove(item)

    scene bg newsroom
    vance "Market plaza. Fruit stand burned to the ground in broad daylight. Go."
    scene bg market_plaza at day2_plaza_origin
    arthur "Go back to the office, rookie."
    jump day2_investigation_hub

label day2_investigation_hub:
    scene bg market_plaza at day2_plaza_origin
    call screen day2_market_investigation
    $ clicked_object = _return
        
    if clicked_object == "musician":
        musician "I saw a freak lightning strike from a clear sky!"
        if "Street Musician 1" not in day2_witnesses_found:
            $ day2_witnesses_found.append("Street Musician 1")
        jump day2_investigation_hub
        
    elif clicked_object == "kids":
        "Just kids playing near the fountain."
        jump day2_investigation_hub
        
    elif clicked_object == "ruined_stall":
        jump day2_ruined_stall
    elif clicked_object == "bakery":
        jump day2_bakery
    elif clicked_object == "electric_shop":
        jump day2_electric_shop
    elif clicked_object == "townhall":
        jump day2_townhall
    elif clicked_object == "bench":
        jump day2_bench
    elif clicked_object == "newsroom":
        jump day2_newspaper_minigame
    else:
        jump day2_investigation_hub

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
    elif clicked_object == "cashier":
        jump day2_cashier_closeup
    elif clicked_object == "zoomstall":
        jump day2_stall_zoom
    elif clicked_object == "vendor":
        vendor "I stopped paying protection money... and they burned my shop!"
        if "Vendor 1" not in day2_witnesses_found:
            $ day2_witnesses_found.append("Vendor 1")
        jump day2_ruined_stall
    elif clicked_object == "townhall":
        jump day2_townhall
    elif clicked_object == "another_stall":
        jump day2_another_stall
    elif clicked_object == "return_to_plaza":
        jump day2_investigation_hub
    else:
        jump day2_ruined_stall

label day2_stall_zoom:
    if evidence_letter:
        scene bg cashier_without_letter
    else:
        scene bg cashier_with_letter
    call screen day2_zoomstall_view
    $ clicked_object = _return

    if clicked_object == "evidence_letter":
        scene bg extortion_letter
        call screen day2_extortion_letter_view
        $ clicked_object = _return
        if clicked_object == "return":
            $ evidence_letter = True
            if "The Extortion Letter" not in inventory_bag_items:
                $ inventory_bag_items.append("The Extortion Letter")
                $ renpy.notify("You got The Extortion Letter.")
            "An extortion letter signed with the blue anchor stamp of The River Boys."
        jump day2_stall_zoom
    elif clicked_object == "camera":
        if not photographer_interviewed:
            "It's busted. I have no use for this; it's not worth my time."
        else:
            if "The Melted Camera" not in inventory_bag_items:
                $ inventory_bag_items.append("The Melted Camera")
                $ renpy.notify("You got The Melted Camera.")
            "I spot the photographer's damaged camera in the debris."
            "If I bring this to the man at the Town Electronics Shop, he might be able to recover a photo from it."
        jump day2_stall_zoom
    else:
        jump day2_ruined_stall

label day2_another_stall:
    scene bg another_stall
    call screen day2_another_stall_view
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
        if "The Extortion Letter" not in inventory_bag_items:
            $ inventory_bag_items.append("The Extortion Letter")
            $ renpy.notify("You got The Extortion Letter.")
        "An extortion letter signed with the blue anchor stamp of The River Boys."
        jump day2_cashier_closeup
    elif clicked_object == "back_to_stall":
        jump day2_ruined_stall
    else:
        jump day2_ruined_stall

label day2_bakery:
    scene bg bakery_stall
    call screen day2_bakery_environment
    $ clicked_object = _return
    
    if clicked_object == "clerk_bakery":
        if not cat_fed and "Bread" not in inventory_bag_items:
            bakery_clerk "Here, have some leftover bread on the house!"
            $ inventory_bag_items.append("Bread")
            $ renpy.notify("You got Bread.")
        else:
            bakery_clerk "Enjoy the pastries!"
        jump day2_bakery
        
    elif clicked_object == "customer1":
        bakery_customer "These pastries are to die for!"
        jump day2_bakery
    elif clicked_object == "kitchen":
        jump day2_bakery_kitchen
    elif clicked_object == "return_to_plaza":
        jump day2_investigation_hub
    else:
        jump day2_bakery

label day2_bakery_kitchen:
    scene bg bakery_kitchen
    call screen day2_bakery_kitchen_environment
    $ clicked_object = _return
    
    if clicked_object == "oil":
        "A greasy puddle near a stove."
        if "The Spilled Cooking Oil" not in day2_clues_found:
            $ day2_clues_found.append("The Spilled Cooking Oil")
        jump day2_bakery_kitchen
    elif clicked_object == "baker":
        baker "It was a targeted hit by rival bakers!"
        if "Baker 1" not in day2_witnesses_found:
            $ day2_witnesses_found.append("Baker 1")
        jump day2_bakery_kitchen
    else:
        jump day2_bakery

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
                $ inventory_bag_items.remove("The Melted Camera")
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

label day2_townhall:
    scene bg townhall
    call screen day2_townhall_environment
    $ clicked_object = _return

    if clicked_object == "shopper":
        shopper "She caused the fire herself for insurance money!"
        if "Shopper 1" not in day2_witnesses_found:
            $ day2_witnesses_found.append("Shopper 1")
        jump day2_townhall
    elif clicked_object == "inside":
        jump day2_townhall_inside
    elif clicked_object == "arthur":
        arthur "Back off, rookie! I'm interviewing these people first."
        jump day2_townhall
    else:
        jump day2_investigation_hub

label day2_townhall_inside:
    scene bg townhall_inside
    call screen day2_townhall_inside_environment
    $ clicked_object = _return

    if clicked_object == "photographer":
        if not photographer_interviewed:
            photographer "I got mugged by the gangsters. I even got a shot of the ones who burned the stall, but they burned my camera along with it."
            $ photographer_interviewed = True
            "I think that camera might be worth my time after all."
        else:
            photographer "I don't have anything else to add."
        jump day2_townhall_inside
    else:
        jump day2_townhall

label day2_bench:
    if cat_fed:
        scene bg bench_bread
    else:
        scene bg bench
       
    call screen day2_bench_environment
    $ clicked_object = _return
   
    if clicked_object == "ticket":
        if not cat_fed:
            if "Bread" in inventory_bag_items:
                menu:
                    "Give bread to the cat":
                        "I toss the bread to the cat. It happily takes it and is finally distracted!"
                        $ cat_fed = True
                        $ inventory_bag_items.remove("Bread")
                    "Don't give bread":
                        "The cat hisses at me, guarding the ticket."
            else:
                "The cat hisses at me, baring its claws as I reach for the ticket."
                "Maybe I need to befriend the cat first to access the ticket. Maybe kitty likes food."
        else:
            if "The Dropped Lottery Ticket" not in day2_items_found:
                $ day2_items_found.append("The Dropped Lottery Ticket")
                $ inventory_bag_items.append("The Dropped Lottery Ticket")
            "With the cat distracted, I safely grab the dropped scratch ticket."
        jump day2_bench
       
    elif clicked_object == "cigar":
        "A half-smoked, imported cigar was dropped nearby."
        if "The Expensive Cigar" not in day2_items_found:
            $ day2_items_found.append("The Expensive Cigar")
            $ inventory_bag_items.append("The Expensive Cigar")
        jump day2_bench
       
    elif clicked_object == "return_to_plaza":
        jump day2_investigation_hub
    else:
        jump day2_bench

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