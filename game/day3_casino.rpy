# ==========================================
# DAY 3 IMAGES
# ==========================================
image bg casino_outside = im.Scale("gui/day3_casino/outside_casino/bg_Casino_Outside.jpg", 1920, 1080)
image bg club_front = im.Scale("gui/day3_casino/local_club/bg_Front_Door_Club.jpg", 1920, 1080)
image bg club_inside = im.Scale("gui/day3_casino/local_club/inside_club/bg_Club_Room.jpg", 1920, 1080)
image bg casino_lobby = im.Scale("gui/day3_casino/casino_lobby/bg_Casino_Lobby.jpg", 1920, 1080)
image bg cashier_closeup = im.Scale("gui/day3_casino/casino_lobby/cashier_closeup.jpg", 1920, 1080)
image bg casino_playroom = im.Scale("gui/day3_casino/casino_playroom/bg_Playroom.jpg", 1920, 1080)
image bg cards_closeup = im.Scale("gui/day3_casino/casino_playroom/cards_closeup/cards_closeup.jpg", 1920, 1080)
image bg underground_casino = im.Scale("gui/day3_casino/underground_casino/bg Underground_Casino.jpg", 1920, 1080)
image bg backroom = im.Scale("gui/day3_casino/backroom/backroom_room/bg_backroom.png", 1920, 1080)
image bg backroom_open = im.Scale("gui/day3_casino/backroom/backroom_room/bg_backroom_open.png", 1920, 1080)
image bg safe_closeup = im.Scale("gui/day3_casino/backroom/safe/vault_close_up.jpg", 1920, 1080)
image bg safe_minigame = im.Scale("gui/day3_casino/backroom/safe/safe_minigame/safe.png", 1920, 1080)
image bg opened_safe = im.Scale("gui/day3_casino/backroom/safe/opened_safe/vault_open.jpg", 1920, 1080)
image bg wiring_minigame = im.Scale("gui/day3_casino/casino_playroom/wire_minigame/bg_wire_box.jpg", 1920, 1080)
image desk_newspaper = im.Scale("gui/desk_newspaper.jpg", 1920, 1080)
image d3newsroom1 = "gui/newsroom_scenes/Day3_Scene1.jpg"
image d3newsroom2 = "gui/newsroom_scenes/Day3_Scene2.jpg"

# --- NEW CONDITIONAL BACKGROUNDS ---
image bg playroom_fire = im.Scale("gui/day3_casino/casino_playroom/bg_playroom_fire.jpg", 1920, 1080)
image bg playroom_bouncer = im.Scale("gui/day3_casino/casino_playroom/bg_playroom_bouncer.jpg", 1920, 1080)
image bg casino_lobby_nobouncer = im.Scale("gui/day3_casino/casino_lobby/bg_casino lobby_noBouncer.jpg", 1920, 1080)

define dealer = Character("Dealer", color="#cccccc")
define cleaner = Character("Cleaner", color="#cccccc")
define waitress = Character("Waitress", color="#cccccc")
define drunk = Character("Drunk Patron", color="#cccccc")
define arthur = Character("Arthur", color="#cccccc")

default day3_clue = ""
default day3_item = ""
default day3_witness = ""
default evidence_ledger = False
default day3_clues_found = []
default day3_items_found = []
default day3_witnesses_found = []
default safe_unlocked = False
default slot_machine_shorted = False

# ==========================================
# DAY 3 BRIEFING
# ==========================================
label day3_start:
    $ current_day = 3
    python:
        for item in ["Blurry Photograph", "The Expensive Cigar", "The Dropped Lottery Ticket"]:
            if item in inventory_bag_items:
                inventory_bag_items.remove(item)

    play sting "audio/sting_day_transition.ogg" volume 0.75
    play music "audio/bgm_newsroom.ogg" fadeout 1.0 fadein 1.5 volume 0.55 if_changed
    play ambient "audio/amb_newsroom.ogg" fadeout 0.8 fadein 1.0 volume 0.40 if_changed

    scene bg newsroom
    scene d3newsroom1 with dissolve
    play sound "audio/sfx_paper_rustle.ogg"
    kenneth "What is this report that landed on my desk!?"
    kenneth "I told you to not cover the burned stall"
    scene d3newsroom2 with dissolve
    kenneth "Both of you, drop the gang story entirely!"
    kenneth "The two gangs are powerful organizations. If you keep digging, you'll be in danger."
    "(Sorry boss, but this gang dispute sounds like an interesting story)"
    "(I'll go to the casino tomorrow, I heard there was a shootout that happened there earlier)"

    play sound "audio/sfx_footsteps_move.ogg"
    show screen global_hud
    jump day3_outside

