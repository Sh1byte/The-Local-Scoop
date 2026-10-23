image d5newsroom1 = "gui/newsroom_scenes/Day5_Scene1.jpg"

define arthur = Character("Arthur", color="#cccccc")
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

# ==========================================
# START & DEPOT ENTRANCE (MAIN HUB)
# ==========================================
label day5_path_a_start:
    $ current_day = 5
    show screen global_hud
    scene expression "gui/day5_abandoned_station/Depot_Entrance/bg Depot_Entrance.jpg" at topleft
    "The morning of the 5th day arrives. Because the money is missing, both gangs blame each other."
    "I've been dispatched to investigate a morning lead at an old rail depot where a getaway driver was found injured."
    "Arthur meets me here in the morning sun, completely unaware that I stole the cash."
    jump day5_investigation_hub

label day5_investigation_hub:
    scene expression "gui/day5_abandoned_station/Depot_Entrance/bg Depot_Entrance.jpg" at topleft
    call screen day5_depot_investigation
    $ clicked_object = _return

    if clicked_object not in day5_clicked_points:
        $ day5_clicked_points.append(clicked_object)

    if clicked_object == "arthur":
        show expression "gui/day5_abandoned_station/Depot_Entrance/Arthur_Day5.png" at topleft
        arthur "Morning! Word is a getaway driver from last night's chaos was dumped here in bad shape."
        arthur "Then the rival gang came here to finish the job, to hit them when their weak but it looks like the robbers ran off"
        jump day5_investigation_hub

    elif clicked_object == "tourist":
        show expression "gui/day5_abandoned_station/Depot_Entrance/Tourist.png" at topleft
        tourist "I didn't know this town would be this active!"
        tourist "I've been snapping photos all morning! I'm pretty sure they were just filming a zombie action movie here with fake blood."
        if "Tourist 1" not in day5_witnesses_found:
            $ day5_witnesses_found.append("Tourist 1")
        jump day5_investigation_hub

    elif clicked_object == "go_to_maintenance_bay":
        "(Let's check out the maintenance bay.)"
        jump day5_maintenance_bay_hub

    elif clicked_object == "go_to_abandoned_tracks":
        "(Let's head over to the abandoned tracks.)"
        jump day5_abandoned_tracks_hub

    elif clicked_object == "go_to_triage":
        "(Looks like a makeshift medical area over there. Let's check it out.)"
        jump day5_triage_hub

    elif clicked_object == "newsroom":
        jump day5_morning_newspaper


# ==========================================
# AREA 1: MAINTENANCE BAY
# ==========================================
label day5_maintenance_bay_hub:
    if "The Rusty Toolbox" not in inventory_bag_items:
        scene expression "gui/day5_abandoned_station/Maintenance_Bay/bg Maintenance_Bay_Toolbox.jpg" at topleft
    else:
        scene expression "gui/day5_abandoned_station/Maintenance_Bay/bg Maintenance_Bay_NoToolbox.jpg" at topleft

    call screen day5_maintenance_bay_environment
    $ clicked_object = _return

    if clicked_object not in day5_clicked_points:
        $ day5_clicked_points.append(clicked_object)

    if clicked_object == "engineer":
        show expression "gui/day5_abandoned_station/Maintenance_Bay/Train_Engineer.png" at topleft
        engineer "Nothing mysterious about it. That driver just fell off a moving cargo train."
        engineer "I was working on the tracks when I saw him fall."
        if "Train Engineer 1" not in day5_witnesses_found:
            $ day5_witnesses_found.append("Train Engineer 1")
        jump day5_maintenance_bay_hub

    elif clicked_object == "toolbox":
        "Heavy junk left behind by a mechanic."
        if "The Rusty Toolbox" not in day5_items_found:
            $ day5_items_found.append("The Rusty Toolbox")
        if "The Rusty Toolbox" not in inventory_bag_items:
            $ inventory_bag_items.append("The Rusty Toolbox")
        jump day5_maintenance_bay_hub

    elif clicked_object == "go_to_oilleak_closeup":
        "(Looks like there's a dark puddle leaking on the floor over there.)"
        
        jump day5_oilleak_closeup_hub

    elif clicked_object == "depot_entrance":
        jump day5_investigation_hub

