init python:
    def brighten(image_path, amount=0.2):
        return Transform(image_path, matrixcolor=BrightnessMatrix(amount))

# ==========================================
# DAY 1 WAREHOUSE SCREENS
# ==========================================
screen day1_warehouse_back_environment():
    imagebutton xpos 0 ypos 0 idle "gui/day1_back_warehouse/fisherman.png" hover brighten("gui/day1_back_warehouse/fisherman.png") focus_mask True action Return("fisherman")
    imagebutton xpos 0 ypos 0 idle "gui/day1_back_warehouse/warehouse_inside_from_back.png" hover brighten("gui/day1_back_warehouse/warehouse_inside_from_back.png") focus_mask True action Return("warehouse_inside_from_the_back")
    imagebutton xpos 0 ypos 0 idle "gui/day1_back_warehouse/garage_back_warehouse.png" hover brighten("gui/day1_back_warehouse/garage_back_warehouse.png") focus_mask True action Return("garage_back_warehouse")
    imagebutton xpos 0 ypos 0 idle "gui/day1_back_warehouse/return_to_front.png" hover brighten("gui/day1_back_warehouse/return_to_front.png") focus_mask True action Return("back_to_front")
   
    # Collar and Watch (Always Visible)
    imagebutton xpos 800 ypos 890 idle "gui/warehouse/item_collar.png" hover brighten("gui/warehouse/item_collar.png") action Return("collar") at Transform(zoom=0.08)
    imagebutton xpos 1100 ypos 880 idle "gui/warehouse/item_watch.png" hover brighten("gui/warehouse/item_watch.png") action Return("watch") at Transform(zoom=0.06)
       
    key "K_ESCAPE" action Return("back_to_front")

screen day1_warehouse_inside_environment():
    # Whiskey and Pizza (Always Visible)
    imagebutton xpos 350 ypos 920 idle "gui/warehouse/clue_whiskey.png" hover brighten("gui/warehouse/clue_whiskey.png") action Return("whiskey") at Transform(zoom=0.08)
    imagebutton xpos 1400 ypos 920 idle "gui/warehouse/clue_pizza.png" hover brighten("gui/warehouse/clue_pizza.png") action Return("pizza") at Transform(zoom=0.15)
       
    key "K_ESCAPE" action Return("return_to_front")

screen day1_warehouse_garage_back_environment():
    # Keyring disappears once added to the inventory bag
    if "The Janitor's Keyring" not in inventory_bag_items:
        imagebutton xpos 400 ypos 900 idle "gui/warehouse/item_keyring.png" hover brighten("gui/warehouse/item_keyring.png") action [Notify("You got a keyring."), Return("keyring")] at Transform(zoom=0.06)
       
    key "K_ESCAPE" action Return("return_to_front")
   
screen tower_clipboard_overlay():
    modal True
    add "gui/day_tower_warehouse/flashlight/clipboard.png" xalign 0.5 yalign 0.5
    textbutton "Close" xalign 0.92 yalign 0.08 action Hide("tower_clipboard_overlay")
    key "K_ESCAPE" action Hide("tower_clipboard_overlay")

screen flashlight_environment():
    modal True
    add "gui/day_tower_warehouse/flashlight/flashlight.png"
    imagebutton:
        xpos 0 ypos 0
        idle "gui/day_tower_warehouse/flashlight/fl_open_idle.png"
        hover brighten("gui/day_tower_warehouse/flashlight/fl_open_idle.png")
        focus_mask True
        action Show("flashlight_open_environment")
    textbutton "Close" xalign 0.92 yalign 0.08 action Hide("flashlight_environment")
    key "K_ESCAPE" action Hide("flashlight_environment")

