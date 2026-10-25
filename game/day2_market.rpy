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
image desk_newspaper = im.Scale("gui/desk_newspaper.jpg", 1920, 1080)
image d2newsroom1 = "gui/newsroom_scenes/Day2_Scene1.jpg"
image d2newsroom2 = "gui/newsroom_scenes/Day2_Scene2.jpg"

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

# ==============================================================================
# DAY 2 BRIEFING
# ==============================================================================
label day2_start:
    $ current_day = 2
    python:
        for item in ["The Broken Pocket Watch", "The Lost Dog Collar"]:
            if item in inventory_bag_items:
                inventory_bag_items.remove(item)

    play sting "audio/sting_day_transition.ogg" volume 0.75
    play music "audio/bgm_newsroom.ogg" fadeout 1.0 fadein 1.5 volume 0.55 if_changed
    play ambient "audio/amb_newsroom.ogg" fadeout 0.8 fadein 1.0 volume 0.40 if_changed

    scene bg newsroom
    scene d2newsroom1 with dissolve
    kenneth "{cps=28}Something happened in the market plaza. A new electronics store just opened{/cps}{w=2.5}{nw}"
    scene d2newsroom2 with dissolve
    kenneth "{cps=28}Get over there and bring me a story{/cps}{w=1}{nw}"
    scene d2newsroom1 with dissolve
    kenneth "{cps=28}Also I heard that a fruit stand burned down, don't mind that and just focus on the new store story{/cps}{w=5}{nw}"

    play sound "audio/sfx_footsteps_move.ogg"
    jump day2_investigation_hub

# ==============================================================================
# DAY 2 MARKET PLAZA (MAIN HUB)
# ==============================================================================
label day2_investigation_hub:
    scene bg market_plaza at day2_plaza_origin
    play music "audio/bgm_day2_market.ogg" fadeout 1.0 fadein 1.2 volume 0.55 if_changed
    play ambient "audio/amb_market_plaza.ogg" fadeout 0.8 fadein 1.0 volume 0.45 if_changed

    call screen day2_market_investigation
    $ clicked_object = _return

    show screen day2_market_investigation

    if clicked_object == "musician":
        play sound "audio/sfx_guitar_strum.ogg"
        musician "I saw a freak lightning strike from a clear sky!"
        musician "It hit the fruit stand and set it ablaze!"
        musician "Maybe i'll write a song about it!"
        if "Street Musician 1" not in day2_witnesses_found:
            play sound "audio/ui_notepad_flip.ogg"
            $ day2_witnesses_found.append("Street Musician 1")
        hide screen day2_market_investigation
        jump day2_investigation_hub

    elif clicked_object == "kids":
        "Just kids playing on the road."
        hide screen day2_market_investigation
        jump day2_investigation_hub

    elif clicked_object == "ruined_stall":
        play sound "audio/sfx_footsteps_move.ogg"
        hide screen day2_market_investigation
        jump day2_ruined_stall

    elif clicked_object == "bakery":
        play sound "audio/sfx_shop_bell.ogg"
        hide screen day2_market_investigation
        jump day2_bakery

    elif clicked_object == "electric_shop":
        play sound "audio/sfx_shop_bell.ogg"
        hide screen day2_market_investigation
        jump day2_electric_shop

    elif clicked_object == "townhall":
        play sound "audio/sfx_footsteps_move.ogg"
        hide screen day2_market_investigation
        jump day2_townhall

    elif clicked_object == "bench":
        play sound "audio/sfx_footsteps_move.ogg"
        hide screen day2_market_investigation
        jump day2_bench

    elif clicked_object == "newsroom":
        play sound "audio/sfx_van_door.ogg"
        hide screen day2_market_investigation
        jump day2_newspaper_minigame

    else:
        hide screen day2_market_investigation
        jump day2_investigation_hub

