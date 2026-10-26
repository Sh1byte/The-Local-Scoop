default current_day = 1

init python:
    def brighten(image_path, amount=0.2):
        return Transform(image_path, matrixcolor=BrightnessMatrix(amount))

    def hide_all_investigation_screens():
        screens_to_hide = [
            # Popups & Tutorial
            "inventory_bag", "news_van_screen", "tutorial_office_environment",
            # Day 1 Screens & Overlays
            "day1_warehouse_investigation", "day1_warehouse_back_environment",
            "day1_warehouse_riverclose_environment", "day1_warehouse_inside_front_environment",
            "day1_warehouse_inside_back_environment", "day1_warehouse_garage_environment",
            "day1_warehouse_tower_environment", "day1_warehouse_office_environment",
            "tower_clipboard_overlay", "flashlight_environment",
            "flashlight_open_environment", "flashlight_empty_environment",
            "key_holder_environment", "drawer_files_environment",
            "drawer3_environment", "development_environment",
            # Day 2 Screens & Overlays
            "day2_market_investigation", "day2_ruined_stall_environment",
            "day2_cashier_environment", "day2_zoomstall_view",
            "day2_extortion_letter_view", "day2_another_stall_view",
            "day2_bakery_environment", "day2_bakery_kitchen_environment",
            "day2_electric_shop_environment", "day2_townhall_environment",
            "day2_townhall_inside_environment", "day2_plaza_return",
            "day2_bench_environment", "day2_blurry_photo_overlay",
            # Day 3 Screens & Overlays
            "day3_outside_casino", "day3_casino_lobby",
            "day3_cashier_environment", "day3_underground_casino",
            "day3_backroom_environment", "day3_safe_closeup_environment",
            "day3_opened_safe_environment", "safe_puzzle_screen",
            "day3_playroom_environment", "day3_cards_closeup_environment",
            "day3_club_front_environment", "day3_club_inside_environment",
            "day3_wire_minigame_screen", "backroom_environment",
            "safe_closeup_environment",
            # Day 5 Screens & Overlays
            "day5_depot_investigation", "day5_maintenance_bay_environment",
            "day5_oilleak_closeup_environment", "day5_abandoned_tracks_environment",
            "day5_tracks_closeup_environment", "day5_grass_closeup_environment",
            "day5_triage_environment", "day5_crate_closeup_environment",
            "day5_triage_tent_environment", "day5_coat_closeup_environment"
        ]
        for scr in screens_to_hide:
            renpy.hide_screen(scr)

    # Icon mapping for the Inventory Grid UI
    item_icons = {
        "Battery": "gui/icons/battery.png",
        "The Janitor's Keyring": "gui/icons/keyring.png",
        "The Broken Pocket Watch": "gui/icons/watch.png",
        "The Lost Dog Collar": "gui/icons/collar.png",
        "The Brass Lighter": "gui/icons/lighter.png",
        "Bread": "gui/icons/bread.png",
        "The Melted Camera": "gui/icons/camera.png",
        "Blurry Photograph": "gui/icons/photo.png",
        "The Expensive Cigar": "gui/icons/cigar.png",
        "The Dropped Lottery Ticket": "gui/icons/ticket.png",
        "The Extortion Letter": "gui/icons/letter.png",
        "The Rusty Toolbox": "gui/icons/toolbox.png",
        "The Empty Wallet": "gui/icons/wallet.png",
        "The Burner Phone": "gui/icons/phone.png",
        "The Train Ticket Stub": "gui/icons/ticketstub.png"
    }

screen global_hud():
    zorder 100

    # Top-Left Settings Button (1080x1080 scaled to ~81x81px; hides while News Van overlay is open)
    if not renpy.get_screen("news_van_screen"):
        imagebutton:
            xalign 0.02
            yalign 0.04
            idle "gui/icons/settings.png"
            hover brighten("gui/icons/settings.png")
            hover_sound "audio/ui_hover.ogg"
            activate_sound "audio/ui_click.ogg"
            action [SetVariable("save_name", "Day " + str(current_day)), ShowMenu("scoop_settings_menu")]
            at Transform(zoom=0.075)

    if current_day != 4:
        # Persistent Bag Icon (Top-Right)
        imagebutton:
            xalign 0.88
            yalign 0.05
            idle "gui/warehouse/ui_icon_bag_idle.png"
            hover brighten("gui/warehouse/ui_icon_bag_idle.png")
            hover_sound "audio/ui_hover.ogg"
            action [If(renpy.get_screen("inventory_bag"), Play("sound", "audio/ui_bag_close.ogg"), Play("sound", "audio/ui_bag_open.ogg")), ToggleScreen("inventory_bag")]
            at Transform(zoom=0.1)

        # News Van Icon (Top-Right)
        imagebutton:
            xalign 0.95
            yalign 0.05
            idle "gui/warehouse/ui_icon_van_idle.png"
            hover brighten("gui/warehouse/ui_icon_van_idle.png")
            hover_sound "audio/ui_hover.ogg"
            activate_sound "audio/sfx_van_door.ogg"
            action Show("news_van_screen")
            at Transform(zoom=0.1)
                   
screen news_van_screen():
    modal True
    zorder 150
   
    python:
        # Check if the player has gathered enough core evidence based on the current day
        can_write = False
        if current_day == 1 and len(day1_clues_found) > 0 and len(day1_items_found) > 0 and len(day1_witnesses_found) > 0:
            can_write = True
        elif current_day == 2 and len(day2_clues_found) > 0 and len(day2_items_found) > 0 and len(day2_witnesses_found) > 0:
            can_write = True
        elif current_day == 3 and len(day3_clues_found) > 0 and len(day3_items_found) > 0 and any(w in day3_witnesses_found for w in ["Dealer 1", "Cleaner 1", "Waitress 1", "Drunk Patron 1"]):
            can_write = True
        elif current_day == 5 and len(day5_clues_found) > 0 and len(day5_items_found) > 0 and len(day5_witnesses_found) > 0:
            can_write = True

    if can_write:
        # Normal Background when ready to write
        add "gui/warehouse/bg van.jpg"
       
        # Show typewriter to create the news (hides all active room cutouts before jumping)
        imagebutton xalign 0.5 yalign 0.5 idle "gui/warehouse/typwriter_idle.png" hover brighten("gui/warehouse/typwriter_idle.png") action [Function(hide_all_investigation_screens), Jump("newspaper_minigame_router")]
       
    else:
        # Blurred Background with Dark Overlay when evidence is missing
        add "gui/warehouse/bg van.jpg" at Transform(blur=15)
        add Solid("#000000AA")
       
        # Not enough evidence notification
        text "(The evidence isn't enough to create a good story, maybe I should look for more)" xalign 0.5 yalign 0.5 size 30 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]

    # Button to leave the van cutout
    textbutton "Leave Van" xalign 0.02 yalign 0.05 action Hide("news_van_screen") text_size 30 text_color "#FFF"

