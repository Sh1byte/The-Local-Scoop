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

label day3_start:
    # Clear out unused items from Day 2 Bag (Keeping the Extortion Letter)
    python:
        for item in ["Blurry Photograph", "The Expensive Cigar", "The Dropped Lottery Ticket"]:
            if item in inventory_bag_items:
                inventory_bag_items.remove(item)
    scene bg newsroom
    vance "Both of you, drop the gang story entirely!"
    scene bg casino_basement
    arthur "Look, this is getting deadly. We are a team now."
    jump day3_outside

# ==========================================
# DAY 3 LOCATIONS
# ==========================================
label day3_outside:
    scene bg casino_outside at topleft
    call screen day3_outside_casino
    $ action = _return
    if action == "casino":
        jump day3_lobby
    elif action == "club_front":
        jump day3_club_front
    elif action == "newsroom":
        jump day3_newspaper_minigame

label day3_club_front:
    scene bg club_front at topleft
    call screen day3_club_front_environment
    $ action = _return
    if action == "inside_club":
        if "The VIP Pass" in inventory_bag_items:
            jump day3_club_inside
        else:
            "Club Bouncer" "You need a VIP Pass to get past this door."
            jump day3_club_front
    elif action == "outside":
        jump day3_outside
    elif action == "newsroom":
        jump day3_newspaper_minigame

label day3_club_inside:
    scene bg club_inside at topleft
    call screen day3_club_inside_environment
    $ action = _return
    if action == "outside":
        jump day3_club_front
    elif action == "gossiper":
        "Gossiping group" "They say the leader of one of the gang is someone powerful enough to control the whole town..."
        jump day3_club_inside
    elif action == "newsroom":
        jump day3_newspaper_minigame

label day3_lobby:
    if slot_machine_shorted:
        scene bg casino_lobby_nobouncer at topleft
    else:
        scene bg casino_lobby at topleft
        
    call screen day3_casino_lobby
    $ action = _return
    if action == "outside":
        jump day3_outside
    elif action == "playroom":
        jump day3_playroom
    elif action == "underground":
        if slot_machine_shorted:
            jump day3_underground
        else:
            "Casino Bouncer" "You can't go down there unless there's an emergency."
            "Maybe if I cause a distraction to the slot machine in the Playroom, I can tell him to go there."
            jump day3_lobby
    elif action == "cashier":
        jump day3_cashier_closeup
    elif action == "newsroom":
        jump day3_newspaper_minigame

# Make sure this label is present and starts at the very beginning of the line (no indentation):
label day3_cashier_closeup:
    scene bg cashier_closeup at topleft
    call screen day3_cashier_environment
    $ action = _return
    jump day3_lobby

label day3_playroom:
    if slot_machine_shorted:
        scene bg playroom_bouncer at topleft
    else:
        scene bg casino_playroom at topleft
        
    call screen day3_playroom_environment
    $ action = _return
    if action == "lobby":
        jump day3_lobby
    elif action == "cards_closeup":
        jump day3_cards_closeup
    elif action == "wire_minigame":
        jump day3_wire_minigame
    elif action == "arthur":
        arthur "I realize the danger now. I agree to split the work with you."
        if "Arthur" not in day3_witnesses_found:
            $ day3_witnesses_found.append("Arthur")
        jump day3_playroom
    elif action == "jukebox":
        "The Smashed Jukebox. Broken glass and loose wiring."
        if "The Smashed Jukebox" not in day3_clues_found:
            $ day3_clues_found.append("The Smashed Jukebox")
        jump day3_playroom
    elif action == "drunk":
        drunk "A rival casino owner drove a bulldozer into the wall!"
        if "Drunk Patron 1" not in day3_witnesses_found:
            $ day3_witnesses_found.append("Drunk Patron 1")
        jump day3_playroom
    elif action == "newsroom":
        jump day3_newspaper_minigame

label day3_cards_closeup:
    scene bg cards_closeup at topleft
    call screen day3_cards_closeup_environment
    $ action = _return
    if action == "back":
        jump day3_playroom
    elif action == "cards":
        "Decks of crooked playing cards littered everywhere."
        if "The Scattered Marked Cards" not in day3_clues_found:
            $ day3_clues_found.append("The Scattered Marked Cards")
        jump day3_cards_closeup
    elif action == "earring":
        "A fake diamond earring on the floor."
        if "The Diamond Earring" not in day3_items_found:
            $ day3_items_found.append("The Diamond Earring")
            $ inventory_bag_items.append("The Diamond Earring")
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
        
        scene bg playroom_fire at topleft
        "SPARK! The crossed wires pop violently and smoke begins to rise from the cabinet."
        
        scene bg playroom_bouncer at topleft with fade
        "The Casino Bouncer shouts in panic and runs over to inspect the Playroom!"
        jump day3_playroom 
        
    elif action == "back":
        jump day3_playroom

