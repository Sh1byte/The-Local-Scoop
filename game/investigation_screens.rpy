# ==========================================
# DAY 1 WAREHOUSE SCREEN
# ==========================================
screen day1_warehouse_investigation():
    # --- CLUES ---
    if "paint_can" not in day1_clicked_points:
        imagebutton xpos 200 ypos 650 idle "ui_assets/clue_paint.png" hover "ui_assets/clue_paint_hover.png" action Return("paint_can")
    if "whiskey" not in day1_clicked_points:
        imagebutton xpos 800 ypos 700 idle "ui_assets/clue_whiskey.png" hover "ui_assets/clue_whiskey_hover.png" action Return("whiskey")
    if "pizza" not in day1_clicked_points:
        imagebutton xpos 300 ypos 750 idle "ui_assets/clue_pizza.png" hover "ui_assets/clue_pizza_hover.png" action Return("pizza")

    # --- ITEMS ---
    if "keyring" not in day1_clicked_points:
        imagebutton xpos 400 ypos 450 idle "ui_assets/item_keyring.png" hover "ui_assets/item_keyring_hover.png" action Return("keyring")
    if "watch" not in day1_clicked_points:
        imagebutton xpos 600 ypos 500 idle "ui_assets/item_watch.png" hover "ui_assets/item_watch_hover.png" action Return("watch")
    if "collar" not in day1_clicked_points:
        imagebutton xpos 700 ypos 600 idle "ui_assets/item_collar.png" hover "ui_assets/item_collar_hover.png" action Return("collar")

    # --- HIDDEN EVIDENCE ---
    if "lighter" not in day1_clicked_points:
        imagebutton xpos 900 ypos 850 idle "ui_assets/evidence_lighter.png" hover "ui_assets/evidence_lighter_hover.png" action Return("lighter")

    # --- WITNESSES ---
    if "watchman" not in day1_clicked_points:
        imagebutton xpos 1100 ypos 300 idle "ui_assets/watchman_neutral.png" hover "ui_assets/watchman_hover.png" action Return("watchman")
    if "fisherman" not in day1_clicked_points:
        imagebutton xpos 100 ypos 350 idle "ui_assets/fisherman_neutral.png" hover "ui_assets/fisherman_hover.png" action Return("fisherman")
    if "driver" not in day1_clicked_points:
        imagebutton xpos 850 ypos 250 idle "ui_assets/driver_neutral.png" hover "ui_assets/driver_hover.png" action Return("driver")
    if "jogger" not in day1_clicked_points:
        imagebutton xpos 1200 ypos 400 idle "ui_assets/jogger_neutral.png" hover "ui_assets/jogger_hover.png" action Return("jogger")

    # --- EXIT BUTTON ---
    if len(day1_clues_found) > 0 and len(day1_items_found) > 0 and len(day1_witnesses_found) > 0:
        imagebutton xalign 0.5 yalign 0.95 idle "ui_assets/ui_button_write_idle.png" hover "ui_assets/ui_button_write_hover.png" action Return("newsroom")
        
    # --- TOGGLES ---
    imagebutton xalign 0.95 yalign 0.05 idle "ui_assets/ui_icon_notepad_idle.png" hover "ui_assets/ui_icon_notepad_hover.png" action ToggleScreen("reporters_notepad")
    imagebutton xalign 0.95 yalign 0.15 idle "ui_assets/ui_icon_bag_idle.png" hover "ui_assets/ui_icon_bag_hover.png" action ToggleScreen("inventory_bag")