# ==============================================================================
# DAY 2 RUINED STALL & CLOSE-UPS
# ==============================================================================
label day2_ruined_stall:
    scene bg ruined_stall
    play music "audio/bgm_day2_market.ogg" fadeout 1.0 fadein 1.0 volume 0.50 if_changed
    play ambient "audio/amb_ruined_stall.ogg" fadeout 0.8 fadein 0.8 volume 0.45 if_changed

    call screen day2_ruined_stall_environment
    $ clicked_object = _return

    show screen day2_ruined_stall_environment

    if clicked_object == "gascan":
        play sound "audio/sfx_camera_shutter.ogg"
        "It reeks of accelerant."
        if "The Scorched Gas Can" not in day2_clues_found:
            play sound "audio/ui_notepad_flip.ogg"
            $ day2_clues_found.append("The Scorched Gas Can")
        "The scorched gas can is a clue that the fire was started intentionally."
        hide screen day2_ruined_stall_environment
        jump day2_ruined_stall

    elif clicked_object == "toycar":
        if "The Melted Toy Car" not in day2_clues_found:
            play sound "audio/ui_notepad_flip.ogg"
            $ day2_clues_found.append("The Melted Toy Car")
        "Sad collateral damage."
        "I'm glad no one was hurt, but this melted toy car is a clue that a child might have been playing with matches."
        hide screen day2_ruined_stall_environment
        jump day2_ruined_stall

    elif clicked_object == "cashier":
        play sound "audio/sfx_footsteps_move.ogg"
        hide screen day2_ruined_stall_environment
        jump day2_cashier_closeup

    elif clicked_object == "zoomstall":
        play sound "audio/sfx_footsteps_move.ogg"
        hide screen day2_ruined_stall_environment
        jump day2_stall_zoom

    elif clicked_object == "vendor":
        if "Vendor 1" not in day2_witnesses_found:
            play sound "audio/ui_notepad_flip.ogg"
            $ day2_witnesses_found.append("Vendor 1")
        vendor "I stopped paying protection money... and they burned my shop!"
        vendor "I have no idea who did it, but I know it was the River Boys!"
        hide screen day2_ruined_stall_environment
        jump day2_ruined_stall

    elif clicked_object == "townhall":
        play sound "audio/sfx_footsteps_move.ogg"
        hide screen day2_ruined_stall_environment
        jump day2_townhall

    elif clicked_object == "another_stall":
        play sound "audio/sfx_footsteps_move.ogg"
        hide screen day2_ruined_stall_environment
        jump day2_another_stall

    elif clicked_object == "return_to_plaza":
        play sound "audio/sfx_footsteps_move.ogg"
        hide screen day2_ruined_stall_environment
        jump day2_investigation_hub

    else:
        hide screen day2_ruined_stall_environment
        jump day2_ruined_stall

label day2_stall_zoom:
    if evidence_letter:
        scene bg cashier_without_letter
    else:
        scene bg cashier_with_letter

    play music "audio/bgm_day2_market.ogg" fadeout 1.0 fadein 1.0 volume 0.50 if_changed
    play ambient "audio/amb_ruined_stall.ogg" fadeout 0.8 fadein 0.8 volume 0.45 if_changed

    call screen day2_zoomstall_view
    $ clicked_object = _return

    show screen day2_zoomstall_view

    if clicked_object == "evidence_letter":
        play sound "audio/sfx_paper_rustle.ogg"
        hide screen day2_zoomstall_view
        scene bg extortion_letter
        call screen day2_extortion_letter_view
        $ clicked_object = _return
        show screen day2_extortion_letter_view

        if clicked_object == "return":
            $ evidence_letter = True
            play sound "audio/sfx_paper_rustle.ogg"
            play sting "audio/sting_clue_major.ogg" volume 0.75
            if "The Extortion Letter" not in inventory_bag_items:
                $ inventory_bag_items.append("The Extortion Letter")
                $ renpy.notify("You got The Extortion Letter.")
            "An extortion letter signed with the blue anchor stamp of The River Boys."

        hide screen day2_extortion_letter_view
        jump day2_stall_zoom

    elif clicked_object == "camera":
        if not photographer_interviewed:
            "It's busted. I have no use for this; it's not worth my time."
        else:
            play sound "audio/sfx_pickup_item.ogg"
            if "The Melted Camera" not in inventory_bag_items:
                $ inventory_bag_items.append("The Melted Camera")
                $ renpy.notify("You got The Melted Camera.")
            "I spot the photographer's damaged camera in the debris."
            "If I bring this to the Froi at the Town Electronics Shop, he might be able to recover a photo from it."
        hide screen day2_zoomstall_view
        jump day2_stall_zoom

    else:
        play sound "audio/ui_cancel.ogg"
        hide screen day2_zoomstall_view
        jump day2_ruined_stall

label day2_another_stall:
    scene bg another_stall
    call screen day2_another_stall_view
    play sound "audio/ui_cancel.ogg"
    hide screen day2_another_stall_view
    jump day2_ruined_stall