screen flashlight_open_environment():
    modal True
    add "gui/day_tower_warehouse/flashlight/flashlight_open.png"
    imagebutton:
        xpos 0 ypos 0
        idle "gui/day_tower_warehouse/flashlight/fl_empty_idle.png"
        hover brighten("gui/day_tower_warehouse/flashlight/fl_empty_idle.png")
        focus_mask True
        action Show("flashlight_empty_environment")
    textbutton "Close" xalign 0.92 yalign 0.08 action Hide("flashlight_open_environment")
    key "K_ESCAPE" action Hide("flashlight_open_environment")

screen flashlight_empty_environment():
    modal True
    add "gui/day_tower_warehouse/flashlight/flashlight_empty.png"
    if not battery_obtained and "Battery" not in inventory_bag_items:
        imagebutton:
            align (0.5, 0.5)
            idle "gui/day_tower_warehouse/flashlight/battery.png"
            hover brighten("gui/day_tower_warehouse/flashlight/battery.png")
            focus_mask True
            action [
                Notify("You got a battery."),
                Function(inventory_bag_items.append, "Battery"),
                SetVariable("battery_obtained", True),
                Hide("flashlight_empty_environment"),
                Hide("flashlight_open_environment"),
                Hide("flashlight_environment"),
                Return("Battery")
            ]
    textbutton "Close" xalign 0.92 yalign 0.08 action [
        Hide("flashlight_empty_environment"),
        Hide("flashlight_open_environment"),
        Hide("flashlight_environment")
    ]
    key "K_ESCAPE" action [
        Hide("flashlight_empty_environment"),
        Hide("flashlight_open_environment"),
        Hide("flashlight_environment")
    ]

screen day1_warehouse_tower_environment():
    add "gui/day_tower_warehouse/bg_tower_warehouse.png"
    imagebutton xpos 0 ypos 0 idle "gui/day_tower_warehouse/jogger.png" hover brighten("gui/day_tower_warehouse/jogger.png") focus_mask True action Return("jogger")
    imagebutton:
        xpos 0 ypos 0
        idle "gui/day_tower_warehouse/tower_clipboard.png"
        hover brighten("gui/day_tower_warehouse/tower_clipboard.png")
        focus_mask True
        action Show("tower_clipboard_overlay")
    imagebutton:
        xpos 0 ypos 0
        idle "gui/day_tower_warehouse/tower_flashlight.png"
        hover brighten("gui/day_tower_warehouse/tower_flashlight.png")
        focus_mask True
        action Show("flashlight_environment")
    key "K_ESCAPE" action Return("return_to_front")

screen day1_warehouse_office_environment():
    if office_empty:
        add "gui/day1_office/bg_office_empty.png"
    else:
        add "gui/day1_office/bg_office.png"
        imagebutton:
            xpos 0
            ypos 0
            idle "gui/day1_office/officerguy.png"
            hover brighten("gui/day1_office/officerguy.png")
            focus_mask True
            action Return("officerguy")
    imagebutton:
        xpos 0
        ypos 0
        idle "gui/day1_office/desktop_office_idle.png"
        hover brighten("gui/day1_office/desktop_office_idle.png")
        focus_mask True
        action Show("development_environment")
    imagebutton:
        xpos 0
        ypos 0
        idle "gui/day1_office/keyholder_idle.png"
        hover brighten("gui/day1_office/keyholder_idle.png")
        focus_mask True
        action Show("key_holder_environment")
    imagebutton:
        xpos 0
        ypos 0
        idle "gui/day1_office/desk_drawer1_idle.png"
        hover brighten("gui/day1_office/desk_drawer1_idle.png")
        focus_mask True
        action Show("development_environment")
    imagebutton:
        xpos 0
        ypos 0
        idle "gui/day1_office/desk_drawer2_idle.png"
        hover brighten("gui/day1_office/desk_drawer2_idle.png")
        focus_mask True
        action Show("development_environment")
    imagebutton:
        xpos 0
        ypos 0
        idle "gui/day1_office/drawer1_idle.png"
        hover brighten("gui/day1_office/drawer1_idle.png")
        focus_mask True
        action Show("drawer_files_environment")
    imagebutton:
        xpos 0
        ypos 0
        idle "gui/day1_office/drawer2_idle.png"
        hover brighten("gui/day1_office/drawer2_idle.png")
        focus_mask True
        action Return("drawer2")
    imagebutton:
        xpos 0
        ypos 0
        idle "gui/day1_office/drawer3_idle.png"
        hover brighten("gui/day1_office/drawer3_idle.png")
        focus_mask True
        action Show("drawer3_environment")
    imagebutton:
        xpos 0
        ypos 0
        idle "gui/day1_office/office_returntofront.png"
        hover brighten("gui/day1_office/office_returntofront.png")
        focus_mask True
        action Return("return_to_front")
    key "K_ESCAPE" action Return("return_to_front")

