# ==============================================================================
# GLOBAL AUDIO CHANNELS & UI HOOKS (Shared across all days)
# ==============================================================================
init -10 python:
    # Dedicated looping channel for environmental room tones & weather
    renpy.music.register_channel("ambient", mixer="sfx", loop=True, tight=True)
    # Dedicated one-shot channel for musical stings & jingles so SFX never cut them off
    renpy.music.register_channel("sting", mixer="sfx", loop=False)

init 10:
    # Title screen music & global dialogue choice button UI sounds
    define config.main_menu_music = "audio/bgm_main_menu.ogg"
    style choice_button:
        hover_sound "audio/ui_hover.ogg"
        activate_sound "audio/ui_click.ogg"

init 999 python:
    # Automatically plays ui_notify.ogg whenever renpy.notify() or Notify() triggers
    _scoop_default_notify = config.notify
    def _scoop_audio_notify(message):
        renpy.play("audio/ui_notify.ogg", channel="audio")
        return _scoop_default_notify(message)
    config.notify = _scoop_audio_notify

# ==============================================================================
# DAY 1 ASSETS & VARIABLES
# ==============================================================================
image bg warehouse = im.Scale("gui/warehouse/warehouse_front.png", 1920, 1072)
image bg warehouse_back = im.Scale("gui/warehouse/bg_warehouse_back.png", 1920, 1072)
image bg warehouse_office = im.Scale("gui/day1_office/bg_office.png", 1920, 1072)
image bg warehouse_office_empty = im.Scale("gui/day1_office/bg_office_empty.png", 1920, 1072)
image bg empty_drawer = im.Scale("gui/day1_office/drawer/bg_empty_drawer.jpg", 1920, 1072)
image bg inside_warehouse = im.Scale("gui/day1_inside_warehouse/bg_inside_warehouse.png", 1920, 1072)
image bg tower_warehouse = im.Scale("gui/day_tower_warehouse/bg_tower_warehouse.png", 1920, 1072)
image bg garage_back_warehouse = im.Scale("gui/day1_garage_warehouse/bg_garage_warehouse.png", 1920, 1072)
image bg riverclose = im.Scale("gui/day1_back_warehouse/bg_riverclose.png", 1920, 1072)
image desk_newspaper = im.Scale("gui/desk_newspaper.jpg", 1920, 1080)
image newsroom1 = "gui/newsroom_scenes/Day1_Scene1.jpg"
image newsroom2 = "gui/newsroom_scenes/Day1_Scene2.jpg"
image news_creation = "gui/newsroom_scenes/Newspaper_Making.jpg"

define kenneth = Character("Editor Kenneth", color="#b30000")
define arthur = Character("Arthur", color="#ff9900")
define watchman = Character("Watchman", color="#cccccc")
define fisherman = Character("Fisherman", color="#cccccc")
define driver = Character("Delivery Driver", color="#cccccc")
define jogger = Character("Jogger", color="#cccccc")
define janitor = Character("Janitor", color="#cccccc")

default day1_clue = ""
default day1_item = ""
default day1_witness = ""

# Progression Variables
default evidence_lighter = False
default battery_obtained = False
default office_empty = False
default janitor_spoken_to = False
default janitor_helped = False
default paint_cleared = False
default whiskey_cleared = False
default pizza_cleared = False
default day1_clues_found = []
default day1_items_found = []
default day1_witnesses_found = []
default day1_clicked_points = []
default inventory_bag_items = []

# ==============================================================================
# STAGE SELECT & DAY 1 BRIEFING
# ==============================================================================
label stage1_briefing:
    $ current_day = 1
    scene bg newsroom
    play music "audio/bgm_main_menu.ogg" fadeout 1.0 fadein 1.0 volume 0.60 if_changed
    play ambient "audio/amb_newsroom.ogg" fadeout 1.0 fadein 1.0 volume 0.35 if_changed

    menu:
        "Tutorial":
            jump tutorial_start
        "Day 1":
            jump day1_path
        "Day 2":
            jump day2_start
        "Day 3":
            jump day3_start
        "Day 4":
            jump day4_start
        "Day 5":
            jump day5_path_a_start