label day2_cashier_closeup:
    if not evidence_letter:
        scene bg cashier_with_letter
    else:
        scene bg cashier_without_letter

    play music "audio/bgm_day2_market.ogg" fadeout 1.0 fadein 1.0 volume 0.50 if_changed
    play ambient "audio/amb_ruined_stall.ogg" fadeout 0.8 fadein 0.8 volume 0.45 if_changed

    call screen day2_cashier_environment
    $ clicked_object = _return

    show screen day2_cashier_environment

    if clicked_object == "letter":
        $ evidence_letter = True
        hide screen day2_cashier_environment
        scene bg cashier_without_letter
        play sound "audio/sfx_paper_rustle.ogg"
        play sting "audio/sting_clue_major.ogg" volume 0.75
        if "The Extortion Letter" not in inventory_bag_items:
            $ inventory_bag_items.append("The Extortion Letter")
            $ renpy.notify("You got The Extortion Letter.")
        "An extortion letter signed with the blue anchor stamp of The River Boys."
        jump day2_cashier_closeup

    elif clicked_object == "back_to_stall":
        play sound "audio/ui_cancel.ogg"
        hide screen day2_cashier_environment
        jump day2_ruined_stall

    else:
        play sound "audio/ui_cancel.ogg"
        hide screen day2_cashier_environment
        jump day2_ruined_stall

# ==============================================================================
# DAY 2 BAKERY & KITCHEN
# ==============================================================================
label day2_bakery:
    scene bg bakery_stall
    play music "audio/bgm_day2_market.ogg" fadeout 1.0 fadein 1.0 volume 0.50 if_changed
    play ambient "audio/amb_bakery.ogg" fadeout 0.8 fadein 0.8 volume 0.45 if_changed

    call screen day2_bakery_environment
    $ clicked_object = _return

    show screen day2_bakery_environment

    if clicked_object == "clerk_bakery":
        if not cat_fed and "Bread" not in inventory_bag_items:
            bakery_clerk "There's a stray cat that keeps hanging around the plaza. It looks hungry."
            bakery_clerk "Here, have some leftover bread on the house!"
            play sound "audio/sfx_pickup_item.ogg"
            $ inventory_bag_items.append("Bread")
            $ renpy.notify("You got Bread.")
        else:
            bakery_clerk "Enjoy the pastries!"
        hide screen day2_bakery_environment
        jump day2_bakery

    elif clicked_object == "customer1":
        bakery_customer "These pastries are to die for!"
        bakery_customer "I mean, with all the oil that they put in them, I might actually die!"
        hide screen day2_bakery_environment
        jump day2_bakery

    elif clicked_object == "kitchen":
        play sound "audio/sfx_door_open.ogg"
        hide screen day2_bakery_environment
        jump day2_bakery_kitchen

    elif clicked_object == "return_to_plaza":
        play sound "audio/sfx_shop_bell.ogg"
        hide screen day2_bakery_environment
        jump day2_investigation_hub

    else:
        hide screen day2_bakery_environment
        jump day2_bakery

label day2_bakery_kitchen:
    scene bg bakery_kitchen
    play music "audio/bgm_day2_market.ogg" fadeout 1.0 fadein 1.0 volume 0.50 if_changed
    play ambient "audio/amb_bakery.ogg" fadeout 0.8 fadein 0.8 volume 0.50 if_changed

    call screen day2_bakery_kitchen_environment
    $ clicked_object = _return

    show screen day2_bakery_kitchen_environment

    if clicked_object == "oil":
        if "The Spilled Cooking Oil" not in day2_clues_found:
            play sound "audio/ui_notepad_flip.ogg"
            $ day2_clues_found.append("The Spilled Cooking Oil")
        "A greasy puddle near a stove."
        "Maybe this spilled cooking oil is a clue that the fire was a simple kitchen grease fire accident."
        hide screen day2_bakery_kitchen_environment
        jump day2_bakery_kitchen

    elif clicked_object == "baker":
        if "Baker 1" not in day2_witnesses_found:
            play sound "audio/ui_notepad_flip.ogg"
            $ day2_witnesses_found.append("Baker 1")
        baker "The owner of the stall is a good friend of mine. He is my supplier of flour and sugar. I can't believe someone would burn his stall down!"
        baker "Obviously it was a targeted hit by rival bakers!"
        baker "They're too jealous of my success that cut my supply of ingredients"
        hide screen day2_bakery_kitchen_environment
        jump day2_bakery_kitchen

    else:
        play sound "audio/sfx_door_open.ogg"
        hide screen day2_bakery_kitchen_environment
        jump day2_bakery