screen key_holder_environment():
    modal True
    add "gui/day1_office/keys/key_holder.png"
    textbutton "Close" xalign 0.92 yalign 0.08 action Hide("key_holder_environment")
    key "K_ESCAPE" action Hide("key_holder_environment")

screen drawer_files_environment():
    modal True
    add "gui/day1_office/drawer/drawer_files.png"
    textbutton "Close" xalign 0.92 yalign 0.08 action Hide("drawer_files_environment")
    key "K_ESCAPE" action Hide("drawer_files_environment")

screen drawer3_environment():
    modal True
    add "gui/day1_office/drawer/drawer3.png"
    textbutton "Close" xalign 0.92 yalign 0.08 action Hide("drawer3_environment")
    key "K_ESCAPE" action Hide("drawer3_environment")

screen development_environment():
    modal True
    add "gui/development.png"
    textbutton "Close" xalign 0.92 yalign 0.08 action Hide("development_environment")
    key "K_ESCAPE" action Hide("development_environment")

screen day1_warehouse_investigation():
    # --- CLUES ---
    imagebutton xpos 780 ypos 950 idle "gui/warehouse/clue_paint.png" hover brighten("gui/warehouse/clue_paint.png") action Return("paint_can") at Transform(zoom=0.08)

    # --- HIDDEN EVIDENCE ---
    if not evidence_lighter:
        imagebutton xpos 300 ypos 960 idle "gui/warehouse/evidence_lighter.png" hover brighten("gui/warehouse/evidence_lighter.png") action [Notify("You got a lighter."), Return("lighter")] at Transform(zoom=0.06)

    # --- WITNESSES ---
    imagebutton xpos 1450 ypos 850 idle "gui/warehouse/driver.png" hover brighten("gui/warehouse/driver.png") action Return("driver") at Transform(zoom=0.15)
    imagebutton xpos 0 ypos 0 idle "gui/warehouse/warehouse_guard_idle.png" hover brighten("gui/warehouse/warehouse_guard_idle.png") focus_mask True action Return("watchman")

    # --- ENVIRONMENT NAVIGATION ---
    imagebutton xpos 0 ypos 0 idle "gui/warehouse/warehouse_grafitti_idle.png" hover brighten("gui/warehouse/warehouse_grafitti_idle.png") focus_mask True action Return("warehouse_graffiti")
    imagebutton xpos 0 ypos 0 idle "gui/warehouse/warehouse_windows_idle.png" hover brighten("gui/warehouse/warehouse_windows_idle.png") focus_mask True action Return("warehouse_windows")
    imagebutton xpos 0 ypos 0 idle "gui/warehouse/warehouse_door_idle.png" hover brighten("gui/warehouse/warehouse_door_idle.png") focus_mask True action Return("warehouse_door")
    imagebutton xpos 0 ypos 0 idle "gui/warehouse/warehouse_tower_idle.png" hover brighten("gui/warehouse/warehouse_tower_idle.png") focus_mask True action Return("warehouse_tower")
    imagebutton xpos 0 ypos 0 idle "gui/warehouse/warehouse_back_idle.png" hover brighten("gui/warehouse/warehouse_back_idle.png") focus_mask True action Return("warehouse_back")
    imagebutton xpos 0 ypos 0 idle "gui/warehouse/warehouse_office_idle.png" hover brighten("gui/warehouse/warehouse_office_idle.png") focus_mask True action Return("warehouse_office")

    # --- EXIT BUTTON ---
    if len(day1_clues_found) > 0 and len(day1_witnesses_found) > 0:
        imagebutton xalign 0.5 yalign 0.95 idle "gui/warehouse/ui_button_write_idle.png" hover brighten("gui/warehouse/ui_button_write_idle.png") action Return("newsroom")
       
    # --- TOGGLES ---
    imagebutton xalign 0.95 yalign 0.05 idle "gui/warehouse/ui_icon_notepad_idle.png" hover brighten("gui/warehouse/ui_icon_notepad_idle.png") action ToggleScreen("reporters_notepad") at Transform(zoom=0.1)
    imagebutton xalign 0.88 yalign 0.05 idle "gui/warehouse/ui_icon_bag_idle.png" hover brighten("gui/warehouse/ui_icon_bag_idle.png") action ToggleScreen("inventory_bag") at Transform(zoom=0.1)