# ==========================================
# DAY 3 LOCATIONS
# ==========================================
label day3_outside:
    $ current_day = 3
    show screen global_hud
    scene bg casino_outside at topleft
    play music "audio/bgm_day3_casino.ogg" fadeout 1.0 fadein 1.2 volume 0.55 if_changed
    play ambient "audio/amb_night_street.ogg" fadeout 0.8 fadein 1.0 volume 0.45 if_changed

    call screen day3_outside_casino
    $ action = _return

    if action == "casino":
        play sound "audio/sfx_door_open.ogg"
        jump day3_lobby
    elif action == "club_front":
        play sound "audio/sfx_footsteps_move.ogg"
        jump day3_club_front
    elif action == "newsroom":
        play sound "audio/sfx_van_door.ogg"
        jump day3_newspaper_minigame
    else:
        jump day3_outside

label day3_club_front:
    scene bg club_front at topleft
    play music "audio/bgm_day3_casino.ogg" fadeout 1.0 fadein 1.0 volume 0.50 if_changed
    play ambient "audio/amb_night_street.ogg" fadeout 0.8 fadein 0.8 volume 0.50 if_changed

    call screen day3_club_front_environment
    $ action = _return

    if action == "inside_club":
        if "The VIP Pass" in inventory_bag_items or "The VIP Pass" in day3_items_found:
            play sound "audio/sfx_pickup_item.ogg"
            "Club Bouncer" "Welcome to the club sir. Enjoy your stay."
            play sound "audio/sfx_door_open.ogg"
            jump day3_club_inside
        else:
            play sound "audio/ui_evidence_locked.ogg"
            "Club Bouncer" "You need a VIP Pass to get past this door."
            jump day3_club_front
    elif action == "outside":
        play sound "audio/sfx_footsteps_move.ogg"
        jump day3_outside
    elif action == "newsroom":
        play sound "audio/sfx_van_door.ogg"
        jump day3_newspaper_minigame
    else:
        jump day3_club_front

label day3_club_inside:
    scene bg club_inside at topleft
    play music "audio/bgm_day3_club.ogg" fadeout 1.0 fadein 1.0 volume 0.55 if_changed
    stop ambient fadeout 0.8

    call screen day3_club_inside_environment
    $ action = _return

    if action == "outside":
        play sound "audio/sfx_door_open.ogg"
        jump day3_club_front
    elif action == "gossiper":
        play sound "audio/ui_notepad_flip.ogg"
        "Gossiping group" "They say the leader of one of the gang is someone powerful enough to control the whole town..."
        jump day3_club_inside
    elif action == "newsroom":
        play sound "audio/sfx_van_door.ogg"
        jump day3_newspaper_minigame
    else:
        jump day3_club_inside

label day3_lobby:
    if slot_machine_shorted:
        scene bg casino_lobby_nobouncer at topleft
    else:
        scene bg casino_lobby at topleft

    play music "audio/bgm_day3_casino.ogg" fadeout 1.0 fadein 1.0 volume 0.55 if_changed
    play ambient "audio/amb_casino_crime.ogg" fadeout 0.8 fadein 0.8 volume 0.45 if_changed

    call screen day3_casino_lobby
    $ action = _return

    if action == "outside":
        play sound "audio/sfx_door_open.ogg"
        jump day3_outside
    elif action == "playroom":
        play sound "audio/sfx_door_open.ogg"
        jump day3_playroom
    elif action == "underground":
        if slot_machine_shorted:
            play sound "audio/sfx_door_open.ogg"
            jump day3_underground
        else:
            play sound "audio/ui_evidence_locked.ogg"
            "Casino Bouncer" "Hit the road dude, this aint no public place this is private property."
            "Maybe if I cause a distraction to the slot machine in the Playroom, I can force him to go there."
            jump day3_lobby
    elif action == "cashier":
        play sound "audio/sfx_footsteps_move.ogg"
        jump day3_cashier_closeup
    elif action == "newsroom":
        play sound "audio/sfx_van_door.ogg"
        jump day3_newspaper_minigame
    else:
        jump day3_lobby

label day3_cashier_closeup:
    scene bg cashier_closeup at topleft
    play music "audio/bgm_day3_casino.ogg" fadeout 1.0 fadein 1.0 volume 0.55 if_changed
    play ambient "audio/amb_casino_crime.ogg" fadeout 0.8 fadein 0.8 volume 0.45 if_changed

    call screen day3_cashier_environment
    $ action = _return
    play sound "audio/ui_cancel.ogg"
    jump day3_lobby