label day5_oilleak_closeup_hub:
    scene expression "gui/day5_abandoned_station/Maintenance_Bay/Oil_Leak_CloseUp.jpg" at topleft
    if "The Leaking Oil Puddle" not in day5_clues_found:
        $ day5_clues_found.append("The Leaking Oil Puddle")
    "Looks like normal car trouble"
    "Wait, what is that red drop beside the puddle?"
    call screen day5_oilleak_closeup_environment
    jump day5_maintenance_bay_hub


# ==========================================
# AREA 2: ABANDONED TRACKS
# ==========================================
label day5_abandoned_tracks_hub:
    if "The Empty Wallet" not in inventory_bag_items:
        scene expression "gui/day5_abandoned_station/Abandoned_Tracks/bg Abandoned_Tracks_Wallet.jpg" at topleft
    else:
        scene expression "gui/day5_abandoned_station/Abandoned_Tracks/bg Abandoned_Tracks_NoWallet.jpg" at topleft

    call screen day5_abandoned_tracks_environment
    $ clicked_object = _return

    if clicked_object not in day5_clicked_points:
        $ day5_clicked_points.append(clicked_object)

    if clicked_object == "hobo":
        show expression "gui/day5_abandoned_station/Abandoned_Tracks/Homeless_Man_Idle.png" at topleft
        hobo "Wake up! The government is poisoning the water supply!"
        hobo "I drank from a rusty faucet and my stomach hurt ALL WEEK"
        if "Hobo 1" not in day5_witnesses_found:
            $ day5_witnesses_found.append("Hobo 1")
        jump day5_abandoned_tracks_hub

    elif clicked_object == "go_to_tracks_closeup":
        "(Looks like there are some tracks on the ground near the rails.)"
        jump day5_tracks_closeup_hub

    elif clicked_object == "go_to_grass_closeup":
        if "The Empty Wallet" not in inventory_bag_items:
            "(Looks like there's something on the grass.)"
        else:
            "(Nothing else left in the grass.)"
        jump day5_grass_closeup_hub

    elif clicked_object == "depot_entrance":
        jump day5_investigation_hub

label day5_tracks_closeup_hub:
    scene expression "gui/day5_abandoned_station/Abandoned_Tracks/Tracks_CloseUp.jpg" at topleft
    call screen day5_tracks_closeup_environment
    $ clicked_object = _return

    if clicked_object == "tiretracks":
        "Bloody tire tracks. They show the exact escape route of the ambushed gangsters."
        if "The Bloody Tire Tracks" not in day5_clues_found:
            $ day5_clues_found.append("The Bloody Tire Tracks")
        jump day5_tracks_closeup_hub

    elif clicked_object == "dogtracks":
        "Wild dog tracks. Maybe they are drawn to the smell of blood."
        "Or they just went for a hunt and stumbled here accidentaly"
        if "The Wild Dog Tracks" not in day5_clues_found:
            $ day5_clues_found.append("The Wild Dog Tracks")
        jump day5_tracks_closeup_hub

    elif clicked_object == "back":
        jump day5_abandoned_tracks_hub

label day5_grass_closeup_hub:
    scene expression "gui/day5_abandoned_station/Abandoned_Tracks/Grass_CloseUp_NoWallet.jpg" at topleft
    call screen day5_grass_closeup_environment
    $ clicked_object = _return

    if clicked_object == "wallet":
        "An empty wallet. Could this belong to a pickpocket?"
        if "The Empty Wallet" not in day5_items_found:
            $ day5_items_found.append("The Empty Wallet")
        if "The Empty Wallet" not in inventory_bag_items:
            $ inventory_bag_items.append("The Empty Wallet")
        jump day5_grass_closeup_hub

    elif clicked_object == "back":
        jump day5_abandoned_tracks_hub