label day1_path:
    play sting "audio/sting_day_transition.ogg" volume 0.75
    play music "audio/bgm_newsroom.ogg" fadeout 1.0 fadein 1.5 volume 0.55 if_changed
    play ambient "audio/amb_newsroom.ogg" fadeout 0.8 fadein 1.0 volume 0.40 if_changed

    scene bg newsroom
    scene newsroom1 with dissolve
    kenneth "{cps=28}Listen up, rookie. I don't want you digging into the rising crime rate. That's an order.{/cps}{w=2.5}{nw}"
    kenneth "{cps=28}Head down to the riverside shipping warehouse. Someone vandalized it. Get a simple quote and come back.{/cps}{w=2.5}{nw}"

    scene newsroom2 with dissolve
    arthur "{cps=28}Stay out of my way rookie! this is my story{/cps}{w=2.5}{nw}"

    play sound "audio/sfx_footsteps_move.ogg"
    jump day1_investigation_hub

# ==============================================================================
# DAY 1 WAREHOUSE EXTERIOR (FRONT HUB)
# ==============================================================================
label day1_investigation_hub:
    scene bg warehouse
    play music "audio/bgm_day1_warehouse.ogg" fadeout 1.0 fadein 1.2 volume 0.55 if_changed
    play ambient "audio/amb_warehouse_ext.ogg" fadeout 0.8 fadein 1.0 volume 0.45 if_changed

    call screen day1_warehouse_investigation
    $ clicked_object = _return

    show screen day1_warehouse_investigation

    if clicked_object == "lighter":
        play sound "audio/sfx_pickup_item.ogg"
        "It's a Brass Lighter engraved with a skull and crossed wrenches."
        play sting "audio/sting_clue_major.ogg" volume 0.75
        "I feel like i've seen this symbol before..."
        $ evidence_lighter = True
        if "The Brass Lighter" not in inventory_bag_items:
            $ inventory_bag_items.append("The Brass Lighter")
            $ renpy.notify("You got The Brass Lighter.")
        hide screen day1_warehouse_investigation
        jump day1_investigation_hub

    elif clicked_object == "watchman":
        if "Watchman 1" not in day1_witnesses_found:
            play sound "audio/ui_notepad_flip.ogg"
        watchman "I saw them... men in heavy leather jackets marking the warehouse as their territory."
        watchman "I didn't stop them because I was scared."
        watchman "I'm just a 'WATCH'man after all."
        if "Watchman 1" not in day1_witnesses_found:
            $ day1_witnesses_found.append("Watchman 1")
        hide screen day1_warehouse_investigation
        jump day1_investigation_hub

    elif clicked_object == "warehouse_graffiti":
        play sound "audio/sfx_camera_shutter.ogg"
        "The graffiti looks fresh. Someone wanted to mark this place as their territory."
        "Or their just incredibly artistic vandals. Either way, this is a crime scene."
        hide screen day1_warehouse_investigation
        jump day1_investigation_hub

    elif clicked_object == "warehouse_windows":
        play sound "audio/sfx_camera_shutter.ogg"
        "They destroyed even the warehouse windows."
        "I guess they are violent artists."
        "Or just violent."
        hide screen day1_warehouse_investigation
        jump day1_investigation_hub

    elif clicked_object == "warehouse_door":
        play sound "audio/sfx_door_open.ogg"
        hide screen day1_warehouse_investigation
        jump day1_warehouse_inside

    elif clicked_object == "warehouse_tower":
        play sound "audio/sfx_footsteps_move.ogg"
        hide screen day1_warehouse_investigation
        jump day1_warehouse_tower

    elif clicked_object == "warehouse_back":
        play sound "audio/sfx_footsteps_move.ogg"
        hide screen day1_warehouse_investigation
        jump day1_warehouse_back

    elif clicked_object == "warehouse_office":
        play sound "audio/sfx_door_open.ogg"
        hide screen day1_warehouse_investigation
        jump day1_warehouse_office

    elif clicked_object == "newsroom":
        play sound "audio/sfx_van_door.ogg"
        hide screen day1_warehouse_investigation
        jump day1_newspaper_minigame

    else:
        hide screen day1_warehouse_investigation
        jump day1_investigation_hub