label day3_playroom:
    if slot_machine_shorted:
        scene bg playroom_bouncer at topleft
        play ambient "audio/amb_playroom_fire.ogg" fadeout 0.8 fadein 0.8 volume 0.50 if_changed
    else:
        scene bg casino_playroom at topleft
        play ambient "audio/amb_casino_crime.ogg" fadeout 0.8 fadein 0.8 volume 0.45 if_changed

    play music "audio/bgm_day3_casino.ogg" fadeout 1.0 fadein 1.0 volume 0.50 if_changed

    call screen day3_playroom_environment
    $ action = _return

    if action == "lobby":
        play sound "audio/sfx_door_open.ogg"
        jump day3_lobby
    elif action == "cards_closeup":
        play sound "audio/sfx_footsteps_move.ogg"
        jump day3_cards_closeup
    elif action == "wire_minigame":
        play sound "audio/ui_click.ogg"
        jump day3_wire_minigame
    elif action == "arthur":
        arthur "Dude, this is getting dangerous."
        arthur "We're in this together right? We need to be careful."
        jump day3_playroom
    elif action == "jukebox":
        if "The Smashed Jukebox" not in day3_clues_found:
            $ day3_clues_found.append("The Smashed Jukebox")
            $ renpy.notify("Clue found: The Smashed Jukebox.")
        "The Smashed Jukebox. Broken glass and loose wiring."
        play sound "audio/sfx_camera_shutter.ogg"
        "It really is a mess in here. I should take a picture of this for my story."
        jump day3_playroom
    elif action == "drunk":
        if "Drunk Patron 1" not in day3_witnesses_found:
            play sound "audio/ui_notepad_flip.ogg"
            $ day3_witnesses_found.append("Drunk Patron 1")
            $ renpy.notify("Witness interviewed: Drunk Patron.")
        drunk "A rival casino owner drove a bulldozer into the wall!"
        drunk "I was drunk and passed out, but I saw the whole thing!"
        "But there are no holes on the wall. Maybe he is exaggerating."
        jump day3_playroom
    elif action == "newsroom":
        play sound "audio/sfx_van_door.ogg"
        jump day3_newspaper_minigame
    else:
        jump day3_playroom

label day3_cards_closeup:
    scene bg cards_closeup at topleft
    call screen day3_cards_closeup_environment
    $ action = _return

    if action == "back":
        play sound "audio/ui_cancel.ogg"
        jump day3_playroom
    elif action == "cards":
        play sound "audio/sfx_paper_rustle.ogg"
        if "The Scattered Marked Cards" not in day3_clues_found:
            $ day3_clues_found.append("The Scattered Marked Cards")
            $ renpy.notify("Clue found: The Scattered Marked Cards.")
        "Decks of crooked playing cards littered everywhere."
        "It looks like they need to fire their maid."
        jump day3_cards_closeup
    elif action == "earring":
        play sound "audio/sfx_pickup_item.ogg"
        if "The Diamond Earring" not in day3_items_found:
            $ day3_items_found.append("The Diamond Earring")
        if "The Diamond Earring" not in inventory_bag_items:
            $ inventory_bag_items.append("The Diamond Earring")
            $ renpy.notify("You got The Diamond Earring.")
        "A fake diamond earring on the floor."
        "I thought casino is where rich people gamble, but this is a cheap imitation."
        jump day3_cards_closeup
    else:
        jump day3_cards_closeup

label day3_wire_minigame:
    if slot_machine_shorted:
        "The bouncer is distracted."
        "I should move quickly."
        jump day3_playroom

    call screen day3_wire_minigame_screen
    $ action = _return

    if action == "win":
        $ slot_machine_shorted = True
        play sound "audio/sfx_spark.ogg"
        play ambient "audio/amb_playroom_fire.ogg" fadeout 0.5 fadein 0.8 volume 0.55 if_changed

        scene bg playroom_fire at topleft
        "SPARK! The crossed wires pop violently and smoke begins to rise from the cabinet."

        play sound "audio/sfx_bouncer_rush.ogg"
        scene bg playroom_bouncer at topleft with fade
        "The Casino Bouncer shouts in panic and runs over to inspect the Playroom!"
        jump day3_playroom

    elif action == "back":
        play sound "audio/ui_cancel.ogg"
        jump day3_playroom
    else:
        jump day3_playroom