# ==============================================================================
# DAY 2 ELECTRONICS SHOP, TOWN HALL & BENCH
# ==============================================================================
label day2_electric_shop:
    scene bg electric_shop
    play music "audio/bgm_day2_market.ogg" fadeout 1.0 fadein 1.0 volume 0.50 if_changed
    play ambient "audio/amb_electronics_shop.ogg" fadeout 0.8 fadein 0.8 volume 0.45 if_changed

    call screen day2_electric_shop_environment
    $ clicked_object = _return

    show screen day2_electric_shop_environment

    if clicked_object == "electronic_man":
        if "The Melted Camera" in inventory_bag_items:
            if not blurry_photo_obtained:
                play sound "audio/sfx_pickup_item.ogg"
                "I hand the broken camera over to the electronics technician."
                play sound "audio/sfx_tech_recover.ogg"
                electronic_man "Give me a moment... The casing is completely melted, but the memory chip inside is still readable!"
                $ blurry_photo_obtained = True
                $ inventory_bag_items.remove("The Melted Camera")
                if "The Melted Camera" not in day2_items_found:
                    $ day2_items_found.append("The Melted Camera")
                if "Blurry Photograph" not in inventory_bag_items:
                    $ inventory_bag_items.append("Blurry Photograph")
                play sting "audio/sting_clue_major.ogg" volume 0.75
                $ renpy.notify("Evidence added: Blurry Photograph.")
                call screen day2_blurry_photo_overlay
                play sound "audio/sfx_paper_rustle.ogg"
                "The recovered blurry photo clearly shows the fire starting! It's now recorded in my evidence for the report."
            else:
                electronic_man "Here is the blurry photograph I recovered from that melted camera."
                play sound "audio/sfx_paper_rustle.ogg"
                call screen day2_blurry_photo_overlay
                play sound "audio/ui_cancel.ogg"
        else:
            electronic_man "Welcome to the best electronics repair shop in town! I can fix anything, from radios to cameras."
            electronic_man "You can look around and see if you find anything that needs fixing."
        hide screen day2_electric_shop_environment
        jump day2_electric_shop

    elif clicked_object == "return_to_plaza":
        play sound "audio/sfx_shop_bell.ogg"
        hide screen day2_electric_shop_environment
        jump day2_investigation_hub

    else:
        hide screen day2_electric_shop_environment
        jump day2_electric_shop

label day2_townhall:
    scene bg townhall
    play music "audio/bgm_day2_market.ogg" fadeout 1.0 fadein 1.0 volume 0.55 if_changed
    play ambient "audio/amb_market_plaza.ogg" fadeout 0.8 fadein 0.8 volume 0.40 if_changed

    call screen day2_townhall_environment
    $ clicked_object = _return

    show screen day2_townhall_environment

    if clicked_object == "shopper":
        if "Shopper 1" not in day2_witnesses_found:
            play sound "audio/ui_notepad_flip.ogg"
            $ day2_witnesses_found.append("Shopper 1")
        shopper "He caused the fire himself for insurance money!"
        shopper "People this days are so greedy, I can't believe it!"
        hide screen day2_townhall_environment
        jump day2_townhall

    elif clicked_object == "inside":
        play sound "audio/sfx_door_open.ogg"
        hide screen day2_townhall_environment
        jump day2_townhall_inside

    elif clicked_object == "arthur":
        arthur "Back off, rookie! I'm interviewing these shopper first."
        hide screen day2_townhall_environment
        jump day2_townhall

    else:
        play sound "audio/sfx_footsteps_move.ogg"
        hide screen day2_townhall_environment
        jump day2_investigation_hub

label day2_townhall_inside:
    scene bg townhall_inside
    play music "audio/bgm_day2_market.ogg" fadeout 1.0 fadein 1.0 volume 0.45 if_changed
    play ambient "audio/amb_townhall_int.ogg" fadeout 0.8 fadein 0.8 volume 0.45 if_changed

    call screen day2_townhall_inside_environment
    $ clicked_object = _return

    show screen day2_townhall_inside_environment

    if clicked_object == "photographer":
        if not photographer_interviewed:
            play sound "audio/ui_notepad_flip.ogg"
            photographer "I got mugged by the gangsters. I even got a shot of the ones who burned the stall, but they burned my camera along with it."
            photographer "I don't have much to say, but I can tell you that the gangsters are part of a secret society called The River Boys."
            $ photographer_interviewed = True
            "(I think that camera might be worth my time after all.)"
        else:
            photographer "I don't have anything else to add kid."
        hide screen day2_townhall_inside_environment
        jump day2_townhall_inside

    else:
        play sound "audio/sfx_door_open.ogg"
        hide screen day2_townhall_inside_environment
        jump day2_townhall