# ==============================================================================
# DAY 1 WAREHOUSE BACK & RIVER CLOSE-UP
# ==============================================================================
label day1_warehouse_back:
    scene bg warehouse_back
    play music "audio/bgm_day1_warehouse.ogg" fadeout 1.0 fadein 1.0 volume 0.55 if_changed
    play ambient "audio/amb_warehouse_ext.ogg" fadeout 0.8 fadein 0.8 volume 0.45 if_changed

    call screen day1_warehouse_back_environment
    $ clicked_object = _return

    show screen day1_warehouse_back_environment

    if clicked_object == "fisherman":
        if "Fisherman 1" not in day1_witnesses_found:
            play sound "audio/ui_notepad_flip.ogg"
        fisherman "I swear, the warehouse was attacked by angry teenagers!"
        fisherman "I saw them spray painting the walls and smashing the windows."
        fisherman "I think..."
        if "Fisherman 1" not in day1_witnesses_found:
            $ day1_witnesses_found.append("Fisherman 1")
        hide screen day1_warehouse_back_environment
        jump day1_warehouse_back

    elif clicked_object == "river":
        play sound "audio/sfx_footsteps_move.ogg"
        hide screen day1_warehouse_back_environment
        jump day1_warehouse_riverclose

    elif clicked_object == "return_to_back":
        play sound "audio/ui_cancel.ogg"
        hide screen day1_warehouse_back_environment
        jump day1_warehouse_back

    elif clicked_object == "collar":
        play sound "audio/sfx_pickup_item.ogg"
        "A Lost Dog Collar lies in the dirt."
        "I wonder if it belongs to a dog that was here during the vandalism."
        if "The Lost Dog Collar" not in day1_items_found:
            $ day1_items_found.append("The Lost Dog Collar")
            $ inventory_bag_items.append("The Lost Dog Collar")
        hide screen day1_warehouse_back_environment
        jump day1_warehouse_back

    elif clicked_object == "warehouse_inside_from_the_back":
        play sound "audio/sfx_door_open.ogg"
        hide screen day1_warehouse_back_environment
        jump day1_warehouse_inside_from_the_back

    elif clicked_object == "garage_back_warehouse":
        play sound "audio/sfx_door_open.ogg"
        hide screen day1_warehouse_back_environment
        jump day1_warehouse_garage_back

    elif clicked_object == "back_to_front":
        play sound "audio/sfx_footsteps_move.ogg"
        hide screen day1_warehouse_back_environment
        scene bg warehouse
        jump day1_investigation_hub

    else:
        hide screen day1_warehouse_back_environment
        jump day1_warehouse_back

label day1_warehouse_riverclose:
    scene bg riverclose
    play music "audio/bgm_day1_warehouse.ogg" fadeout 1.0 fadein 1.0 volume 0.55 if_changed
    play ambient "audio/amb_river_closeup.ogg" fadeout 0.8 fadein 0.8 volume 0.55 if_changed

    call screen day1_warehouse_riverclose_environment
    $ clicked_object = _return

    show screen day1_warehouse_riverclose_environment

    if clicked_object == "watch":
        play sound "audio/sfx_water_splash.ogg"
        "There's a Broken Pocket Watch in the water."
        "Talk about the 'flow' of time."
        "hehe..."
        if "The Broken Pocket Watch" not in day1_items_found:
            $ day1_items_found.append("The Broken Pocket Watch")
        if "The Broken Pocket Watch" not in inventory_bag_items:
            $ inventory_bag_items.append("The Broken Pocket Watch")
        hide screen day1_warehouse_riverclose_environment
        jump day1_warehouse_riverclose

    elif clicked_object == "return_to_back":
        play sound "audio/ui_cancel.ogg"
        hide screen day1_warehouse_riverclose_environment
        jump day1_warehouse_back

    else:
        hide screen day1_warehouse_riverclose_environment
        jump day1_warehouse_riverclose