label newspaper_minigame_router:
    $ hide_all_investigation_screens()
    if current_day == 1:
        jump day1_newspaper_minigame
    elif current_day == 2:
        jump day2_newspaper_minigame
    elif current_day == 3:
        jump day3_newspaper_minigame
    elif current_day == 5:
        jump day5_morning_newspaper

# ==========================================
# DAY 1 WAREHOUSE SCREENS
# ==========================================
screen day1_warehouse_back_environment():
    imagebutton xpos 0 ypos 0 idle "gui/day1_back_warehouse/fisherman.png" hover brighten("gui/day1_back_warehouse/fisherman.png") focus_mask True action Return("fisherman")
    imagebutton xpos 0 ypos 0 idle im.Scale("gui/day1_back_warehouse/river_idle.png", 1920, 1072) hover brighten(im.Scale("gui/day1_back_warehouse/river_idle.png", 1920, 1072)) focus_mask True action Return("river")
    imagebutton xpos 0 ypos 0 idle "gui/day1_back_warehouse/warehouse_inside_from_back.png" hover brighten("gui/day1_back_warehouse/warehouse_inside_from_back.png") focus_mask True action Return("warehouse_inside_from_the_back")
    imagebutton xpos 0 ypos 0 idle "gui/day1_back_warehouse/garage_back_warehouse.png" hover brighten("gui/day1_back_warehouse/garage_back_warehouse.png") focus_mask True action Return("garage_back_warehouse")
    imagebutton xpos 0 ypos 0 idle "gui/day1_back_warehouse/return_to_front.png" hover brighten("gui/day1_back_warehouse/return_to_front.png") focus_mask True action Return("back_to_front")
   
    if "The Lost Dog Collar" not in inventory_bag_items:
        imagebutton xpos 800 ypos 890 idle "gui/warehouse/item_collar.png" hover brighten("gui/warehouse/item_collar.png") action Return("collar") at Transform(zoom=0.08)
       
    key "K_ESCAPE" action Return("back_to_front")

screen day1_warehouse_riverclose_environment():
    if "The Broken Pocket Watch" not in inventory_bag_items:
        imagebutton xpos 0 ypos 0 idle "gui/day1_back_warehouse/item_watch_idle.png" hover brighten("gui/day1_back_warehouse/item_watch_idle.png") focus_mask True action Return("watch")
    textbutton "Back" xalign 0.95 yalign 0.05 action Return("return_to_back")
    key "K_ESCAPE" action Return("return_to_back")

screen day1_warehouse_inside_front_environment():
    if not janitor_helped:
        imagebutton xpos 0 ypos 0 idle "gui/day1_inside_warehouse/janitor.png" hover brighten("gui/day1_inside_warehouse/janitor.png") focus_mask True action Return("janitor")
        
    if not whiskey_cleared:
        imagebutton xpos 0 ypos 0 idle "gui/day1_inside_warehouse/clue_whiskey_idle.png" hover brighten("gui/day1_inside_warehouse/clue_whiskey_idle.png") focus_mask True action Return("whiskey")
    if not pizza_cleared:
        imagebutton xpos 0 ypos 0 idle "gui/day1_inside_warehouse/clue_pizza_idle.png" hover brighten("gui/day1_inside_warehouse/clue_pizza_idle.png") focus_mask True action Return("pizza")
    if not paint_cleared:
        imagebutton xpos 0 ypos 0 idle "gui/day1_inside_warehouse/clue_paint_idle.png" hover brighten("gui/day1_inside_warehouse/clue_paint_idle.png") focus_mask True action Return("paint_can")
    key "K_ESCAPE" action Return("return_to_front")

screen day1_warehouse_inside_back_environment():
    if not janitor_helped:
        imagebutton xpos 0 ypos 0 idle "gui/day1_inside_warehouse/janitor.png" hover brighten("gui/day1_inside_warehouse/janitor.png") focus_mask True action Return("janitor")
        
    if not whiskey_cleared:
        imagebutton xpos 0 ypos 0 idle "gui/day1_inside_warehouse/clue_whiskey_idle.png" hover brighten("gui/day1_inside_warehouse/clue_whiskey_idle.png") focus_mask True action Return("whiskey")
    if not pizza_cleared:
        imagebutton xpos 0 ypos 0 idle "gui/day1_inside_warehouse/clue_pizza_idle.png" hover brighten("gui/day1_inside_warehouse/clue_pizza_idle.png") focus_mask True action Return("pizza")
    if not paint_cleared:
        imagebutton xpos 0 ypos 0 idle "gui/day1_inside_warehouse/clue_paint_idle.png" hover brighten("gui/day1_inside_warehouse/clue_paint_idle.png") focus_mask True action Return("paint_can")
    key "K_ESCAPE" action Return("return_to_back")

screen day1_warehouse_garage_environment():
    add "gui/day1_garage_warehouse/bg_garage_warehouse.png"
    imagebutton xpos 0 ypos 0 idle "gui/day1_garage_warehouse/batterycharger_idle.png" hover brighten("gui/day1_garage_warehouse/batterycharger_idle.png") focus_mask True action Return("battery_charger")
    imagebutton xpos 0 ypos 0 idle "gui/day1_garage_warehouse/boxesgarage_idle.png" hover brighten("gui/day1_garage_warehouse/boxesgarage_idle.png") focus_mask True action Return("garage_boxes")
    imagebutton xpos 0 ypos 0 idle "gui/day1_garage_warehouse/driver.png" hover brighten("gui/day1_garage_warehouse/driver.png") focus_mask True action Return("garage_driver")
    imagebutton xpos 0 ypos 0 idle "gui/day1_garage_warehouse/garageclipboard_idle.png" hover brighten("gui/day1_garage_warehouse/garageclipboard_idle.png") focus_mask True action Return("garage_clipboard")
    imagebutton xpos 0 ypos 0 idle "gui/day1_garage_warehouse/office_garage_idle.png" hover brighten("gui/day1_garage_warehouse/office_garage_idle.png") focus_mask True action Return("garage_office")
    imagebutton xpos 0 ypos 0 idle "gui/day1_garage_warehouse/return_to_back_idle.png" hover brighten("gui/day1_garage_warehouse/return_to_back_idle.png") focus_mask True action Return("return_to_back")
    key "K_ESCAPE" action Return("return_to_back")
   
screen tower_clipboard_overlay():
    modal True
    add "gui/day_tower_warehouse/flashlight/clipboard.png" xalign 0.5 yalign 0.5
    textbutton "Close" xalign 0.92 yalign 0.08 action Hide("tower_clipboard_overlay")
    key "K_ESCAPE" action Hide("tower_clipboard_overlay")