# ==========================================
# NOTEPAD & BAG SCREENS
# ==========================================
screen reporters_notepad():
    add Solid("#00000088")
    add "gui/warehouse/ui_notepad.png" align (0.5, 0.5)
    imagebutton:
        align (0.75, 0.25)
        idle "gui/warehouse/ui_close_idle.png"
        hover "gui/warehouse/ui_close_hover.png"
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
    add "gui/warehouse/ui_bag_bg.png" align (0.5, 0.5)
    imagebutton:
        align (0.75, 0.25)
        idle "gui/warehouse/ui_close_idle.png"
        hover "gui/warehouse/ui_close_hover.png"
        action Hide("inventory_bag")
       
    vbox:
        xalign 0.5 ypos 300
        spacing 15
        text "Physical Evidence Bag" size 32 bold True color "#155dfc"
       
        for item in inventory_bag_items:
            text "• [item]" size 24 color "#6a7282"
           
        if len(inventory_bag_items) == 0:
            text "The bag is empty." size 24 color "#6a7282" italic True


# ==========================================
# DAY 2 MARKET PLAZA SCREENS
# ==========================================
screen day2_market_investigation():
    # --- ITEMS IN PLAZA FRONT (Always Visible) ---
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/plaza_front/item_lottery.png" hover brighten("gui/day2_plaza/plaza_front/item_lottery.png") focus_mask True action Return("lottery")
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/plaza_front/item_cigar.png" hover brighten("gui/day2_plaza/plaza_front/item_cigar.png") focus_mask True action Return("cigar")

    # --- WITNESSES IN PLAZA FRONT ---
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/plaza_front/shopper.png" hover brighten("gui/day2_plaza/plaza_front/shopper.png") focus_mask True action Return("shopper")
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/plaza_front/musician.png" hover brighten("gui/day2_plaza/plaza_front/musician.png") focus_mask True action Return("musician")
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/plaza_front/arthur.png" hover brighten("gui/day2_plaza/plaza_front/arthur.png") focus_mask True action Return("arthur")

    # --- NAVIGATION DOORS / STALLS ---
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/plaza_front/goto_ruined_stall.png" hover brighten("gui/day2_plaza/plaza_front/goto_ruined_stall.png") focus_mask True action Return("ruined_stall")
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/plaza_front/goto_bakery.png" hover brighten("gui/day2_plaza/plaza_front/goto_bakery.png") focus_mask True action Return("bakery")
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/plaza_front/goto_electric_shop.png" hover brighten("gui/day2_plaza/plaza_front/goto_electric_shop.png") focus_mask True action Return("electric_shop")

    # --- EXIT BUTTON ---
    if len(day2_clues_found) > 0 and len(day2_items_found) > 0 and len(day2_witnesses_found) > 0:
        imagebutton xalign 0.5 yalign 0.95 idle "gui/warehouse/ui_button_write_idle.png" hover brighten("gui/warehouse/ui_button_write_idle.png") action Return("newsroom")
       
    # --- TOGGLES ---
    imagebutton xalign 0.95 yalign 0.05 idle "gui/warehouse/ui_icon_notepad_idle.png" hover brighten("gui/warehouse/ui_icon_notepad_idle.png") action ToggleScreen("reporters_notepad") at Transform(zoom=0.1)
    imagebutton xalign 0.88 yalign 0.05 idle "gui/warehouse/ui_icon_bag_idle.png" hover brighten("gui/warehouse/ui_icon_bag_idle.png") action ToggleScreen("inventory_bag") at Transform(zoom=0.1)