# ---------------------------------------------
# JANITOR TRASH LOGIC (Inside Warehouse)
# ---------------------------------------------
label day1_warehouse_inside_from_the_back:
    scene bg inside_warehouse
    play music "audio/bgm_day1_warehouse.ogg" fadeout 1.0 fadein 1.0 volume 0.50 if_changed
    play ambient "audio/amb_warehouse_int.ogg" fadeout 0.8 fadein 0.8 volume 0.45 if_changed

    call screen day1_warehouse_inside_back_environment
    $ clicked_object = _return

    show screen day1_warehouse_inside_back_environment

    if clicked_object == "janitor":
        if paint_cleared and pizza_cleared and whiskey_cleared:
            if not janitor_helped:
                janitor "I am shocked! You cleaned up all this trash!"
                janitor "Since you're so good at this, do you want to help me clean up the rest of the warehouse?"
                menu:
                    "Yes":
                        janitor "Thank you so much! Here's my keyring, go find my cleaning tools in the other rooms."
                        play sound "audio/sfx_keys_jingle.ogg"
                        $ renpy.notify("You obtained a keyring.")
                        $ inventory_bag_items.append("The Janitor's Keyring")
                        $ janitor_helped = True
                    "No":
                        janitor "Alright, but you can come help me anytime."
            else:
                "The janitor is busy cleaning."
        else:
            if not janitor_spoken_to:
                janitor "This building is a mess. I don't know how I would clean this up all by myself."
                janitor "I don't get paid enough to clean up after vandals."
                $ janitor_spoken_to = True
            else:
                janitor "There's still so much trash everywhere..."
        hide screen day1_warehouse_inside_back_environment
        jump day1_warehouse_inside_from_the_back

    elif clicked_object == "whiskey":
        if "The Broken Whiskey Bottle" not in day1_clues_found:
            play sound "audio/ui_notepad_flip.ogg"
            $ day1_clues_found.append("The Broken Whiskey Bottle")
        "Just a cheap bottle left by a homeless person."
        if janitor_spoken_to:
            menu:
                "Throw it away":
                    play sound "audio/sfx_trash_glass.ogg"
                    $ whiskey_cleared = True
                    "I threw the bottle in the trash."
                "Leave it alone":
                    pass
        hide screen day1_warehouse_inside_back_environment
        jump day1_warehouse_inside_from_the_back

    elif clicked_object == "pizza":
        if "The Torn Pizza Box" not in day1_clues_found:
            play sound "audio/ui_notepad_flip.ogg"
            $ day1_clues_found.append("The Torn Pizza Box")
        "Empty food boxes scattered around."
        if janitor_spoken_to:
            menu:
                "Throw it away":
                    play sound "audio/sfx_trash_cardboard.ogg"
                    $ pizza_cleared = True
                    "I threw the boxes in the trash."
                "Leave it alone":
                    pass
        hide screen day1_warehouse_inside_back_environment
        jump day1_warehouse_inside_from_the_back

    elif clicked_object == "paint_can":
        if "The Smashed Paint Can" not in day1_clues_found:
            play sound "audio/ui_notepad_flip.ogg"
            $ day1_clues_found.append("The Smashed Paint Can")
        "It smells like industrial-grade spray paint. Proof of a coordinated, planned job."
        if janitor_spoken_to:
            menu:
                "Throw it away":
                    play sound "audio/sfx_trash_metal.ogg"
                    $ paint_cleared = True
                    "I tossed the paint can."
                "Leave it alone":
                    pass
        hide screen day1_warehouse_inside_back_environment
        jump day1_warehouse_inside_from_the_back

    elif clicked_object == "return_to_back":
        play sound "audio/sfx_door_open.ogg"
        hide screen day1_warehouse_inside_back_environment
        jump day1_warehouse_back

    elif clicked_object == "return_to_front":
        play sound "audio/sfx_door_open.ogg"
        hide screen day1_warehouse_inside_back_environment
        scene bg warehouse
        jump day1_investigation_hub

    else:
        hide screen day1_warehouse_inside_back_environment
        jump day1_warehouse_inside_from_the_back