# ==========================================
# DAY 2 MARKET PLAZA SCREEN
# ==========================================
screen day2_market_investigation():
    # --- CLUES ---
    if "gascan" not in day2_clicked_points:
        imagebutton xpos 200 ypos 650 idle "ui_assets/clue_gascan.png" hover "ui_assets/clue_gascan_hover.png" action Return("gascan")
    if "toycar" not in day2_clicked_points:
        imagebutton xpos 800 ypos 700 idle "ui_assets/clue_toycar.png" hover "ui_assets/clue_toycar_hover.png" action Return("toycar")
    if "oil" not in day2_clicked_points:
        imagebutton xpos 300 ypos 750 idle "ui_assets/clue_oil.png" hover "ui_assets/clue_oil_hover.png" action Return("oil")

    # --- ITEMS ---
    if "camera" not in day2_clicked_points:
        imagebutton xpos 400 ypos 450 idle "ui_assets/item_camera.png" hover "ui_assets/item_camera_hover.png" action Return("camera")
    if "cigar" not in day2_clicked_points:
        imagebutton xpos 600 ypos 500 idle "ui_assets/item_cigar.png" hover "ui_assets/item_cigar_hover.png" action Return("cigar")
    if "lottery" not in day2_clicked_points:
        imagebutton xpos 700 ypos 600 idle "ui_assets/item_lottery.png" hover "ui_assets/item_lottery_hover.png" action Return("lottery")

    # --- HIDDEN EVIDENCE ---
    if "letter" not in day2_clicked_points:
        imagebutton xpos 900 ypos 850 idle "ui_assets/evidence_letter.png" hover "ui_assets/evidence_letter_hover.png" action Return("letter")

    # --- WITNESSES ---
    if "vendor" not in day2_clicked_points:
        imagebutton xpos 1100 ypos 300 idle "ui_assets/vendor_neutral.png" hover "ui_assets/vendor_hover.png" action Return("vendor")
    if "shopper" not in day2_clicked_points:
        imagebutton xpos 100 ypos 350 idle "ui_assets/shopper_neutral.png" hover "ui_assets/shopper_hover.png" action Return("shopper")
    if "baker" not in day2_clicked_points:
        imagebutton xpos 850 ypos 250 idle "ui_assets/baker_neutral.png" hover "ui_assets/baker_hover.png" action Return("baker")
    if "musician" not in day2_clicked_points:
        imagebutton xpos 1200 ypos 400 idle "ui_assets/musician_neutral.png" hover "ui_assets/musician_hover.png" action Return("musician")

    # --- EXIT BUTTON ---
    if len(day2_clues_found) > 0 and len(day2_items_found) > 0 and len(day2_witnesses_found) > 0:
        imagebutton xalign 0.5 yalign 0.95 idle "ui_assets/ui_button_write_idle.png" hover "ui_assets/ui_button_write_hover.png" action Return("newsroom")
        
    # --- TOGGLES ---
    imagebutton xalign 0.95 yalign 0.05 idle "ui_assets/ui_icon_notepad_idle.png" hover "ui_assets/ui_icon_notepad_hover.png" action ToggleScreen("reporters_notepad")
    imagebutton xalign 0.95 yalign 0.15 idle "ui_assets/ui_icon_bag_idle.png" hover "ui_assets/ui_icon_bag_hover.png" action ToggleScreen("inventory_bag")