screen flashlight_environment():
    modal True
    add "gui/day_tower_warehouse/flashlight/flashlight.png"
    imagebutton xpos 0 ypos 0 idle "gui/day_tower_warehouse/flashlight/fl_open_idle.png" hover brighten("gui/day_tower_warehouse/flashlight/fl_open_idle.png") focus_mask True action If(battery_obtained, Show("flashlight_empty_environment"), Show("flashlight_open_environment"))
    textbutton "Close" xalign 0.92 yalign 0.08 action Hide("flashlight_environment")
    key "K_ESCAPE" action Hide("flashlight_environment")

screen flashlight_open_environment():
    modal True
    add "gui/day_tower_warehouse/flashlight/flashlight_open.png"
    imagebutton xpos 0 ypos 0 idle "gui/day_tower_warehouse/flashlight/fl_empty_idle.png" hover brighten("gui/day_tower_warehouse/flashlight/fl_empty_idle.png") focus_mask True action Show("flashlight_empty_environment")
    textbutton "Close" xalign 0.92 yalign 0.08 action [
        Hide("flashlight_open_environment"),
        Hide("flashlight_environment")
    ]
    key "K_ESCAPE" action [
        Hide("flashlight_open_environment"),
        Hide("flashlight_environment")
    ]

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
    imagebutton xpos 0 ypos 0 idle "gui/day_tower_warehouse/tower_clipboard.png" hover brighten("gui/day_tower_warehouse/tower_clipboard.png") focus_mask True action Show("tower_clipboard_overlay")
    imagebutton xpos 0 ypos 0 idle "gui/day_tower_warehouse/tower_flashlight.png" hover brighten("gui/day_tower_warehouse/tower_flashlight.png") focus_mask True action If(battery_obtained, Show("flashlight_empty_environment"), Show("flashlight_environment"))
    key "K_ESCAPE" action Return("return_to_front")

screen day1_warehouse_office_environment():
    if office_empty:
        add "gui/day1_office/bg_office_empty.png"
    else:
        add "gui/day1_office/bg_office.png"
        imagebutton xpos 0 ypos 0 idle "gui/day1_office/officerguy.png" hover brighten("gui/day1_office/officerguy.png") focus_mask True action Return("officerguy")
    imagebutton xpos 0 ypos 0 idle "gui/day1_office/desktop_office_idle.png" hover brighten("gui/day1_office/desktop_office_idle.png") focus_mask True action Show("development_environment")
    imagebutton xpos 0 ypos 0 idle "gui/day1_office/keyholder_idle.png" hover brighten("gui/day1_office/keyholder_idle.png") focus_mask True action Show("key_holder_environment")
    imagebutton xpos 0 ypos 0 idle "gui/day1_office/desk_drawer1_idle.png" hover brighten("gui/day1_office/desk_drawer1_idle.png") focus_mask True action Show("development_environment")
    imagebutton xpos 0 ypos 0 idle "gui/day1_office/desk_drawer2_idle.png" hover brighten("gui/day1_office/desk_drawer2_idle.png") focus_mask True action Show("development_environment")
    imagebutton xpos 0 ypos 0 idle "gui/day1_office/drawer1_idle.png" hover brighten("gui/day1_office/drawer1_idle.png") focus_mask True action Show("drawer_files_environment")
    imagebutton xpos 0 ypos 0 idle "gui/day1_office/drawer2_idle.png" hover brighten("gui/day1_office/drawer2_idle.png") focus_mask True action Return("drawer2")
    imagebutton xpos 0 ypos 0 idle "gui/day1_office/drawer3_idle.png" hover brighten("gui/day1_office/drawer3_idle.png") focus_mask True action Show("drawer3_environment")
    imagebutton xpos 0 ypos 0 idle "gui/day1_office/office_returntofront.png" hover brighten("gui/day1_office/office_returntofront.png") focus_mask True action Return("return_to_front")
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
    if not evidence_lighter:
        imagebutton xpos 300 ypos 960 idle "gui/warehouse/evidence_lighter.png" hover brighten("gui/warehouse/evidence_lighter.png") action [Notify("You got a lighter."), Return("lighter")] at Transform(zoom=0.04)
    imagebutton xpos 0 ypos 0 idle "gui/warehouse/warehouse_guard_idle.png" hover brighten("gui/warehouse/warehouse_guard_idle.png") focus_mask True action Return("watchman")
    imagebutton xpos 0 ypos 0 idle "gui/warehouse/warehouse_grafitti_idle.png" hover brighten("gui/warehouse/warehouse_grafitti_idle.png") focus_mask True action Return("warehouse_graffiti")
    imagebutton xpos 0 ypos 0 idle "gui/warehouse/warehouse_windows_idle.png" hover brighten("gui/warehouse/warehouse_windows_idle.png") focus_mask True action Return("warehouse_windows")
    imagebutton xpos 0 ypos 0 idle "gui/warehouse/warehouse_door_idle.png" hover brighten("gui/warehouse/warehouse_door_idle.png") focus_mask True action Return("warehouse_door")
    imagebutton xpos 0 ypos 0 idle "gui/warehouse/warehouse_tower_idle.png" hover brighten("gui/warehouse/warehouse_tower_idle.png") focus_mask True action Return("warehouse_tower")
    imagebutton xpos 0 ypos 0 idle "gui/warehouse/warehouse_back_idle.png" hover brighten("gui/warehouse/warehouse_back_idle.png") focus_mask True action Return("warehouse_back")
    imagebutton xpos 0 ypos 0 idle "gui/warehouse/warehouse_office_idle.png" hover brighten("gui/warehouse/warehouse_office_idle.png") focus_mask True action Return("warehouse_office")
    
# ==========================================
# BAG SCREEN
# ==========================================
screen inventory_bag():
    add Solid("#00000088")
    add "gui/warehouse/ui_bag_bg.png" align (0.5, 0.5)
   
    imagebutton:
        align (0.78, 0.15)
        idle "gui/warehouse/ui_close_idle.png"
        hover "gui/warehouse/ui_close_hover.png"
        action Hide("inventory_bag")
       
    # Dictionary of descriptions that pop up when clicking an item
    python:
        item_descriptions = {
            "Battery": "A heavy industrial battery. It might power something.",
            "The Janitor's Keyring": "A keyring with a master key attached. Could unlock doors or drawers.",
            "The Broken Pocket Watch": "An expensive watch. Talk about the 'flow' of time.",
            "The Lost Dog Collar": "A dirty pet collar. I wonder if it belongs to a dog that was here.",
            "The Brass Lighter": "Engraved with a skull and crossed wrenches. A crucial piece of evidence.",
            "Bread": "Some leftover bread. Maybe I can use this to feed a hungry animal.",
            "The Melted Camera": "The casing is melted, but the memory chip inside might survive.",
            "Blurry Photograph": "A blurry photo recovered from the melted camera. Shows the fire starting.",
            "The Expensive Cigar": "A half-smoked, imported cigar dropped nearby.",
            "The Dropped Lottery Ticket": "A winning scratch ticket.",
            "The Extortion Letter": "Signed with the blue anchor stamp of The River Boys.",
            "The Rusty Toolbox": "Heavy junk left behind by a mechanic. It adds nothing to my story.",
            "The Empty Wallet": "A pickpocket's discarded trash that distracts from the big picture.",
            "The Burner Phone": "Dropped near the medical supplies, confirming a massive gang war at the shipping docks at midnight.",
            "The Train Ticket Stub": "Found in the injured driver's pocket, proving the gangs were planning to leave town."
        }
       
    vpgrid:
        cols 5
        spacing 0
        xpos 575
        ypos 210
       
        for item in inventory_bag_items:
            fixed:
                xysize (170, 140)
               
                if item in item_icons and renpy.loadable(item_icons[item]):
                    # Make the icon a clickable button that shows a notification
                    imagebutton:
                        align (0.5, 0.5)
                        idle item_icons[item]
                        hover brighten(item_icons[item])
                        action Notify(item_descriptions.get(item, "A mysterious item."))
                        at Transform(zoom=2)
                else:
                    textbutton "[item]":
                        align (0.5, 0.5)
                        text_size 16
                        text_color "#ffffff"
                        action Notify(item_descriptions.get(item, "A mysterious item."))