label day3_underground:
    scene bg underground_casino at topleft
    call screen day3_underground_casino
    $ action = _return
    if action == "lobby":
        jump day3_lobby
    elif action == "backroom":
        jump day3_backroom
    elif action == "bullethole":
        "Over fifty bullet holes scar the masonry."
        if "The Bullet-Riddled Wall" not in day3_clues_found:
            $ day3_clues_found.append("The Bullet-Riddled Wall")
        jump day3_underground
    elif action == "cleaner":
        cleaner "The police raided the place in secret and took all the money!"
        if "Cleaner 1" not in day3_witnesses_found:
            $ day3_witnesses_found.append("Cleaner 1")
        jump day3_underground
    elif action == "waitress":
        waitress "An angry ghost haunts the basement!"
        if "Waitress 1" not in day3_witnesses_found:
            $ day3_witnesses_found.append("Waitress 1")
        jump day3_underground
    elif action == "creditcard":
        "A stolen plastic credit card."
        if "The Stolen Credit Card" not in day3_items_found:
            $ day3_items_found.append("The Stolen Credit Card")
            $ inventory_bag_items.append("The Stolen Credit Card")
        jump day3_underground
    elif action == "vippass":
        "It's a VIP Pass to a local club. A silver casino card."
        if "The VIP Pass" not in day3_items_found:
            $ day3_items_found.append("The VIP Pass")
            $ inventory_bag_items.append("The VIP Pass")
        jump day3_underground
    elif action == "newsroom":
        jump day3_newspaper_minigame

label day3_backroom:
    if safe_unlocked:
        scene bg backroom_open at topleft
    else:
        scene bg backroom at topleft
        
    call screen day3_backroom_environment
    $ action = _return
    if action == "underground":
        jump day3_underground
    elif action == "vault":
        jump day3_safe_close_up
    elif action == "dealer":
        dealer "The Iron Syndicate raided us because this place is owned by The River Boys!"
        if "Dealer 1" not in day3_witnesses_found:
            $ day3_witnesses_found.append("Dealer 1")
        jump day3_backroom
    elif action == "newsroom":
        jump day3_newspaper_minigame

label day3_safe_close_up:
    scene bg safe_closeup at topleft
    call screen day3_safe_closeup_environment
    $ action = _return
    if action == "back":
        jump day3_backroom
    elif action == "clue_paper":
        "The note has a jack-o-lantern and a genie, maybe this is a clue. It says '3 - 1 - 3'."
        jump day3_safe_close_up
    elif action == "safe_interact":
        if safe_unlocked:
            jump day3_opened_safe_view
        else:
            jump day3_safe_minigame

label day3_safe_minigame:
    $ safe_current_digit = 0
    $ safe_entered_code = ""
label day3_safe_minigame_loop:
    scene bg safe_minigame at topleft
    call screen safe_puzzle_screen(safe_current_digit, safe_entered_code)
    $ action = _return
    if action == "turn_right":
        $ safe_current_digit = (safe_current_digit - 1) % 10
        jump day3_safe_minigame_loop
    elif action == "turn_left":
        $ safe_current_digit = (safe_current_digit + 1) % 10
        jump day3_safe_minigame_loop
    elif action == "enter_digit":
        $ safe_entered_code += str(safe_current_digit)
        if len(safe_entered_code) == 3:
            if safe_entered_code == "313":
                $ safe_unlocked = True
                "Click. The heavy mechanism unlocks."
                jump day3_opened_safe_view
            else:
                "Bzzt. Wrong combination. The dial resets."
                $ safe_entered_code = ""
                jump day3_safe_minigame_loop
        jump day3_safe_minigame_loop
    elif action == "exit":
        jump day3_safe_close_up

label day3_opened_safe_view:
    scene bg opened_safe at topleft
    call screen day3_opened_safe_environment
    $ action = _return
    if action == "bloody_ledger":
        "I found a Bloody Ledger listing illegal weapon purchases inside the safe."
        $ evidence_ledger = True
        jump day3_opened_safe_view
    elif action == "back":
        jump day3_safe_close_up

# ==========================================
# NEWSROOM MINIGAME
# ==========================================
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