# ==========================================
# AREA 3: MAKESHIFT TRIAGE & TENT
# ==========================================
label day5_triage_hub:
    if "The Burner Phone" not in inventory_bag_items and not evidence_phone:
        scene expression "gui/day5_abandoned_station/Triage/bg Makeshift_Triage_Phone.jpg" at topleft
    else:
        scene expression "gui/day5_abandoned_station/Triage/bg Makeshift_Triage_NoPhone.jpg" at topleft

    call screen day5_triage_environment
    $ clicked_object = _return

    if clicked_object not in day5_clicked_points:
        $ day5_clicked_points.append(clicked_object)

    if clicked_object == "medic":
        show expression "gui/day5_abandoned_station/Triage/Medic.png" at topleft
        medic "They forced me at gunpoint to treat a wounded gangster! He kept muttering about how they're gonna get revenge on the shipping docks!"
        if "Medic 1" not in day5_witnesses_found:
            $ day5_witnesses_found.append("Medic 1")
        jump day5_triage_hub

    elif clicked_object == "go_to_crate_closeup":
        if "The Burner Phone" not in inventory_bag_items and not evidence_phone:
            "(Looks like there's something dropped near the medical crates.)"
        else:
            "(Nothing else near the medical supplies.)"
        jump day5_crate_closeup_hub

    elif clicked_object == "go_to_tent":
        "(Looks like the wounded driver was treated inside this tent. Let's take a look inside.)"
        jump day5_triage_tent_hub

    elif clicked_object == "depot_entrance":
        jump day5_investigation_hub

label day5_crate_closeup_hub:
    scene expression "gui/day5_abandoned_station/Triage/Crate_CloseUp_NoPhone.jpg" at topleft
    call screen day5_crate_closeup_environment
    $ clicked_object = _return

    if clicked_object == "phone":
        "A cheap burner phone dropped near the medical supplies. The messages confirm there will be a massive gang war at midnight!"
        $ evidence_phone = True
        if "The Burner Phone" not in inventory_bag_items:
            $ inventory_bag_items.append("The Burner Phone")
        jump day5_crate_closeup_hub

    elif clicked_object == "back":
        jump day5_triage_hub

label day5_triage_tent_hub:
    if "The Train Ticket Stub" not in inventory_bag_items:
        scene expression "gui/day5_abandoned_station/Triage/Tent/bg Inside_Tent_Ticket.jpg" at topleft
    else:
        scene expression "gui/day5_abandoned_station/Triage/Tent/bg Inside_Tent_NoTicket.jpg" at topleft

    call screen day5_triage_tent_environment
    $ clicked_object = _return

    if clicked_object == "go_to_coat_closeup":
        if "The Train Ticket Stub" not in inventory_bag_items:
            "(Looks like there's something sticking out of the driver's coat pocket.)"
        else:
            "(Nothing else left in the coat pocket.)"
        jump day5_coat_closeup_hub

    elif clicked_object == "back_to_triage":
        jump day5_triage_hub

label day5_coat_closeup_hub:
    scene expression "gui/day5_abandoned_station/Triage/Tent/Coat_CloseUp_NoTicket.jpg" at topleft
    call screen day5_coat_closeup_environment
    $ clicked_object = _return

    if clicked_object == "ticketstub":
        "This is a Train Ticket Stub in the injured driver's pocket. Looks like they we're planning to leave town until they got ambushed by the rival gang"
        if "The Train Ticket Stub" not in day5_items_found:
            $ day5_items_found.append("The Train Ticket Stub")
        if "The Train Ticket Stub" not in inventory_bag_items:
            $ inventory_bag_items.append("The Train Ticket Stub")
        jump day5_coat_closeup_hub

    elif clicked_object == "back":
        jump day5_triage_tent_hub


# ==========================================
# NEWSPAPER MINIGAME & API EXECUTION
# ==========================================
label day5_morning_newspaper:
    hide screen global_hud
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
       
    scene desk_newspaper
    "Let's see how the final story turned out..."
    
    call screen newspaper_results_ui(daily_headline, daily_body, daily_rating, total_credibility_score)
    
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