# ==========================================
# DAY 2 MARKET PLAZA SCREENS
# ==========================================
screen day2_market_investigation():
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/plaza_front/musician.png" hover brighten("gui/day2_plaza/plaza_front/musician.png") focus_mask True action Return("musician")
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/plaza_front/kids.png" hover brighten("gui/day2_plaza/plaza_front/kids.png") focus_mask True action Return("kids")
   
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/plaza_front/market_stalls_idle.png" hover brighten("gui/day2_plaza/plaza_front/market_stalls_idle.png") focus_mask True action Return("ruined_stall")
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/plaza_front/bakery_idle.png" hover brighten("gui/day2_plaza/plaza_front/bakery_idle.png") focus_mask True action Return("bakery")
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/plaza_front/electronics_idle.png" hover brighten("gui/day2_plaza/plaza_front/electronics_idle.png") focus_mask True action Return("electric_shop")
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/plaza_front/townhall_front.png" hover brighten("gui/day2_plaza/plaza_front/townhall_front.png") focus_mask True action Return("townhall")
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/plaza_front/bench_idle.png" hover brighten("gui/day2_plaza/plaza_front/bench_idle.png") focus_mask True action Return("bench")
   
screen day2_ruined_stall_environment():
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/market_stalls/clue_gascan_idle.png" hover brighten("gui/day2_plaza/market_stalls/clue_gascan_idle.png") focus_mask True action Return("gascan")
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/market_stalls/clue_toycar_idle.png" hover brighten("gui/day2_plaza/market_stalls/clue_toycar_idle.png") focus_mask True action Return("toycar")
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/market_stalls/zoomstall_idle.png" hover brighten("gui/day2_plaza/market_stalls/zoomstall_idle.png") focus_mask True action Return("zoomstall")
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/market_stalls/vendor_idle.png" hover brighten("gui/day2_plaza/market_stalls/vendor_idle.png") focus_mask True action Return("vendor")
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/market_stalls/townhall_fromstall_idle.png" hover brighten("gui/day2_plaza/market_stalls/townhall_fromstall_idle.png") focus_mask True action Return("townhall")
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/market_stalls/fruitstand_idle.png" hover brighten("gui/day2_plaza/market_stalls/fruitstand_idle.png") focus_mask True action Return("another_stall")
    key "K_ESCAPE" action Return("return_to_plaza")

screen day2_cashier_environment():
    if not evidence_letter:
        imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/market_stalls/ruined_stalls/extortion_letter.png" hover brighten("gui/day2_plaza/market_stalls/ruined_stalls/extortion_letter.png") focus_mask True action [Return("letter")]
    textbutton "Back" xalign 0.92 yalign 0.08 action Return("back_to_stall")
    key "K_ESCAPE" action Return("back_to_stall")

screen day2_zoomstall_view():
    if not evidence_letter:
        imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/market_stalls/ruined_stalls/evidence_letter.png" hover brighten("gui/day2_plaza/market_stalls/ruined_stalls/evidence_letter.png") focus_mask True action Return("evidence_letter")
    if renpy.loadable("gui/day2_plaza/market_stalls/ruined_stalls/item_camera.png") and "The Melted Camera" not in inventory_bag_items and not blurry_photo_obtained:
        imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/market_stalls/ruined_stalls/item_camera.png" hover brighten("gui/day2_plaza/market_stalls/ruined_stalls/item_camera.png") focus_mask True action Return("camera")
    key "K_ESCAPE" action Return("back_to_stall")

screen day2_extortion_letter_view():
    textbutton "Return" xalign 0.92 yalign 0.08 action Return("return")
    key "K_ESCAPE" action Return("return")

screen day2_another_stall_view():
    imagebutton xpos 0 ypos 0 idle "bg another_stall" action Return()
    key "K_ESCAPE" action Return()

screen day2_bakery_environment():
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/bakery/kitchen_idle.png" hover brighten("gui/day2_plaza/bakery/kitchen_idle.png") focus_mask True action Return("kitchen")
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/bakery/clerkbakery.png" hover brighten("gui/day2_plaza/bakery/clerkbakery.png") focus_mask True action Return("clerk_bakery")
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/bakery/customer1.png" hover brighten("gui/day2_plaza/bakery/customer1.png") focus_mask True action Return("customer1")
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/bakery/return_to_plaza.png" hover brighten("gui/day2_plaza/bakery/return_to_plaza.png") focus_mask True action Return("return_to_plaza")
    key "K_ESCAPE" action Return("return_to_plaza")

screen day2_bakery_kitchen_environment():
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/bakery/kitchen/clue_oil.png" hover brighten("gui/day2_plaza/bakery/kitchen/clue_oil.png") focus_mask True action Return("oil")
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/bakery/kitchen/baker.png" hover brighten("gui/day2_plaza/bakery/kitchen/baker.png") focus_mask True action Return("baker")
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/bakery/kitchen/return_to_bakery_idle.png" hover brighten("gui/day2_plaza/bakery/kitchen/return_to_bakery_idle.png") focus_mask True action Return("return_to_bakery")
    key "K_ESCAPE" action Return()

screen day2_electric_shop_environment():
    imagebutton xpos 0 ypos -10 idle "gui/day2_plaza/electric_shop/electronic_man.png" hover brighten("gui/day2_plaza/electric_shop/electronic_man.png") focus_mask True action Return("electronic_man")
    imagebutton xpos 0 ypos -10 idle "gui/day2_plaza/electric_shop/return_to_plaza.png" hover brighten("gui/day2_plaza/electric_shop/return_to_plaza.png") focus_mask True action Return("return_to_plaza")
    key "K_ESCAPE" action Return("return_to_plaza")