label day1_warehouse_inside:
    scene bg inside_warehouse
    play music "audio/bgm_day1_warehouse.ogg" fadeout 1.0 fadein 1.0 volume 0.50 if_changed
    play ambient "audio/amb_warehouse_int.ogg" fadeout 0.8 fadein 0.8 volume 0.45 if_changed

    call screen day1_warehouse_inside_front_environment
    $ clicked_object = _return

    show screen day1_warehouse_inside_front_environment

    if clicked_object == "janitor":
        if paint_cleared and pizza_cleared and whiskey_cleared:
            if not janitor_helped:
                janitor "I am shocked! You cleaned up all this trash!"
                janitor "Since you're so good at this, do you want to help me clean up the rest of the warehouse?"
                menu:
                    "Yes":
                        janitor "Thank you so much! Here's my keyring, go find my cleaning tools in the other rooms."
                        play sound "audio/sfx_keys_jingle.ogg"
                        $ renpy.notify("You obtained a keyring.")
                        $ inventory_bag_items.append("The Janitor's Keyring")
                        $ janitor_helped = True
                    "No":
                        janitor "Alright, but you can come help me anytime."
            else:
                "The janitor is busy cleaning."
        else:
            if not janitor_spoken_to:
                janitor "This building is a mess. I don't know how I would clean this up all by myself."
                janitor "I don't get paid enough to clean up after vandals."
                $ janitor_spoken_to = True
            else:
                janitor "There's still so much trash everywhere..."
        hide screen day1_warehouse_inside_front_environment
        jump day1_warehouse_inside

    elif clicked_object == "whiskey":
        if "The Broken Whiskey Bottle" not in day1_clues_found:
            play sound "audio/ui_notepad_flip.ogg"
            $ day1_clues_found.append("The Broken Whiskey Bottle")
        "Just a cheap bottle left by a homeless person."
        if janitor_spoken_to:
            menu:
                "Throw it away":
                    play sound "audio/sfx_trash_glass.ogg"
                    $ whiskey_cleared = True
                    "I threw the bottle in the trash."
                "Leave it alone":
                    pass
        hide screen day1_warehouse_inside_front_environment
        jump day1_warehouse_inside

    elif clicked_object == "pizza":
        if "The Torn Pizza Box" not in day1_clues_found:
            play sound "audio/ui_notepad_flip.ogg"
            $ day1_clues_found.append("The Torn Pizza Box")
        "Empty food boxes scattered around."
        if janitor_spoken_to:
            menu:
                "Throw it away":
                    play sound "audio/sfx_trash_cardboard.ogg"
                    $ pizza_cleared = True
                    "I threw the boxes in the trash."
                "Leave it alone":
                    pass
        hide screen day1_warehouse_inside_front_environment
        jump day1_warehouse_inside

    elif clicked_object == "paint_can":
        if "The Smashed Paint Can" not in day1_clues_found:
            play sound "audio/ui_notepad_flip.ogg"
            $ day1_clues_found.append("The Smashed Paint Can")
        "It smells like industrial-grade spray paint. Proof of a coordinated, planned job."
        if janitor_spoken_to:
            menu:
                "Throw it away":
                    play sound "audio/sfx_trash_metal.ogg"
                    $ paint_cleared = True
                    "I tossed the paint can."
                "Leave it alone":
                    pass
        hide screen day1_warehouse_inside_front_environment
        jump day1_warehouse_inside

    elif clicked_object == "return_to_front":
        play sound "audio/sfx_door_open.ogg"
        hide screen day1_warehouse_inside_front_environment
        scene bg warehouse
        jump day1_investigation_hub

    else:
        hide screen day1_warehouse_inside_front_environment
        jump day1_warehouse_inside