# ==========================================
# DAY 3 CASINO SCREEN
# ==========================================
screen day3_casino_investigation():
    # --- CLUES ---
    if "bullethole" not in day3_clicked_points:
        imagebutton xpos 200 ypos 650 idle "ui_assets/clue_bullethole.png" hover "ui_assets/clue_bullethole_hover.png" action Return("bullethole")
    if "cards" not in day3_clicked_points:
        imagebutton xpos 800 ypos 700 idle "ui_assets/clue_cards.png" hover "ui_assets/clue_cards_hover.png" action Return("cards")
    if "jukebox" not in day3_clicked_points:
        imagebutton xpos 300 ypos 750 idle "ui_assets/clue_jukebox.png" hover "ui_assets/clue_jukebox_hover.png" action Return("jukebox")

    # --- ITEMS ---
    if "vippass" not in day3_clicked_points:
        imagebutton xpos 400 ypos 450 idle "ui_assets/item_vippass.png" hover "ui_assets/item_vippass_hover.png" action Return("vippass")
    if "earring" not in day3_clicked_points:
        imagebutton xpos 600 ypos 500 idle "ui_assets/item_earring.png" hover "ui_assets/item_earring_hover.png" action Return("earring")
    if "creditcard" not in day3_clicked_points:
        imagebutton xpos 700 ypos 600 idle "ui_assets/item_creditcard.png" hover "ui_assets/item_creditcard_hover.png" action Return("creditcard")

    # --- HIDDEN EVIDENCE ---
    if "ledger" not in day3_clicked_points:
        imagebutton xpos 900 ypos 850 idle "ui_assets/evidence_ledger.png" hover "ui_assets/evidence_ledger_hover.png" action Return("ledger")

    # --- WITNESSES ---
    if "dealer" not in day3_clicked_points:
        imagebutton xpos 1100 ypos 300 idle "ui_assets/dealer_neutral.png" hover "ui_assets/dealer_hover.png" action Return("dealer")
    if "cleaner" not in day3_clicked_points:
        imagebutton xpos 100 ypos 350 idle "ui_assets/cleaner_neutral.png" hover "ui_assets/cleaner_hover.png" action Return("cleaner")
    if "waitress" not in day3_clicked_points:
        imagebutton xpos 850 ypos 250 idle "ui_assets/waitress_neutral.png" hover "ui_assets/waitress_hover.png" action Return("waitress")
    if "drunk" not in day3_clicked_points:
        imagebutton xpos 1200 ypos 400 idle "ui_assets/drunk_neutral.png" hover "ui_assets/drunk_hover.png" action Return("drunk")

    # --- EXIT BUTTON ---
    if len(day3_clues_found) > 0 and len(day3_items_found) > 0 and len(day3_witnesses_found) > 0:
        imagebutton xalign 0.5 yalign 0.95 idle "ui_assets/ui_button_write_idle.png" hover "ui_assets/ui_button_write_hover.png" action Return("newsroom")
        
    # --- TOGGLES ---
    imagebutton xalign 0.95 yalign 0.05 idle "ui_assets/ui_icon_notepad_idle.png" hover "ui_assets/ui_icon_notepad_hover.png" action ToggleScreen("reporters_notepad")
    imagebutton xalign 0.95 yalign 0.15 idle "ui_assets/ui_icon_bag_idle.png" hover "ui_assets/ui_icon_bag_hover.png" action ToggleScreen("inventory_bag")