# ==========================================
# UNDERGROUND CASINO, BACKROOM & SAFE PUZZLE
# ==========================================
label day3_underground:
    scene bg underground_casino at topleft
    play music "audio/bgm_day3_underground.ogg" fadeout 1.0 fadein 1.2 volume 0.55 if_changed
    play ambient "audio/amb_casino_crime.ogg" fadeout 0.8 fadein 0.8 volume 0.45 if_changed

    call screen day3_underground_casino
    $ action = _return

    if action == "lobby":
        play sound "audio/sfx_door_open.ogg"
        jump day3_lobby
    elif action == "backroom":
        play sound "audio/sfx_door_open.ogg"
        jump day3_backroom
    elif action == "bullethole":
        play sound "audio/sfx_camera_shutter.ogg"
        if "The Bullet-Riddled Wall" not in day3_clues_found:
            play sting "audio/sting_clue_major.ogg" volume 0.75
            $ day3_clues_found.append("The Bullet-Riddled Wall")
            $ renpy.notify("Clue found: The Bullet-Riddled Wall.")
        "Over fifty bullet holes scar the masonry."
        "This is a clue that proves heavy firepower was used in the attack."
        jump day3_underground
    elif action == "cleaner":
        if "Cleaner 1" not in day3_witnesses_found:
            play sound "audio/ui_notepad_flip.ogg"
            $ day3_witnesses_found.append("Cleaner 1")
            $ renpy.notify("Witness interviewed: Cleaner.")
        cleaner "The police raided the place in secret and took all the money!"
        cleaner "I was just cleaning the place when they came in and took everything!"
        jump day3_underground
    elif action == "waitress":
        if "Waitress 1" not in day3_witnesses_found:
            play sound "audio/ui_notepad_flip.ogg"
            $ day3_witnesses_found.append("Waitress 1")
            $ renpy.notify("Witness interviewed: Waitress.")
        waitress "An angry ghost haunts the basement!"
        waitress "I was serving drinks when I saw a shadowy figure and heard a loud crash!"
        jump day3_underground
    elif action == "creditcard":
        play sound "audio/sfx_pickup_item.ogg"
        if "The Stolen Credit Card" not in day3_items_found:
            $ day3_items_found.append("The Stolen Credit Card")
        if "The Stolen Credit Card" not in inventory_bag_items:
            $ inventory_bag_items.append("The Stolen Credit Card")
            $ renpy.notify("You got The Stolen Credit Card.")
        "A stolen plastic credit card."
        jump day3_underground
    elif action == "vippass":
        play sound "audio/sfx_pickup_item.ogg"
        if "The VIP Pass" not in day3_items_found:
            play sting "audio/sting_clue_major.ogg" volume 0.70
            $ day3_items_found.append("The VIP Pass")
        if "The VIP Pass" not in inventory_bag_items:
            $ inventory_bag_items.append("The VIP Pass")
            $ renpy.notify("You got The VIP Pass.")
        "It's a VIP Pass to a local club. A silver casino card."
        "With this, I can get into the club"
        jump day3_underground
    elif action == "newsroom":
        play sound "audio/sfx_van_door.ogg"
        jump day3_newspaper_minigame
    else:
        jump day3_underground

label day3_backroom:
    if safe_unlocked:
        scene bg backroom_open at topleft
    else:
        scene bg backroom at topleft

    play music "audio/bgm_day3_underground.ogg" fadeout 1.0 fadein 1.0 volume 0.55 if_changed
    play ambient "audio/amb_casino_crime.ogg" fadeout 0.8 fadein 0.8 volume 0.45 if_changed

    call screen day3_backroom_environment
    $ action = _return

    if action == "underground":
        play sound "audio/sfx_door_open.ogg"
        jump day3_underground
    elif action == "vault":
        play sound "audio/sfx_footsteps_move.ogg"
        jump day3_safe_close_up
    elif action == "dealer":
        if "Dealer 1" not in day3_witnesses_found:
            play sound "audio/ui_notepad_flip.ogg"
            $ day3_witnesses_found.append("Dealer 1")
            $ renpy.notify("Witness interviewed: Dealer.")
        dealer "The Iron Syndicate raided us because this is the River Boys' casino!"
        dealer "The tension between the two gangs has been building for years, and it looks like it about to explode!"
        jump day3_backroom
    elif action == "newsroom":
        play sound "audio/sfx_van_door.ogg"
        jump day3_newspaper_minigame
    else:
        jump day3_backroom