screen day2_townhall_environment():
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/townhall/arthur.png" hover brighten("gui/day2_plaza/townhall/arthur.png") focus_mask True action Return("arthur")
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/townhall/shopper.png" hover brighten("gui/day2_plaza/townhall/shopper.png") focus_mask True action Return("shopper")
    imagebutton xpos 0 ypos 0 idle im.Scale("gui/day2_plaza/townhall/goto_insidetownhall_idle.png", 1920, 1072) hover brighten(im.Scale("gui/day2_plaza/townhall/goto_insidetownhall_idle.png", 1920, 1072)) focus_mask True action Return("inside")
    textbutton "Return to Plaza" xalign 0.92 yalign 0.08 action Return("return_to_plaza")
    key "K_ESCAPE" action Return("return_to_plaza")

screen day2_townhall_inside_environment():
    imagebutton xpos 0 ypos 0 idle im.Scale("gui/day2_plaza/townhall/inside_townhall/photographer.png", 1920, 1072) hover brighten(im.Scale("gui/day2_plaza/townhall/inside_townhall/photographer.png", 1920, 1072)) focus_mask True action Return("photographer")
    imagebutton xpos 0 ypos 0 idle im.Scale("gui/day2_plaza/townhall/inside_townhall/return_to_thfront.png", 1920, 1072) hover brighten(im.Scale("gui/day2_plaza/townhall/inside_townhall/return_to_thfront.png", 1920, 1072)) focus_mask True action Return("return_to_thfront")
    key "K_ESCAPE" action Return("return_to_thfront")

screen day2_plaza_return():
    textbutton "Return to Plaza" xalign 0.92 yalign 0.08 action Return()
    key "K_ESCAPE" action Return()

screen day2_bench_environment():
    if "The Dropped Lottery Ticket" not in day2_items_found:
        imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/bench/item_ticket_idle.png" hover brighten("gui/day2_plaza/bench/item_ticket_idle.png") focus_mask True action Return("ticket")
           
    if "The Expensive Cigar" not in day2_items_found:
        imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/bench/item_cigarrete_idle.png" hover brighten("gui/day2_plaza/bench/item_cigarrete_idle.png") focus_mask True action Return("cigar")
           
    textbutton "Return to Plaza" xalign 0.92 yalign 0.08 action Return("return_to_plaza")
    key "K_ESCAPE" action Return("return_to_plaza")

screen day2_blurry_photo_overlay():
    modal True
    add Solid("#00000088")
    add "gui/day2_plaza//market_stalls/ruined_stalls/blurry_photo.png" align (0.5, 0.5) zoom 3
    textbutton "Close" xalign 0.92 yalign 0.08 action Return()
    key "K_ESCAPE" action Return()
    
# ==========================================
# DAY 3 CASINO SCREENS
# ==========================================

screen day3_outside_casino():
    imagebutton xpos 0 ypos 0 idle "gui/day3_casino/outside_casino/go_to_casino.png" hover brighten("gui/day3_casino/outside_casino/go_to_casino.png") focus_mask True action Return("casino")
    imagebutton xpos 0 ypos 0 idle "gui/day3_casino/outside_casino/go_to_club.png" hover brighten("gui/day3_casino/outside_casino/go_to_club.png") focus_mask True action Return("club_front")

screen day3_casino_lobby():
    imagebutton xpos 0 ypos 0 idle "gui/day3_casino/casino_lobby/go_to_cashier.png" hover brighten("gui/day3_casino/casino_lobby/go_to_cashier.png") focus_mask True action Return("cashier")
    imagebutton xpos 0 ypos 0 idle "gui/day3_casino/casino_lobby/go_to_outside_casino.png" hover brighten("gui/day3_casino/casino_lobby/go_to_outside_casino.png") focus_mask True action Return("outside")
    imagebutton xpos 0 ypos 0 idle "gui/day3_casino/casino_lobby/go_to_playroom.png" hover brighten("gui/day3_casino/casino_lobby/go_to_playroom.png") focus_mask True action Return("playroom")
   
    if slot_machine_shorted:
        imagebutton xpos 0 ypos 0 idle "gui/day3_casino/casino_lobby/go_to_underground_noBouncer.png" hover brighten("gui/day3_casino/casino_lobby/go_to_underground_noBouncer.png") focus_mask True action Return("underground")
    else:
        imagebutton xpos 0 ypos 0 idle "gui/day3_casino/casino_lobby/go_to_underground.png" hover brighten("gui/day3_casino/casino_lobby/go_to_underground.png") focus_mask True action Return("underground")

screen day3_cashier_environment():
    textbutton "Back" action Return("back") align (0.05, 0.95)

screen day3_underground_casino():
    imagebutton xpos 0 ypos 0 idle "gui/day3_casino/underground_casino/go_to_lobby.png" hover brighten("gui/day3_casino/underground_casino/go_to_lobby.png") focus_mask True action Return("lobby")
    imagebutton xpos 0 ypos 0 idle "gui/day3_casino/underground_casino/go_to_backroom.png" hover brighten("gui/day3_casino/underground_casino/go_to_backroom.png") focus_mask True action Return("backroom")
    imagebutton xpos 0 ypos 0 idle "gui/day3_casino/underground_casino/bullet_wall_idle.png" hover brighten("gui/day3_casino/underground_casino/bullet_wall_idle.png") focus_mask True action Return("bullethole")
    imagebutton xpos 0 ypos 0 idle "gui/day3_casino/underground_casino/cleaner_idle.png" hover brighten("gui/day3_casino/underground_casino/cleaner_idle.png") focus_mask True action Return("cleaner")
    imagebutton xpos 0 ypos 0 idle "gui/day3_casino/underground_casino/waitress_idle.png" hover brighten("gui/day3_casino/underground_casino/waitress_idle.png") focus_mask True action Return("waitress")
    
    if "The Stolen Credit Card" not in day3_items_found:
        imagebutton xpos 0 ypos 0 idle "gui/day3_casino/underground_casino/credit card idle.png" hover brighten("gui/day3_casino/underground_casino/credit card idle.png") focus_mask True action Return("creditcard")
   
    if "The VIP Pass" not in day3_items_found:
        imagebutton xpos 0 ypos 0 idle "gui/day3_casino/underground_casino/vip_pass_idle.png" hover brighten("gui/day3_casino/underground_casino/vip_pass_idle.png") focus_mask True action Return("vippass")