# ==============================================================================
# DAY 1 GARAGE, TOWER & WAREHOUSE OFFICE
# ==============================================================================
label day1_warehouse_garage_back:
    scene bg garage_back_warehouse
    play music "audio/bgm_day1_warehouse.ogg" fadeout 1.0 fadein 1.0 volume 0.50 if_changed
    play ambient "audio/amb_warehouse_int.ogg" fadeout 0.8 fadein 0.8 volume 0.45 if_changed

    call screen day1_warehouse_garage_environment
    $ clicked_object = _return

    show screen day1_warehouse_garage_environment

    if clicked_object == "battery_charger":
        play sound "audio/sfx_flashlight_click.ogg"
        "The battery charger is still plugged in. Maybe it can power something useful."
        hide screen day1_warehouse_garage_environment
        jump day1_warehouse_garage_back

    elif clicked_object == "garage_boxes":
        play sound "audio/sfx_trash_cardboard.ogg"
        "Crates and shipping boxes are stacked against the wall."
        "Someone was moving equipment in a hurry."
        hide screen day1_warehouse_garage_environment
        jump day1_warehouse_garage_back

    elif clicked_object == "garage_driver":
        if "Delivery Driver 1" not in day1_witnesses_found:
            play sound "audio/ui_notepad_flip.ogg"
            $ day1_witnesses_found.append("Delivery Driver 1")
        driver "It was a rival shipping company trying to steal business."
        driver "Nobody plays fair in this town. I don't know why I even bother."
        hide screen day1_warehouse_garage_environment
        jump day1_warehouse_garage_back

    elif clicked_object == "garage_clipboard":
        play sound "audio/sfx_paper_rustle.ogg"
        "There are notes on the clipboard about deliveries and damaged cargo."
        hide screen day1_warehouse_garage_environment
        jump day1_warehouse_garage_back

    elif clicked_object == "garage_office":
        play sound "audio/sfx_drawer_locked.ogg"
        "The office was kept locked up tight. Someone was hiding something in here."
        hide screen day1_warehouse_garage_environment
        jump day1_warehouse_garage_back

    elif clicked_object == "return_to_back":
        play sound "audio/sfx_door_open.ogg"
        hide screen day1_warehouse_garage_environment
        jump day1_warehouse_back

    elif clicked_object == "return_to_front":
        play sound "audio/sfx_footsteps_move.ogg"
        hide screen day1_warehouse_garage_environment
        scene bg warehouse
        jump day1_investigation_hub

    else:
        hide screen day1_warehouse_garage_environment
        jump day1_warehouse_garage_back

label day1_warehouse_tower:
    scene bg tower_warehouse
    play music "audio/bgm_day1_warehouse.ogg" fadeout 1.0 fadein 1.0 volume 0.55 if_changed
    play ambient "audio/amb_warehouse_ext.ogg" fadeout 0.8 fadein 0.8 volume 0.45 if_changed

    call screen day1_warehouse_tower_environment
    $ clicked_object = _return

    show screen day1_warehouse_tower_environment

    if clicked_object == "jogger":
        if "Jogger 1" not in day1_witnesses_found:
            play sound "audio/ui_notepad_flip.ogg"
        jogger "I saw a glowing ghost damage the walls!"
        jogger "That place always creeped me out. I don't know why I even jog here."
        jogger "I think it's time I find a new route for my morning jogs."
        if "Jogger 1" not in day1_witnesses_found:
            $ day1_witnesses_found.append("Jogger 1")
        hide screen day1_warehouse_tower_environment
        jump day1_warehouse_tower

    elif clicked_object == "Battery":
        play sound "audio/sfx_flashlight_click.ogg"
        "I see a battery that can be removed."
        "This can power something... I should take it."
        hide screen day1_warehouse_tower_environment
        jump day1_warehouse_tower

    elif clicked_object == "return_to_front":
        play sound "audio/sfx_footsteps_move.ogg"
        hide screen day1_warehouse_tower_environment
        scene bg warehouse
        jump day1_investigation_hub

    else:
        play sound "audio/sfx_footsteps_move.ogg"
        hide screen day1_warehouse_tower_environment
        scene bg warehouse
        jump day1_investigation_hub

label day1_get_battery:
    play sound "audio/sfx_flashlight_click.ogg"
    "You got a battery."
    if "Battery" not in inventory_bag_items:
        $ inventory_bag_items.append("Battery")
    return