label day2_bench:
    if cat_fed:
        scene bg bench_bread
    else:
        scene bg bench

    play music "audio/bgm_day2_market.ogg" fadeout 1.0 fadein 1.0 volume 0.55 if_changed
    play ambient "audio/amb_market_plaza.ogg" fadeout 0.8 fadein 0.8 volume 0.45 if_changed

    call screen day2_bench_environment
    $ clicked_object = _return

    show screen day2_bench_environment

    if clicked_object == "ticket":
        if not cat_fed:
            if "Bread" in inventory_bag_items:
                menu:
                    "Give bread to the cat":
                        play sound "audio/sfx_cat_happy.ogg"
                        "I toss the bread to the cat. It happily takes it and is finally distracted!"
                        $ cat_fed = True
                        $ inventory_bag_items.remove("Bread")
                    "Don't give bread":
                        play sound "audio/sfx_cat_hiss.ogg"
                        "The cat hisses at me, guarding the ticket."
            else:
                play sound "audio/sfx_cat_hiss.ogg"
                "The cat hisses at me, baring its claws as I reach for the ticket."
                "Maybe I need to befriend the cat first to access the ticket. Maybe kitty likes food."
        else:
            play sound "audio/sfx_paper_rustle.ogg"
            if "The Dropped Lottery Ticket" not in day2_items_found:
                $ day2_items_found.append("The Dropped Lottery Ticket")
                $ inventory_bag_items.append("The Dropped Lottery Ticket")
            "With the cat distracted, I safely grab the dropped scratch ticket."
            "Too bad it's a losing ticket, but it might be useful for my report..."
            "or not."
        hide screen day2_bench_environment
        jump day2_bench

    elif clicked_object == "cigar":
        play sound "audio/sfx_pickup_item.ogg"
        "A half-smoked, imported cigar was dropped nearby."
        "Maybe this expensive cigar is a clue that someone wealthy was involved in the fire."
        if "The Expensive Cigar" not in day2_items_found:
            $ day2_items_found.append("The Expensive Cigar")
            $ inventory_bag_items.append("The Expensive Cigar")
        hide screen day2_bench_environment
        jump day2_bench

    elif clicked_object == "return_to_plaza":
        play sound "audio/sfx_footsteps_move.ogg"
        hide screen day2_bench_environment
        jump day2_investigation_hub

    else:
        hide screen day2_bench_environment
        jump day2_investigation_hub

# ==============================================================================
# DAY 2 NEWSPAPER MINIGAME & EDITION RESULTS
# ==============================================================================
label day2_newspaper_minigame:
    $ hide_all_investigation_screens()
    play sound "audio/sfx_typewriter_write.ogg"
    play music "audio/bgm_newsroom.ogg" fadeout 1.0 fadein 1.2 volume 0.55 if_changed
    play ambient "audio/amb_newsroom.ogg" fadeout 1.0 fadein 1.0 volume 0.35 if_changed

    scene news_creation with dissolve
    "Time to review my Reporter's Notepad and write the market edition."

label select_day2_clue:
    play sound "audio/ui_notepad_flip.ogg"
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
    play sound "audio/ui_notepad_flip.ogg"
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
    play sound "audio/ui_notepad_flip.ogg"
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
        day2_accurate_picks = (
            (day2_clue == "The Scorched Gas Can")
            + (day2_item == "The Melted Camera")
            + (day2_witness == "Vendor 1")
        )

    scene desk_newspaper
    play sound "audio/sfx_newspaper_print.ogg"
    "Let's see how the market edition turned out..."

    if day2_accurate_picks >= 2:
        play sting "audio/sting_rating_high.ogg" volume 0.80
    else:
        play sting "audio/sting_rating_low.ogg" volume 0.80

    call screen newspaper_results_ui(daily_headline, daily_body, daily_rating, total_credibility_score)
    play sound "audio/sfx_paper_rustle.ogg"
    $ renpy.force_autosave(True)
    jump day3_start