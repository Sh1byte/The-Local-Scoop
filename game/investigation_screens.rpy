init python:
    def brighten(image_path, amount=0.2):
        return Transform(image_path, matrixcolor=BrightnessMatrix(amount))

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
        "The Extortion Letter": "gui/icons/letter.png"
    }

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
    imagebutton xpos 0 ypos 0 idle "gui/day_tower_warehouse/flashlight/fl_open_idle.png" hover brighten("gui/day_tower_warehouse/flashlight/fl_open_idle.png") focus_mask True action Show("flashlight_open_environment")
    textbutton "Close" xalign 0.92 yalign 0.08 action Hide("flashlight_environment")
    key "K_ESCAPE" action Hide("flashlight_environment")

screen flashlight_open_environment():
    modal True
    add "gui/day_tower_warehouse/flashlight/flashlight_open.png"
    imagebutton xpos 0 ypos 0 idle "gui/day_tower_warehouse/flashlight/fl_empty_idle.png" hover brighten("gui/day_tower_warehouse/flashlight/fl_empty_idle.png") focus_mask True action Show("flashlight_empty_environment")
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
    imagebutton xpos 0 ypos 0 idle "gui/day_tower_warehouse/tower_clipboard.png" hover brighten("gui/day_tower_warehouse/tower_clipboard.png") focus_mask True action Show("tower_clipboard_overlay")
    imagebutton xpos 0 ypos 0 idle "gui/day_tower_warehouse/tower_flashlight.png" hover brighten("gui/day_tower_warehouse/tower_flashlight.png") focus_mask True action Show("flashlight_environment")
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
        imagebutton xpos 300 ypos 960 idle "gui/warehouse/evidence_lighter.png" hover brighten("gui/warehouse/evidence_lighter.png") action [Notify("You got a lighter."), Return("lighter")] at Transform(zoom=0.06)
    imagebutton xpos 0 ypos 0 idle "gui/warehouse/warehouse_guard_idle.png" hover brighten("gui/warehouse/warehouse_guard_idle.png") focus_mask True action Return("watchman")
    imagebutton xpos 0 ypos 0 idle "gui/warehouse/warehouse_grafitti_idle.png" hover brighten("gui/warehouse/warehouse_grafitti_idle.png") focus_mask True action Return("warehouse_graffiti")
    imagebutton xpos 0 ypos 0 idle "gui/warehouse/warehouse_windows_idle.png" hover brighten("gui/warehouse/warehouse_windows_idle.png") focus_mask True action Return("warehouse_windows")
    imagebutton xpos 0 ypos 0 idle "gui/warehouse/warehouse_door_idle.png" hover brighten("gui/warehouse/warehouse_door_idle.png") focus_mask True action Return("warehouse_door")
    imagebutton xpos 0 ypos 0 idle "gui/warehouse/warehouse_tower_idle.png" hover brighten("gui/warehouse/warehouse_tower_idle.png") focus_mask True action Return("warehouse_tower")
    imagebutton xpos 0 ypos 0 idle "gui/warehouse/warehouse_back_idle.png" hover brighten("gui/warehouse/warehouse_back_idle.png") focus_mask True action Return("warehouse_back")
    imagebutton xpos 0 ypos 0 idle "gui/warehouse/warehouse_office_idle.png" hover brighten("gui/warehouse/warehouse_office_idle.png") focus_mask True action Return("warehouse_office")
    
    if len(day1_clues_found) > 0 and len(day1_witnesses_found) > 0:
        imagebutton xalign 0.5 yalign 0.95 idle "gui/warehouse/ui_button_write_idle.png" hover brighten("gui/warehouse/ui_button_write_idle.png") action Return("newsroom")
       
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
            "The Extortion Letter": "Signed with the blue anchor stamp of The River Boys."
        }
       
    vpgrid:
        cols 5
        spacing 0
        xpos 575
        ypos 210
       
        for item in inventory_bag_items:
            fixed:
                xysize (170, 140)
               
                if item in item_icons:
                    # Make the icon a clickable button that shows a notification
                    imagebutton:
                        align (0.5, 0.5)
                        idle item_icons[item]
                        hover brighten(item_icons[item])
                        action Notify(item_descriptions.get(item, "A mysterious item."))
                        at Transform(zoom=2)
                else:
                    text "[item]" size 16 color "#ffffff" align (0.5, 0.5)


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
   
    if len(day2_clues_found) > 0 and len(day2_witnesses_found) > 0:
        imagebutton xalign 0.5 yalign 0.95 idle "gui/warehouse/ui_button_write_idle.png" hover brighten("gui/warehouse/ui_button_write_idle.png") action Return("newsroom")
       
    imagebutton xalign 0.95 yalign 0.05 idle "gui/warehouse/ui_icon_notepad_idle.png" hover brighten("gui/warehouse/ui_icon_notepad_idle.png") action ToggleScreen("reporters_notepad") at Transform(zoom=0.1)
    imagebutton xalign 0.88 yalign 0.05 idle "gui/warehouse/ui_icon_bag_idle.png" hover brighten("gui/warehouse/ui_icon_bag_idle.png") action ToggleScreen("inventory_bag") at Transform(zoom=0.1)

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
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/electric_shop/electronic_man.png" hover brighten("gui/day2_plaza/electric_shop/electronic_man.png") focus_mask True action Return("electronic_man")
    imagebutton xpos 0 ypos 0 idle "gui/day2_plaza/electric_shop/return_to_plaza.png" hover brighten("gui/day2_plaza/electric_shop/return_to_plaza.png") focus_mask True action Return("return_to_plaza")
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