screen day3_backroom_environment():
    if safe_unlocked:
        imagebutton xpos 0 ypos 0 idle "gui/day3_casino/backroom/backroom_room/go_to_open_vault.png" hover brighten("gui/day3_casino/backroom/backroom_room/go_to_open_vault.png") focus_mask True action Return("vault")
    else:
        imagebutton xpos 0 ypos 0 idle "gui/day3_casino/backroom/backroom_room/go_to_vault.png" hover brighten("gui/day3_casino/backroom/backroom_room/go_to_vault.png") focus_mask True action Return("vault")
    
    imagebutton xpos 0 ypos 0 idle "gui/day3_casino/backroom/backroom_room/dealer_idle.png" hover brighten("gui/day3_casino/backroom/backroom_room/dealer_idle.png") focus_mask True action Return("dealer")
    imagebutton xpos 0 ypos 0 idle "gui/day3_casino/backroom/backroom_room/go_backto_underground.png" hover brighten("gui/day3_casino/backroom/backroom_room/go_backto_underground.png") focus_mask True action Return("underground")

screen day3_safe_closeup_environment():
    imagebutton xpos 0 ypos 0 idle "gui/day3_casino/backroom/safe/vault_closeup_idle.png" hover brighten("gui/day3_casino/backroom/safe/vault_closeup_idle.png") focus_mask True action Return("safe_interact")
    imagebutton xpos 0 ypos 0 idle "gui/day3_casino/backroom/safe/note_idle.png" hover brighten("gui/day3_casino/backroom/safe/note_idle.png") focus_mask True action Return("clue_paper")
    textbutton "Back" action Return("back") align (0.05, 0.95)

screen day3_opened_safe_environment():
    if not evidence_ledger:
        imagebutton xpos 0 ypos 0 idle "gui/day3_casino/backroom/safe/opened_safe/ledger_idle.png" hover brighten("gui/day3_casino/backroom/safe/opened_safe/ledger_idle.png") focus_mask True action Return("bloody_ledger")
    textbutton "Leave Safe" action Return("back") align (0.05, 0.95)

screen safe_puzzle_screen(current_digit, entered_code):
    $ rotation_angle = current_digit * -36
    # Keep the dial and arrow elements inside the minigame
    add "gui/day3_casino/backroom/safe/safe_minigame/safe_knob.png":
        xalign 0.5
        yalign 0.5
        transform_anchor True
        rotate rotation_angle
    add "gui/day3_casino/backroom/safe/safe_minigame/safe_arrow.png":
        xalign 0.5
        yalign 0.15
        
    text "Code Entered: [entered_code]" xalign 0.5 yalign 0.05 size 40 color "#ffffff"
    key "a" action Return("turn_right")
    key "A" action Return("turn_right")
    key "d" action Return("turn_left")
    key "D" action Return("turn_left")
    key "K_RETURN" action Return("enter_digit")
    key "K_KP_ENTER" action Return("enter_digit")
    key "K_ESCAPE" action Return("exit")
    
    vbox:
        align (0.95, 0.95)
        text "'A' to turn Right" color "#ffffff"
        text "'D' to turn Left" color "#ffffff"
        text "'Enter' to lock in number" color "#ffffff"
    textbutton "Back" action Return("exit") align (0.05, 0.95)

screen day3_playroom_environment():
    imagebutton xpos 0 ypos 0 idle "gui/day3_casino/casino_playroom/go_to_lobby_from_playroom.png" hover brighten("gui/day3_casino/casino_playroom/go_to_lobby_from_playroom.png") focus_mask True action Return("lobby")
    imagebutton xpos 0 ypos 0 idle "gui/day3_casino/casino_playroom/go_to_cards_closeup.png" hover brighten("gui/day3_casino/casino_playroom/go_to_cards_closeup.png") focus_mask True action Return("cards_closeup")
    imagebutton xpos 0 ypos 0 idle "gui/day3_casino/casino_playroom/go_to_wire_minigame.png" hover brighten("gui/day3_casino/casino_playroom/go_to_wire_minigame.png") focus_mask True action Return("wire_minigame")
    imagebutton xpos 0 ypos 0 idle "gui/day3_casino/casino_playroom/arthur_idle.png" hover brighten("gui/day3_casino/casino_playroom/arthur_idle.png") focus_mask True action Return("arthur")
   
    if slot_machine_shorted:
        imagebutton xpos 0 ypos 0 idle "gui/day3_casino/casino_playroom/destroyed_jukebox_bouncer.png" hover brighten("gui/day3_casino/casino_playroom/destroyed_jukebox_bouncer.png") focus_mask True action Return("jukebox")
    else:
        imagebutton xpos 0 ypos 0 idle "gui/day3_casino/casino_playroom/destroyed_jukebox_idle.png" hover brighten("gui/day3_casino/casino_playroom/destroyed_jukebox_idle.png") focus_mask True action Return("jukebox")
       
    imagebutton xpos 0 ypos 0 idle "gui/day3_casino/casino_playroom/drunk_idle.png" hover brighten("gui/day3_casino/casino_playroom/drunk_idle.png") focus_mask True action Return("drunk")

screen day3_cards_closeup_environment():
    imagebutton xpos 0 ypos 0 idle "gui/day3_casino/casino_playroom/cards_closeup/cards_idle.png" hover brighten("gui/day3_casino/casino_playroom/cards_closeup/cards_idle.png") focus_mask True action Return("cards")
    
    if "The Diamond Earring" not in day3_items_found:
        imagebutton xpos 0 ypos 0 idle "gui/day3_casino/casino_playroom/cards_closeup/earring_idle.png" hover brighten("gui/day3_casino/casino_playroom/cards_closeup/earring_idle.png") focus_mask True action Return("earring")
    textbutton "Back" action Return("back") align (0.05, 0.95)

screen day3_club_front_environment():
    imagebutton xpos 0 ypos 0 idle "gui/day3_casino/local_club/club_door_idle.png" hover brighten("gui/day3_casino/local_club/club_door_idle.png") focus_mask True action Return("inside_club")
    textbutton "Back to Outside" action Return("outside") align (0.05, 0.95)

screen day3_club_inside_environment():
    imagebutton xpos 0 ypos 0 idle "gui/day3_casino/local_club/inside_club/go_to_outside_club.png" hover brighten("gui/day3_casino/local_club/inside_club/go_to_outside_club.png") focus_mask True action Return("outside")
    imagebutton xpos -17 ypos 0 idle "gui/day3_casino/local_club/inside_club/gossiper_idle.png" hover brighten("gui/day3_casino/local_club/inside_club/gossiper_idle.png") focus_mask True action Return("gossiper")


# ==========================================
# DAY 5 DEPOT SCREENS
# ==========================================