# ==========================================
# DAY 5 DEPOT SCREEN
# ==========================================
screen day5_depot_investigation():
    # --- CLUES ---
    if "tiretracks" not in day5_clicked_points:
        imagebutton xpos 200 ypos 650 idle "ui_assets/clue_tiretracks.png" hover "ui_assets/clue_tiretracks_hover.png" action Return("tiretracks")
    if "dogtracks" not in day5_clicked_points:
        imagebutton xpos 800 ypos 700 idle "ui_assets/clue_dogtracks.png" hover "ui_assets/clue_dogtracks_hover.png" action Return("dogtracks")
    if "oilpuddle" not in day5_clicked_points:
        imagebutton xpos 300 ypos 750 idle "ui_assets/clue_oilpuddle.png" hover "ui_assets/clue_oilpuddle_hover.png" action Return("oilpuddle")

    # --- ITEMS ---
    if "ticketstub" not in day5_clicked_points:
        imagebutton xpos 400 ypos 450 idle "ui_assets/item_ticketstub.png" hover "ui_assets/item_ticketstub_hover.png" action Return("ticketstub")
    if "wallet" not in day5_clicked_points:
        imagebutton xpos 600 ypos 500 idle "ui_assets/item_wallet.png" hover "ui_assets/item_wallet_hover.png" action Return("wallet")
    if "toolbox" not in day5_clicked_points:
        imagebutton xpos 700 ypos 600 idle "ui_assets/item_toolbox.png" hover "ui_assets/item_toolbox_hover.png" action Return("toolbox")

    # --- HIDDEN EVIDENCE ---
    if "phone" not in day5_clicked_points:
        imagebutton xpos 900 ypos 850 idle "ui_assets/evidence_phone.png" hover "ui_assets/evidence_phone_hover.png" action Return("phone")

    # --- WITNESSES ---
    if "medic" not in day5_clicked_points:
        imagebutton xpos 1100 ypos 300 idle "ui_assets/medic_neutral.png" hover "ui_assets/medic_hover.png" action Return("medic")
    if "engineer" not in day5_clicked_points:
        imagebutton xpos 100 ypos 350 idle "ui_assets/engineer_neutral.png" hover "ui_assets/engineer_hover.png" action Return("engineer")
    if "hobo" not in day5_clicked_points:
        imagebutton xpos 850 ypos 250 idle "ui_assets/hobo_neutral.png" hover "ui_assets/hobo_hover.png" action Return("hobo")
    if "tourist" not in day5_clicked_points:
        imagebutton xpos 1200 ypos 400 idle "ui_assets/tourist_neutral.png" hover "ui_assets/tourist_hover.png" action Return("tourist")

    # --- EXIT BUTTON ---
    if len(day5_clues_found) > 0 and len(day5_items_found) > 0 and len(day5_witnesses_found) > 0 and evidence_phone:
        imagebutton xalign 0.5 yalign 0.95 idle "ui_assets/ui_button_write_idle.png" hover "ui_assets/ui_button_write_hover.png" action Return("newsroom")
        
    # --- TOGGLES ---
    imagebutton xalign 0.95 yalign 0.05 idle "ui_assets/ui_icon_notepad_idle.png" hover "ui_assets/ui_icon_notepad_hover.png" action ToggleScreen("reporters_notepad")
    imagebutton xalign 0.95 yalign 0.15 idle "ui_assets/ui_icon_bag_idle.png" hover "ui_assets/ui_icon_bag_hover.png" action ToggleScreen("inventory_bag")


# ==========================================
# NOTEPAD & BAG SCREENS
# ==========================================
screen reporters_notepad():
    add Solid("#00000088")
    add "ui_assets/ui_notepad.png" align (0.5, 0.5)

    imagebutton:
        align (0.75, 0.25)
        idle "ui_assets/ui_close_idle.png"
        hover "ui_assets/ui_close_hover.png"
        action Hide("reporters_notepad")
        
    vbox:
        xalign 0.5 ypos 300
        spacing 15
        
        text "Case Evidence Tracker" size 32 bold True color "#155dfc"
        
        if evidence_lighter:
            text "• The Brass Lighter (Iron Syndicate)" size 24 color "#6a7282"
        if evidence_letter:
            text "• The Extortion Letter (The River Boys)" size 24 color "#6a7282"
        if evidence_ledger:
            text "• The Bloody Ledger (Joint Purchase)" size 24 color "#6a7282"
        if evidence_phone:
            text "• The Burner Phone (Midnight Dock War)" size 24 color "#6a7282"
            
        if not evidence_lighter and not evidence_letter and not evidence_ledger and not evidence_phone:
            text "No hard evidence collected yet." size 24 color "#6a7282" italic True


screen inventory_bag():
    add Solid("#00000088")
    add "ui_assets/ui_bag_bg.png" align (0.5, 0.5)

    imagebutton:
        align (0.75, 0.25)
        idle "ui_assets/ui_close_idle.png"
        hover "ui_assets/ui_close_hover.png"
        action Hide("inventory_bag")
        
    vbox:
        xalign 0.5 ypos 300
        spacing 15
        
        text "Physical Evidence Bag" size 32 bold True color "#155dfc"
        
        for item in inventory_bag_items:
            text "• [item]" size 24 color "#6a7282"
            
        if len(inventory_bag_items) == 0:
            text "The bag is empty." size 24 color "#6a7282" italic True