label day3_safe_close_up:
    scene bg safe_closeup at topleft
    play music "audio/bgm_day3_underground.ogg" fadeout 1.0 fadein 1.0 volume 0.55 if_changed
    play ambient "audio/amb_casino_crime.ogg" fadeout 0.8 fadein 0.8 volume 0.40 if_changed

    call screen day3_safe_closeup_environment
    $ action = _return

    if action == "back":
        play sound "audio/ui_cancel.ogg"
        jump day3_backroom
    elif action == "clue_paper":
        play sound "audio/sfx_paper_rustle.ogg"
        "The note has a jack-o-lantern and a genie, maybe this is a clue. It says Jack-O-Lantern and a genie."
        "When do I see jack-o-lanterns and for the genies, could it be the number of wishes? Maybe this is an elaborate clue."
        jump day3_safe_close_up
    elif action == "safe_interact":
        if safe_unlocked:
            play sound "audio/sfx_door_open.ogg"
            jump day3_opened_safe_view
        else:
            play sound "audio/ui_click.ogg"
            jump day3_safe_minigame
    else:
        jump day3_safe_close_up

label day3_safe_minigame:
    $ safe_current_digit = 0
    $ safe_entered_code = ""

label day3_safe_minigame_loop:
    scene bg safe_minigame at topleft
    call screen safe_puzzle_screen(safe_current_digit, safe_entered_code)
    $ action = _return

    if action == "turn_right":
        play sound "audio/sfx_safe_tick.ogg"
        $ safe_current_digit = (safe_current_digit - 1) % 10
        jump day3_safe_minigame_loop
    elif action == "turn_left":
        play sound "audio/sfx_safe_tick.ogg"
        $ safe_current_digit = (safe_current_digit + 1) % 10
        jump day3_safe_minigame_loop
    elif action == "enter_digit":
        $ safe_entered_code += str(safe_current_digit)
        if len(safe_entered_code) == 3:
            if safe_entered_code == "313":
                $ safe_unlocked = True
                play sound "audio/sfx_safe_unlock.ogg"
                "Click. The heavy mechanism unlocks."
                jump day3_opened_safe_view
            else:
                play sound "audio/sfx_safe_error.ogg"
                "Bzzt. Wrong combination. The dial resets."
                $ safe_entered_code = ""
                jump day3_safe_minigame_loop
        else:
            play sound "audio/sfx_safe_enter.ogg"
        jump day3_safe_minigame_loop
    elif action == "exit":
        play sound "audio/ui_cancel.ogg"
        jump day3_safe_close_up
    else:
        jump day3_safe_minigame_loop

label day3_opened_safe_view:
    scene bg opened_safe at topleft
    call screen day3_opened_safe_environment
    $ action = _return

    if action == "bloody_ledger":
        $ evidence_ledger = True
        play sound "audio/sfx_paper_rustle.ogg"
        play sting "audio/sting_clue_major.ogg" volume 0.80
        if "The Bloody Ledger" not in inventory_bag_items:
            $ inventory_bag_items.append("The Bloody Ledger")
            $ renpy.notify("You got The Bloody Ledger.")
        "I found a Bloody Ledger listing illegal weapon purchases inside the safe."
        "The details are all here, the buyers, the sellers, the dates, and the prices."
        jump day3_opened_safe_view
    elif action == "back":
        play sound "audio/ui_cancel.ogg"
        jump day3_safe_close_up
    else:
        jump day3_opened_safe_view

# ==========================================
# NEWSROOM MINIGAME
# ==========================================
label day3_newspaper_minigame:
    $ hide_all_investigation_screens()
    play sound "audio/sfx_typewriter_write.ogg"
    play music "audio/bgm_newsroom.ogg" fadeout 1.0 fadein 1.2 volume 0.55 if_changed
    play ambient "audio/amb_newsroom.ogg" fadeout 1.0 fadein 1.0 volume 0.35 if_changed

    scene news_creation with dissolve
    "Time to review my Reporter's Notepad and write the casino edition."

label select_day3_clue:
    play sound "audio/ui_notepad_flip.ogg"
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
    play sound "audio/ui_notepad_flip.ogg"
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
    play sound "audio/ui_notepad_flip.ogg"
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
        day3_accurate_picks = (
            (day3_clue == "The Bullet-Riddled Wall")
            + (day3_item == "The VIP Pass")
            + (day3_witness == "Dealer 1")
        )

    scene desk_newspaper
    play sound "audio/sfx_newspaper_print.ogg"
    "Let's see how the casino edition turned out..."

    if day3_accurate_picks >= 2:
        play sting "audio/sting_rating_high.ogg" volume 0.80
    else:
        play sting "audio/sting_rating_low.ogg" volume 0.80

    call screen newspaper_results_ui(daily_headline, daily_body, daily_rating, total_credibility_score)
    play sound "audio/sfx_paper_rustle.ogg"
    $ renpy.force_autosave(True)
    jump day4_start