# --- DEPOT ENTRANCE (MAIN HUB) ---
screen day5_depot_investigation():
    add "gui/day5_abandoned_station/Depot_Entrance/bg Depot_Entrance.jpg"

    # Navigation Hotspots
    imagebutton xpos 0 ypos 0 idle "gui/day5_abandoned_station/Depot_Entrance/go_to_Maintenance_Bay.png" hover brighten("gui/day5_abandoned_station/Depot_Entrance/go_to_Maintenance_Bay.png") focus_mask True action Return("go_to_maintenance_bay")
    imagebutton xpos 0 ypos 0 idle "gui/day5_abandoned_station/Depot_Entrance/go_to_Train_Tracks.png" hover brighten("gui/day5_abandoned_station/Depot_Entrance/go_to_Train_Tracks.png") focus_mask True action Return("go_to_abandoned_tracks")
    imagebutton xpos 0 ypos 0 idle "gui/day5_abandoned_station/Depot_Entrance/go_to_Triage.png" hover brighten("gui/day5_abandoned_station/Depot_Entrance/go_to_Triage.png") focus_mask True action Return("go_to_triage")

    # NPC & Witness
    imagebutton xpos 0 ypos 0 idle "gui/day5_abandoned_station/Depot_Entrance/Arthur_Day5.png" hover brighten("gui/day5_abandoned_station/Depot_Entrance/Arthur_Day5.png") focus_mask True action Return("arthur")
    imagebutton xpos 0 ypos 0 idle "gui/day5_abandoned_station/Depot_Entrance/Tourist.png" hover brighten("gui/day5_abandoned_station/Depot_Entrance/Tourist.png") focus_mask True action Return("tourist")


# --- MAINTENANCE BAY ---
screen day5_maintenance_bay_environment():
    if "The Rusty Toolbox" not in inventory_bag_items:
        add "gui/day5_abandoned_station/Maintenance_Bay/bg Maintenance_Bay_Toolbox.jpg"
        imagebutton xpos 0 ypos 0 idle "gui/day5_abandoned_station/Maintenance_Bay/Toolbox_idle.png" hover brighten("gui/day5_abandoned_station/Maintenance_Bay/Toolbox_idle.png") focus_mask True action [Notify("You got The Rusty Toolbox."), Return("toolbox")]
    else:
        add "gui/day5_abandoned_station/Maintenance_Bay/bg Maintenance_Bay_NoToolbox.jpg"

    # Close-up Hotspot (Leaking Oil Puddle)
    imagebutton xpos 0 ypos 0 idle "gui/day5_abandoned_station/Maintenance_Bay/go_to_OilLeak_CloseUp.png" hover brighten("gui/day5_abandoned_station/Maintenance_Bay/go_to_OilLeak_CloseUp.png") focus_mask True action Return("go_to_oilleak_closeup")

    # Witness: Train Engineer 1
    imagebutton xpos 0 ypos 0 idle "gui/day5_abandoned_station/Maintenance_Bay/Train_Engineer.png" hover brighten("gui/day5_abandoned_station/Maintenance_Bay/Train_Engineer.png") focus_mask True action Return("engineer")

    # Return to Depot Entrance
    imagebutton xpos 0 ypos 0 idle "gui/day5_abandoned_station/Maintenance_Bay/go_to_Depot_Entrance_MaintenanceBay.png" hover brighten("gui/day5_abandoned_station/Maintenance_Bay/go_to_Depot_Entrance_MaintenanceBay.png") focus_mask True action Return("depot_entrance")
    key "K_ESCAPE" action Return("depot_entrance")

screen day5_oilleak_closeup_environment():
    add "gui/day5_abandoned_station/Maintenance_Bay/Oil_Leak_CloseUp.jpg"
    textbutton "Back" xalign 0.05 yalign 0.95 action Return("back") text_size 30 text_color "#FFFFFF"
    key "K_ESCAPE" action Return("back")


# --- ABANDONED TRACKS ---
screen day5_abandoned_tracks_environment():
    if "The Empty Wallet" not in inventory_bag_items:
        add "gui/day5_abandoned_station/Abandoned_Tracks/bg Abandoned_Tracks_Wallet.jpg"
        imagebutton xpos 0 ypos 0 idle "gui/day5_abandoned_station/Abandoned_Tracks/go_to_Grass_CloseUp.png" hover brighten("gui/day5_abandoned_station/Abandoned_Tracks/go_to_Grass_CloseUp.png") focus_mask True action Return("go_to_grass_closeup")
    else:
        add "gui/day5_abandoned_station/Abandoned_Tracks/bg Abandoned_Tracks_NoWallet.jpg"

    # Close-up Hotspot (Tracks)
    imagebutton xpos 0 ypos 0 idle "gui/day5_abandoned_station/Abandoned_Tracks/go_to_Bloody_Tracks_CloseUp.png" hover brighten("gui/day5_abandoned_station/Abandoned_Tracks/go_to_Bloody_Tracks_CloseUp.png") focus_mask True action Return("go_to_tracks_closeup")

    # Witness: Hobo 1
    imagebutton xpos 0 ypos 0 idle "gui/day5_abandoned_station/Abandoned_Tracks/Homeless_Man_Idle.png" hover brighten("gui/day5_abandoned_station/Abandoned_Tracks/Homeless_Man_Idle.png") focus_mask True action Return("hobo")

    # Return to Depot Entrance
    imagebutton xpos 0 ypos 0 idle "gui/day5_abandoned_station/Abandoned_Tracks/go_to_Depot_Entrance.png" hover brighten("gui/day5_abandoned_station/Abandoned_Tracks/go_to_Depot_Entrance.png") focus_mask True action Return("depot_entrance")
    key "K_ESCAPE" action Return("depot_entrance")

screen day5_tracks_closeup_environment():
    add "gui/day5_abandoned_station/Abandoned_Tracks/Tracks_CloseUp.jpg"

    # Clues: Bloody Tire Tracks & Wild Dog Tracks
    imagebutton xpos 0 ypos 0 idle "gui/day5_abandoned_station/Abandoned_Tracks/Tire_Tracks.png" hover brighten("gui/day5_abandoned_station/Abandoned_Tracks/Tire_Tracks.png") focus_mask True action Return("tiretracks")
    imagebutton xpos 0 ypos 0 idle "gui/day5_abandoned_station/Abandoned_Tracks/Animal_Tracks.png" hover brighten("gui/day5_abandoned_station/Abandoned_Tracks/Animal_Tracks.png") focus_mask True action Return("dogtracks")

    textbutton "Back" xalign 0.05 yalign 0.95 action Return("back") text_size 30 text_color "#FFFFFF"
    key "K_ESCAPE" action Return("back")

screen day5_grass_closeup_environment():
    add "gui/day5_abandoned_station/Abandoned_Tracks/Grass_CloseUp_NoWallet.jpg"

    # Obtainable Item: The Empty Wallet (disappears when clicked)
    if "The Empty Wallet" not in inventory_bag_items:
        imagebutton xpos 0 ypos 0 idle "gui/day5_abandoned_station/Abandoned_Tracks/Wallet_idle.png" hover brighten("gui/day5_abandoned_station/Abandoned_Tracks/Wallet_idle.png") focus_mask True action [Notify("You got The Empty Wallet."), Return("wallet")]

    textbutton "Back" xalign 0.05 yalign 0.95 action Return("back") text_size 30 text_color "#FFFFFF"
    key "K_ESCAPE" action Return("back")