screen backroom_environment():
    # Replace xpos/ypos and idle images with your exact layout hotspot assets
    imagebutton xpos 400 ypos 300 idle "safe_distant_idle.png" action Return("safe")

screen safe_closeup_environment():
    imagebutton xpos 350 ypos 250 idle "safe_closeup_idle.png" action Return("safe_interact")
    imagebutton xpos 600 ypos 450 idle "clue_paper_idle.png" action Return("clue_paper")
    textbutton "Back" action Return("back") align (0.05, 0.95)

screen safe_puzzle_screen(current_digit, entered_code):
    # Calculates the rotation so the dial spins correctly based on the standard 0-9 layout
    $ rotation_angle = current_digit * -36

    # The rotating safe knob
    add "gui/day3_casino/backroom/safe/safe_knob.png":
        xalign 0.5 
        yalign 0.5
        transform_anchor True
        rotate rotation_angle

    # The stationary indicator arrow pointing at the current number
    add "gui/day3_casino/backroom/safe/safe_arrow.png":
        xalign 0.5 
        yalign 0.15

    # Visual cue for entered digits
    text "Code Entered: [entered_code]" xalign 0.5 yalign 0.05 size 40 color "#ffffff"

    # Keybinds for playing the minigame (Swapped A and D)
    key "a" action Return("turn_right")
    key "A" action Return("turn_right")
    key "d" action Return("turn_left")
    key "D" action Return("turn_left")
    key "K_RETURN" action Return("enter_digit")
    key "K_KP_ENTER" action Return("enter_digit")
    key "K_ESCAPE" action Return("exit")

    # Instructions UI (Swapped text)
    vbox:
        align (0.95, 0.95)
        text "'A' to turn Right" color "#ffffff"
        text "'D' to turn Left" color "#ffffff"
        text "'Enter' to lock in number" color "#ffffff"

    textbutton "Back" action Return("exit") align (0.05, 0.95)
    
screen opened_safe_environment():
    if "Bloody Ledger" not in backroom_items_found:
        imagebutton xalign 0.5 yalign 0.5 idle "bloody_ledger.jpg" action Return("bloody_ledger")
    textbutton "Leave Safe" action Return("back") align (0.05, 0.95)