screen day2_ruined_stall_environment():
    # --- CLUES (Always Visible) ---
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/ruined_stall/clue_gascan.png" hover brighten("gui/day2_plaza/ruined_stall/clue_gascan.png") focus_mask True action Return("gascan")
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/ruined_stall/clue_toycar.png" hover brighten("gui/day2_plaza/ruined_stall/clue_toycar.png") focus_mask True action Return("toycar")

    # --- DISAPPEARING CAMERA ---
    if "The Melted Camera" not in inventory_bag_items:
        imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/ruined_stall/item_camera.png" hover brighten("gui/day2_plaza/ruined_stall/item_camera.png") focus_mask True action [Notify("You got the Melted Camera."), Return("camera")]

    # --- CASH REGISTER (Leads to Extortion Letter) ---
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/ruined_stall/cashier_idle.png" hover brighten("gui/day2_plaza/ruined_stall/cashier_idle.png") focus_mask True action Return("cashier")

    # --- WITNESS ---
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/ruined_stall/vendor.png" hover brighten("gui/day2_plaza/ruined_stall/vendor.png") focus_mask True action Return("vendor")

    # --- RETURN ---
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/ruined_stall/return_to_plaza.png" hover brighten("gui/day2_plaza/ruined_stall/return_to_plaza.png") focus_mask True action Return("return_to_plaza")
    key "K_ESCAPE" action Return("return_to_plaza")

screen day2_cashier_environment():
    if not evidence_letter:
        imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/ruined_stall/evidence_letter.png" hover brighten("gui/day2_plaza/ruined_stall/evidence_letter.png") focus_mask True action [Notify("You got the Extortion Letter."), Return("letter")]

    textbutton "Back" xalign 0.92 yalign 0.08 action Return("back_to_stall")
    key "K_ESCAPE" action Return("back_to_stall")

screen day2_bakery_environment():
    # --- CLUE (Always Visible) ---
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/bakery/clue_oil.png" hover brighten("gui/day2_plaza/bakery/clue_oil.png") focus_mask True action Return("oil")

    # --- WITNESS ---
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/bakery/baker.png" hover brighten("gui/day2_plaza/bakery/baker.png") focus_mask True action Return("baker")

    # --- RETURN ---
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/bakery/return_to_plaza.png" hover brighten("gui/day2_plaza/bakery/return_to_plaza.png") focus_mask True action Return("return_to_plaza")
    key "K_ESCAPE" action Return("return_to_plaza")

screen day2_electric_shop_environment():
    # --- ELECTRONIC MAN (Give Broken Camera to Recover Blurry Photo) ---
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/electric_shop/electronic_man.png" hover brighten("gui/day2_plaza/electric_shop/electronic_man.png") focus_mask True action Return("electronic_man")

    # --- RETURN ---
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/electric_shop/return_to_plaza.png" hover brighten("gui/day2_plaza/electric_shop/return_to_plaza.png") focus_mask True action Return("return_to_plaza")
    key "K_ESCAPE" action Return("return_to_plaza")

screen day2_blurry_photo_overlay():
    modal True
    add Solid("#00000088")
    add "gui/day2_plaza/ruined_stall/blurry_photo.png" align (0.5, 0.5)
    textbutton "Close" xalign 0.92 yalign 0.08 action Return()
    key "K_ESCAPE" action Return()


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