# --- MAKESHIFT TRIAGE & TENT ---
screen day5_triage_environment():
    if not evidence_phone and "The Burner Phone" not in inventory_bag_items:
        add "gui/day5_abandoned_station/Triage/bg Makeshift_Triage_Phone.jpg"
        imagebutton xpos 0 ypos 0 idle "gui/day5_abandoned_station/Triage/go_to_Crate_CloseUp.png" hover brighten("gui/day5_abandoned_station/Triage/go_to_Crate_CloseUp.png") focus_mask True action Return("go_to_crate_closeup")
    else:
        add "gui/day5_abandoned_station/Triage/bg Makeshift_Triage_NoPhone.jpg"

    # Tent Hotspot
    imagebutton xpos 0 ypos 0 idle "gui/day5_abandoned_station/Triage/go_to_Tent.png" hover brighten("gui/day5_abandoned_station/Triage/go_to_Tent.png") focus_mask True action Return("go_to_tent")

    # Witness: Medic 1
    imagebutton xpos 0 ypos 0 idle "gui/day5_abandoned_station/Triage/Medic.png" hover brighten("gui/day5_abandoned_station/Triage/Medic.png") focus_mask True action Return("medic")

    # Return to Depot Entrance
    textbutton "Back to Depot Entrance" xalign 0.05 yalign 0.95 action Return("depot_entrance") text_size 30 text_color "#FFFFFF"
    key "K_ESCAPE" action Return("depot_entrance")

screen day5_crate_closeup_environment():
    add "gui/day5_abandoned_station/Triage/Crate_CloseUp_NoPhone.jpg"

    # Obtainable Evidence Item: The Burner Phone (disappears when clicked)
    if not evidence_phone and "The Burner Phone" not in inventory_bag_items:
        imagebutton xpos 0 ypos 0 idle "gui/day5_abandoned_station/Triage/Phone_idle.png" hover brighten("gui/day5_abandoned_station/Triage/Phone_idle.png") focus_mask True action [Notify("You got The Burner Phone."), Return("phone")]

    textbutton "Back" xalign 0.05 yalign 0.95 action Return("back") text_size 30 text_color "#FFFFFF"
    key "K_ESCAPE" action Return("back")

screen day5_triage_tent_environment():
    if "The Train Ticket Stub" not in inventory_bag_items:
        add "gui/day5_abandoned_station/Triage/Tent/bg Inside_Tent_Ticket.jpg"
        imagebutton xpos 0 ypos 0 idle "gui/day5_abandoned_station/Triage/Tent/go_to_Coat_CloseUp.png" hover brighten("gui/day5_abandoned_station/Triage/Tent/go_to_Coat_CloseUp.png") focus_mask True action Return("go_to_coat_closeup")
    else:
        add "gui/day5_abandoned_station/Triage/Tent/bg Inside_Tent_NoTicket.jpg"

    # Return outside to Makeshift Triage
    imagebutton xpos 0 ypos 0 idle "gui/day5_abandoned_station/Triage/Tent/go_to_Triage_Tent.png" hover brighten("gui/day5_abandoned_station/Triage/Tent/go_to_Triage_Tent.png") focus_mask True action Return("back_to_triage")
    key "K_ESCAPE" action Return("back_to_triage")

screen day5_coat_closeup_environment():
    add "gui/day5_abandoned_station/Triage/Tent/Coat_CloseUp_NoTicket.jpg"

    # Obtainable Story Item: The Train Ticket Stub (disappears when clicked)
    if "The Train Ticket Stub" not in inventory_bag_items:
        imagebutton xpos 0 ypos 0 idle "gui/day5_abandoned_station/Triage/Tent/Ticket_idle.png" hover brighten("gui/day5_abandoned_station/Triage/Tent/Ticket_idle.png") focus_mask True action [Notify("You got The Train Ticket Stub."), Return("ticketstub")]

    textbutton "Back" xalign 0.05 yalign 0.95 action Return("back") text_size 30 text_color "#FFFFFF"
    key "K_ESCAPE" action Return("back")

screen backroom_environment():
    # Replace xpos/ypos and idle images with your exact layout hotspot assets
    imagebutton xpos 400 ypos 300 idle "safe_distant_idle.png" action Return("safe")

screen safe_closeup_environment():
    imagebutton xpos 350 ypos 250 idle "safe_closeup_idle.png" action Return("safe_interact")
    imagebutton xpos 600 ypos 450 idle "clue_paper_idle.png" action Return("clue_paper")
    textbutton "Back" action Return("back") align (0.05, 0.95)

# ==========================================
# TUTORIAL SCREENS
# ==========================================
screen tutorial_office_environment():
    imagebutton xpos 0 ypos -9 idle "gui/tutorial/files_idle.png" hover brighten("gui/tutorial/files_idle.png") focus_mask True action Return("files")
    
    # The badge disappears after it is picked up
    if not tutorial_badge_picked:
        imagebutton xpos 0 ypos -9 idle "gui/tutorial/badge_idle.png" hover brighten("gui/tutorial/badge_idle.png") focus_mask True action Return("badge")
        
    imagebutton xpos 0 ypos -9 idle "gui/tutorial/arthur_tuts_idle.png" hover brighten("gui/tutorial/arthur_tuts_idle.png") focus_mask True action Return("arthur")
    imagebutton xpos 0 ypos -9 idle "gui/tutorial/door_idle.png" hover brighten("gui/tutorial/door_idle.png") focus_mask True action Return("door")
    
    # The News Van icon acts as the "Finish Tutorial" button
    imagebutton xalign 0.95 yalign 0.05 idle "gui/tutorial/ui_icon_van_idle.png" hover brighten("gui/tutorial/ui_icon_van_idle.png") action Return("van") at Transform(zoom=0.1)

# ==========================================
# NEWSPAPER UI SCREEN
# ==========================================
screen newspaper_results_ui(headline, body, rating, score):
    # This displays your straight, un-slanted zoomed-in newspaper asset
    add "gui/newspaper_zoomed.jpg"
    
    # This aligns the text block perfectly over the straight box
    vbox:
        # Shifting the position further right (600) and slightly up (310)
        # to clear the left margin and align with the square box
        pos (600,375) 
        # Shrinking the width to 720 so text wraps before the right border
        xsize 720 
        spacing 15 # Tightened slightly for a natural read inside the vertical height
        
        # Sized nicely to look natural and not overflow
        text headline size 28 bold True color "#1a1a1a"
        text body size 18 color "#2b2b2b" line_spacing 3
        
        # Give some visual separation before the rating and score
        null height 10
        
        text "Editor's Rating: [rating]" size 22 italic True color "#590000"
        text "Total Credibility: [score]" size 22 bold True color "#1a1a1a"
        
    # Standard textbutton at the bottom, repositioned slightly to prevent conflict
    textbutton "Put away newspaper" action Return() align (0.5, 0.93) text_size 28 text_color "#ffffff" text_outlines [(2, "#000000", 0, 0)]