label day1_warehouse_office:
    if office_empty:
        scene bg warehouse_office_empty
    else:
        scene bg warehouse_office

    play music "audio/bgm_day1_warehouse.ogg" fadeout 1.0 fadein 1.0 volume 0.50 if_changed
    play ambient "audio/amb_warehouse_int.ogg" fadeout 0.8 fadein 0.8 volume 0.40 if_changed

    call screen day1_warehouse_office_environment
    $ clicked_object = _return

    show screen day1_warehouse_office_environment

    if clicked_object == "drawer2":
        if office_empty:
            if "The Janitor's Keyring" in inventory_bag_items:
                menu:
                    "Use the drawer key":
                        play sound "audio/sfx_drawer_unlock.ogg"
                        "The key fits. The drawer unlocks."
                        $ inventory_bag_items.remove("The Janitor's Keyring")
                        hide screen day1_warehouse_office_environment
                        scene bg empty_drawer
                        "This drawer is empty."
                        "I thought I saw something. This is the drawer for the warehouse's blueprints."
                        play sting "audio/sting_clue_major.ogg" volume 0.75
                        "Unless it was also stolen by the vandals."
                        if "Missing blueprint" not in day1_items_found:
                            $ day1_items_found.append("Missing blueprint")
                            $ renpy.notify("You found a clue: Missing blueprint.")
                    "I leave the drawer closed for now.":
                        pass
            else:
                menu:
                    "Try to open the drawer":
                        play sound "audio/sfx_drawer_locked.ogg"
                        "It's locked. I need a key."
                    "Leave the drawer alone":
                        "I should come back with a key."
        else:
            "I should wait until the office is empty to open the drawer."
        hide screen day1_warehouse_office_environment
        jump day1_warehouse_office

    elif clicked_object == "officerguy":
        if "Battery" in inventory_bag_items:
            play sound "audio/sfx_flashlight_click.ogg"
            "My equipment just arrived. I can use this battery."
            $ inventory_bag_items.remove("Battery")
            "I'll go to the restroom while it gets set up."
            play sound "audio/sfx_door_open.ogg"
            $ office_empty = True
        else:
            "My parcel or my equipment just arrived. I need a battery."
        hide screen day1_warehouse_office_environment
        jump day1_warehouse_office

    elif clicked_object == "return_to_front":
        play sound "audio/sfx_door_open.ogg"
        hide screen day1_warehouse_office_environment
        scene bg warehouse
        jump day1_investigation_hub

    else:
        play sound "audio/sfx_door_open.ogg"
        hide screen day1_warehouse_office_environment
        scene bg warehouse
        jump day1_investigation_hub

# ==============================================================================
# DAY 1 NEWSPAPER MINIGAME & EDITION RESULTS
# ==============================================================================
label day1_newspaper_minigame:
    $ hide_all_investigation_screens()
    play sound "audio/sfx_typewriter_write.ogg"
    play music "audio/bgm_newsroom.ogg" fadeout 1.0 fadein 1.2 volume 0.55 if_changed
    play ambient "audio/amb_newsroom.ogg" fadeout 1.0 fadein 1.0 volume 0.35 if_changed

    scene news_creation with dissolve
    "Time to review my Reporter's Notepad and write the evening edition."

label select_day1_clue:
    play sound "audio/ui_notepad_flip.ogg"
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
    play sound "audio/ui_notepad_flip.ogg"
    "What was the most credible object I gathered at the warehouse?"
    menu:
        "Missing blueprint" if "Missing blueprint" in day1_items_found:
            "Description: Unlocks restricted offices containing vandalized blueprints."
            menu:
                "Confirm this choice":
                    $ day1_item = "Missing blueprint"
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
    play sound "audio/ui_notepad_flip.ogg"
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
        article_result = sheetdb_client.fetch_newspaper_article(day1_clue, day1_item, day1_witness, "day1")
        daily_headline = article_result.get("headline", "Error: Story Not Found")
        daily_body = article_result.get("body", "Error: Check database connection.")
        day1_accurate_picks = (
            (day1_clue == "The Smashed Paint Can")
            + (day1_item == "Missing blueprint")
            + (day1_witness == "Watchman 1")
        )

    # Show the wide desk shot first
    scene desk_newspaper
    play sound "audio/sfx_newspaper_print.ogg"
    "Let's see how the morning edition turned out..."

    # Play high or low credibility sting when the zoomed newspaper opens
    if day1_accurate_picks >= 2:
        play sting "audio/sting_rating_high.ogg" volume 0.80
    else:
        play sting "audio/sting_rating_low.ogg" volume 0.80

    # Call the zoomed-in UI screen and pass it the variables
    call screen newspaper_results_ui(daily_headline, daily_body, daily_rating, total_credibility_score)
    play sound "audio/sfx_paper_rustle.ogg"
    $ renpy.force_autosave(True)
    jump day2_start