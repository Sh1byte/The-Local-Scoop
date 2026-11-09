image day5_office_empty = "gui/day5/Office_empty.jpg"

image day5_pas1_1 = "gui/day5/Path A/Scene 1/PAS1_1.jpg"
image day5_pas1_2 = "gui/day5/Path A/Scene 1/PAS1_2.jpg"
image day5_pas1_3 = "gui/day5/Path A/Scene 1/PAS1_3.jpg"
image day5_pas1_4 = "gui/day5/Path A/Scene 1/PAS1_4.jpg"
image day5_pas1_5 = "gui/day5/Path A/Scene 1/PAS1_5.jpg"

image day5_pas2_1 = "gui/day5/Path A/Scene 2/PAS2_1.jpg"
image day5_pas2_2 = "gui/day5/Path A/Scene 2/PAS2_2.jpg"
image day5_pas2_3 = "gui/day5/Path A/Scene 2/PAS2_3.jpg"
image day5_pas2_4 = "gui/day5/Path A/Scene 2/PAS2_4.jpg"

image day5_ea1_1 = "gui/day5/Path A/Ending 1/EA1_1.jpg"
image day5_ea1_2 = "gui/day5/Path A/Ending 1/EA1_2.jpg"
image day5_ea1_3 = "gui/day5/Path A/Ending 1/EA1_3.jpg"
image day5_ea1_4 = "gui/day5/Path A/Ending 1/EA1_4.jpg"
image day5_ea1_5 = "gui/day5/Path A/Ending 1/EA1_5.jpg"
image day5_ea1_6 = "gui/day5/Path A/Ending 1/EA1_6.jpg"
image day5_ea1_7 = "gui/day5/Path A/Ending 1/EA1_7.jpg"
image day5_ea1_8 = "gui/day5/Path A/Ending 1/EA1_8.jpg"
image day5_ea1_9 = "gui/day5/Path A/Ending 1/EA1_9.jpg"
image day5_ea1_10 = "gui/day5/Path A/Ending 1/EA1_10.jpg"
image day5_ea1_9_nomoney = "gui/day5/Path A/Ending 1/EA1_9_NOMONEY.jpg"
image day5_ea1_10_nomoney = "gui/day5/Path A/Ending 1/EA1_10_NOMONEY.jpg"

image day5_ea2_1 = "gui/day5/Path A/Ending 2/EA2_1.jpg"
image day5_ea2_2 = "gui/day5/Path A/Ending 2/EA2_2.jpg"
image day5_ea2_3 = "gui/day5/Path A/Ending 2/EA2_3.jpg"
image day5_ea2_4 = "gui/day5/Path A/Ending 2/EA2_4.jpg"

image day5_b5_1 = "gui/day5/Path B/Scene 1/b5_1.jpg"
image day5_b5_2 = "gui/day5/Path B/Scene 1/b5_2.jpg"
image day5_b5_3 = "gui/day5/Path B/Scene 1/b5_3.jpg"
image day5_b5_4 = "gui/day5/Path B/Scene 1/b5_4.jpg"
image day5_b5_5 = "gui/day5/Path B/Scene 1/b5_5.jpg"
image day5_b5_6 = "gui/day5/Path B/Scene 1/b5_6.jpg"
image day5_b5_7 = "gui/day5/Path B/Scene 1/b5_7.jpg"

image day5_bea3_1 = "gui/day5/Path B/Ending 3/BEA3_1.jpg"
image day5_bea3_2 = "gui/day5/Path B/Ending 3/BEA3_2.jpg"
image day5_bea3_3 = "gui/day5/Path B/Ending 3/BEA3_3.jpg"
image day5_bea3_4 = "gui/day5/Path B/Ending 3/BEA3_4.jpg"
image day5_bea3_5 = "gui/day5/Path B/Ending 3/BEA3_5.jpg"
image day5_bea3_6 = "gui/day5/Path B/Ending 3/BEA3_6.jpg"
image day5_bea3_7 = "gui/day5/Path B/Ending 3/BEA3_7.jpg"

define medic = Character("Medic", color="#cccccc")
define engineer = Character("Train Engineer", color="#cccccc")
define hobo = Character("Hobo", color="#cccccc")
define tourist = Character("Tourist", color="#cccccc")
define police_chief = Character("Police Chief", color="#4a90e2")

default day5_clue = ""
default day5_item = ""
default day5_witness = ""
default evidence_phone = False
default day5_clues_found = []
default day5_items_found = []
default day5_witnesses_found = []

screen day5_docks_choice():
    modal True
    zorder 50
    on "show" action Show("global_hud")
    hbox:
        align (0.5, 0.82)
        spacing 200
        textbutton "SEND HIM DOWN":
            at day4_choice_hover
            hover_sound "audio/ui_hover.ogg"
            activate_sound "audio/ui_click.ogg"
            action Return("send_arthur")
            background None
            hover_background Solid("#FF000038")
            padding (28, 14)
            text_size 46
            text_bold True
            text_color "#FF0000"
            text_hover_color "#FF5555"
            text_outlines [(3, "#000000", 0, 0)]
            text_hover_outlines [(4, "#FFFF00", 0, 0), (2, "#000000", 0, 0)]
        textbutton "STOP HIM":
            at day4_choice_hover
            hover_sound "audio/ui_hover.ogg"
            activate_sound "audio/ui_click.ogg"
            action Return("stop_arthur")
            background None
            hover_background Solid("#FF000038")
            padding (28, 14)
            text_size 46
            text_bold True
            text_color "#FF0000"
            text_hover_color "#FF5555"
            text_outlines [(3, "#000000", 0, 0)]
            text_hover_outlines [(4, "#FFFF00", 0, 0), (2, "#000000", 0, 0)]
    if not renpy.get_screen("global_hud"):
        use global_hud

label day5_path_a_start:
    $ current_day = 4
    $ preferences.set_mixer("music", 0.70)
    show screen global_hud
    python:
        for item in ["The Diamond Earring", "The Stolen Credit Card", "The VIP Pass"]:
            if item in inventory_bag_items:
                inventory_bag_items.remove(item)
    play sting "audio/sting_day_transition.ogg" volume 0.75
    play music "audio/bgm_newsroom.ogg" fadeout 1.0 fadein 1.5 volume 0.70 if_changed
    play ambient "audio/amb_newsroom.ogg" fadeout 0.8 fadein 1.0 volume 0.45 if_changed

    scene day5_office_empty with fade
    "Boss Kenneth's office was completely empty this morning. That's odd—he's never late for work."
    play sound "audio/sfx_footsteps_move.ogg"
    play music "audio/bgm_day5_depot.ogg" fadeout 1.0 fadein 1.5 volume 0.70 if_changed
    play ambient "audio/amb_rail_depot.ogg" fadeout 0.8 fadein 1.2 volume 0.75 if_changed

    $ current_day = 5
    show screen global_hud
    scene expression "gui/day5_abandoned_station/Depot_Entrance/bg Depot_Entrance.jpg" at topleft with fade
    if took_cash:
        "Would you look at that, it's already my fifth day on the job and I've already survived a bank shootout. Because the briefcase of cash vanished in the chaos, both gangs are blaming each other."
        "I've been dispatched to investigate a morning lead at this old rail depot where one of the getaway drivers was found badly injured."
        "Arthur met me here in the morning sun, completely unaware that the missing bank cash is hidden under my floorboards."
    else:
        "Would you look at that, it's already my fifth day on the job and I barely made it out of yesterday's bank shootout alive. The robbers fled, but it looks like they were ambushed by the rival gang right after."
        "I've been dispatched to investigate a morning lead at this old rail depot where one of the getaway drivers was found badly injured."
    play sound "audio/sfx_footsteps_move.ogg"
    jump day5_investigation_hub

label day5_investigation_hub:
    $ current_day = 5
    show screen global_hud
    scene expression "gui/day5_abandoned_station/Depot_Entrance/bg Depot_Entrance.jpg" at topleft
    play music "audio/bgm_day5_depot.ogg" fadeout 1.0 fadein 1.0 volume 0.70 if_changed
    play ambient "audio/amb_rail_depot.ogg" fadeout 0.8 fadein 1.0 volume 0.75 if_changed
    call screen day5_depot_investigation
    $ clicked_object = _return

    if clicked_object == "arthur":
        show expression "gui/day5_abandoned_station/Depot_Entrance/Arthur_Day5.png" at topleft
        arthur "Morning! Word is a getaway driver from yesterday's bank chaos was dumped here in bad shape."
        arthur "Then the rival gang showed up to finish the job while they were weak, forcing the survivors to scatter. Keep your eyes peeled for anything they dropped."
    elif clicked_object == "tourist":
        if "Tourist 1" not in day5_witnesses_found:
            play sound "audio/ui_notepad_flip.ogg"
            $ day5_witnesses_found.append("Tourist 1")
        show expression "gui/day5_abandoned_station/Depot_Entrance/Tourist.png" at topleft
        play sound "audio/sfx_camera_shutter.ogg"
        tourist "I didn't know this town would be this active!"
        tourist "I've been snapping photos all morning! I'm pretty sure they were just filming a zombie action movie here with fake blood."
    elif clicked_object == "go_to_maintenance_bay":
        play sound "audio/sfx_door_open.ogg"
        jump day5_maintenance_bay_hub
    elif clicked_object == "go_to_abandoned_tracks":
        play sound "audio/sfx_footsteps_move.ogg"
        jump day5_abandoned_tracks_hub
    elif clicked_object == "go_to_triage":
        play sound "audio/sfx_footsteps_move.ogg"
        jump day5_triage_hub
    elif clicked_object == "newsroom":
        play sound "audio/sfx_van_door.ogg"
        jump day5_morning_newspaper

    jump day5_investigation_hub

label day5_maintenance_bay_hub:
    if "The Rusty Toolbox" not in inventory_bag_items:
        scene expression "gui/day5_abandoned_station/Maintenance_Bay/bg Maintenance_Bay_Toolbox.jpg" at topleft
    else:
        scene expression "gui/day5_abandoned_station/Maintenance_Bay/bg Maintenance_Bay_NoToolbox.jpg" at topleft
    play music "audio/bgm_day5_depot.ogg" fadeout 1.0 fadein 1.0 volume 0.70 if_changed
    play ambient "audio/amb_maintenance_bay.ogg" fadeout 0.8 fadein 0.8 volume 0.75 if_changed
    call screen day5_maintenance_bay_environment
    $ clicked_object = _return

    if clicked_object == "engineer":
        if "Train Engineer 1" not in day5_witnesses_found:
            play sound "audio/ui_notepad_flip.ogg"
            $ day5_witnesses_found.append("Train Engineer 1")
        show expression "gui/day5_abandoned_station/Maintenance_Bay/Train_Engineer.png" at topleft
        engineer "Nothing mysterious about it. That driver just fell off a moving cargo train."
        engineer "I was working on the tracks when I saw him tumble right off."
    elif clicked_object == "toolbox":
        play sound "audio/sfx_trash_metal.ogg"
        "Heavy junk left behind by a mechanic."
        if "The Rusty Toolbox" not in day5_items_found:
            $ day5_items_found.append("The Rusty Toolbox")
        if "The Rusty Toolbox" not in inventory_bag_items:
            $ inventory_bag_items.append("The Rusty Toolbox")
    elif clicked_object == "go_to_oilleak_closeup":
        play sound "audio/sfx_footsteps_move.ogg"
        jump day5_oilleak_closeup_hub
    elif clicked_object == "depot_entrance":
        play sound "audio/sfx_door_open.ogg"
        jump day5_investigation_hub

    jump day5_maintenance_bay_hub

label day5_oilleak_closeup_hub:
    scene expression "gui/day5_abandoned_station/Maintenance_Bay/Oil_Leak_CloseUp.jpg" at topleft
    if "The Leaking Oil Puddle" not in day5_clues_found:
        play sound "audio/ui_notepad_flip.ogg"
        $ day5_clues_found.append("The Leaking Oil Puddle")
    "Looks like normal car trouble."
    "Wait, what is that red drop beside the puddle?"
    call screen day5_oilleak_closeup_environment
    play sound "audio/ui_cancel.ogg"
    jump day5_maintenance_bay_hub

label day5_abandoned_tracks_hub:
    if "The Empty Wallet" not in inventory_bag_items:
        scene expression "gui/day5_abandoned_station/Abandoned_Tracks/bg Abandoned_Tracks_Wallet.jpg" at topleft
    else:
        scene expression "gui/day5_abandoned_station/Abandoned_Tracks/bg Abandoned_Tracks_NoWallet.jpg" at topleft
    play music "audio/bgm_day5_depot.ogg" fadeout 1.0 fadein 1.0 volume 0.70 if_changed
    play ambient "audio/amb_rail_depot.ogg" fadeout 0.8 fadein 0.8 volume 0.80 if_changed
    call screen day5_abandoned_tracks_environment
    $ clicked_object = _return

    if clicked_object == "hobo":
        if "Hobo 1" not in day5_witnesses_found:
            play sound "audio/ui_notepad_flip.ogg"
            $ day5_witnesses_found.append("Hobo 1")
        show expression "gui/day5_abandoned_station/Abandoned_Tracks/Homeless_Man_Idle.png" at topleft
        hobo "Wake up! The government is poisoning the water supply!"
        hobo "I drank from a rusty faucet and my stomach hurt ALL WEEK!"
    elif clicked_object == "go_to_tracks_closeup":
        play sound "audio/sfx_footsteps_move.ogg"
        jump day5_tracks_closeup_hub
    elif clicked_object == "go_to_grass_closeup":
        play sound "audio/sfx_footsteps_move.ogg"
        jump day5_grass_closeup_hub
    elif clicked_object == "depot_entrance":
        play sound "audio/sfx_footsteps_move.ogg"
        jump day5_investigation_hub

    jump day5_abandoned_tracks_hub

label day5_tracks_closeup_hub:
    scene expression "gui/day5_abandoned_station/Abandoned_Tracks/Tracks_CloseUp.jpg" at topleft
    call screen day5_tracks_closeup_environment
    $ clicked_object = _return
    if clicked_object == "tiretracks":
        play sound "audio/sfx_camera_shutter.ogg"
        if "The Bloody Tire Tracks" not in day5_clues_found:
            play sting "audio/sting_clue_major.ogg" volume 0.75
            $ day5_clues_found.append("The Bloody Tire Tracks")
        "Bloody tire tracks. They show the exact escape route of the ambushed gangsters."
        jump day5_tracks_closeup_hub
    elif clicked_object == "dogtracks":
        if "The Wild Dog Tracks" not in day5_clues_found:
            play sound "audio/ui_notepad_flip.ogg"
            $ day5_clues_found.append("The Wild Dog Tracks")
        "Wild dog tracks. Maybe they were drawn to the smell of blood."
        "Or they just went for a hunt and stumbled through here accidentally."
        jump day5_tracks_closeup_hub
    play sound "audio/ui_cancel.ogg"
    jump day5_abandoned_tracks_hub

label day5_grass_closeup_hub:
    scene expression "gui/day5_abandoned_station/Abandoned_Tracks/Grass_CloseUp_NoWallet.jpg" at topleft
    call screen day5_grass_closeup_environment
    $ clicked_object = _return
    if clicked_object == "wallet":
        play sound "audio/sfx_pickup_item.ogg"
        "An empty leather wallet. Could this belong to a local pickpocket?"
        if "The Empty Wallet" not in day5_items_found:
            $ day5_items_found.append("The Empty Wallet")
        if "The Empty Wallet" not in inventory_bag_items:
            $ inventory_bag_items.append("The Empty Wallet")
        jump day5_grass_closeup_hub
    play sound "audio/ui_cancel.ogg"
    jump day5_abandoned_tracks_hub

label day5_triage_hub:
    if "The Burner Phone" not in inventory_bag_items and not evidence_phone:
        scene expression "gui/day5_abandoned_station/Triage/bg Makeshift_Triage_Phone.jpg" at topleft
    else:
        scene expression "gui/day5_abandoned_station/Triage/bg Makeshift_Triage_NoPhone.jpg" at topleft
    play music "audio/bgm_day5_depot.ogg" fadeout 1.0 fadein 1.0 volume 0.70 if_changed
    play ambient "audio/amb_rail_depot.ogg" fadeout 0.8 fadein 0.8 volume 0.75 if_changed
    call screen day5_triage_environment
    $ clicked_object = _return

    if clicked_object == "medic":
        if "Medic 1" not in day5_witnesses_found:
            play sound "audio/ui_notepad_flip.ogg"
            $ day5_witnesses_found.append("Medic 1")
        show expression "gui/day5_abandoned_station/Triage/Medic.png" at topleft
        medic "They forced me at gunpoint to treat a wounded gangster! He kept muttering about how they're gonna get revenge at the shipping docks tonight!"
    elif clicked_object == "go_to_crate_closeup":
        play sound "audio/sfx_footsteps_move.ogg"
        jump day5_crate_closeup_hub
    elif clicked_object == "go_to_tent":
        play sound "audio/sfx_zipper_tent.ogg"
        jump day5_triage_tent_hub
    elif clicked_object == "depot_entrance":
        play sound "audio/sfx_footsteps_move.ogg"
        jump day5_investigation_hub

    jump day5_triage_hub

label day5_crate_closeup_hub:
    scene expression "gui/day5_abandoned_station/Triage/Crate_CloseUp_NoPhone.jpg" at topleft
    call screen day5_crate_closeup_environment
    $ clicked_object = _return
    if clicked_object == "phone":
        play sound "audio/sfx_phone_pickup.ogg"
        play sting "audio/sting_clue_major.ogg" volume 0.80
        "A cheap burner phone dropped near the medical supplies. The text messages confirm there will be an all-out gang war at the shipping docks at midnight!"
        $ evidence_phone = True
        if "The Burner Phone" not in inventory_bag_items:
            $ inventory_bag_items.append("The Burner Phone")
        jump day5_crate_closeup_hub
    play sound "audio/ui_cancel.ogg"
    jump day5_triage_hub

label day5_triage_tent_hub:
    if "The Train Ticket Stub" not in inventory_bag_items:
        scene expression "gui/day5_abandoned_station/Triage/Tent/bg Inside_Tent_Ticket.jpg" at topleft
    else:
        scene expression "gui/day5_abandoned_station/Triage/Tent/bg Inside_Tent_NoTicket.jpg" at topleft
    play music "audio/bgm_day5_depot.ogg" fadeout 1.0 fadein 1.0 volume 0.70 if_changed
    play ambient "audio/amb_triage_tent.ogg" fadeout 0.8 fadein 0.8 volume 0.75 if_changed
    call screen day5_triage_tent_environment
    $ clicked_object = _return
    if clicked_object == "go_to_coat_closeup":
        play sound "audio/sfx_paper_rustle.ogg"
        jump day5_coat_closeup_hub
    elif clicked_object == "back_to_triage":
        play sound "audio/sfx_zipper_tent.ogg"
        jump day5_triage_hub
    jump day5_triage_tent_hub

label day5_coat_closeup_hub:
    scene expression "gui/day5_abandoned_station/Triage/Tent/Coat_CloseUp_NoTicket.jpg" at topleft
    call screen day5_coat_closeup_environment
    $ clicked_object = _return
    if clicked_object == "ticketstub":
        play sound "audio/sfx_paper_rustle.ogg"
        play sting "audio/sting_clue_major.ogg" volume 0.75
        "There's a Train Ticket Stub in the injured driver's pocket. Looks like they were planning to flee town until they got ambushed by the rival gang."
        if "The Train Ticket Stub" not in day5_items_found:
            $ day5_items_found.append("The Train Ticket Stub")
        if "The Train Ticket Stub" not in inventory_bag_items:
            $ inventory_bag_items.append("The Train Ticket Stub")
        jump day5_coat_closeup_hub
    play sound "audio/ui_cancel.ogg"
    jump day5_triage_tent_hub

label day5_morning_newspaper:
    if not evidence_phone:
        play sound "audio/ui_evidence_locked.ogg"
        "(Wait... I feel like I missed something crucial near the medical crates at the Triage area. I should check there before writing my story.)"
        jump day5_investigation_hub
    $ hide_all_investigation_screens()
    $ current_day = 4
    show screen global_hud
    play sound "audio/sfx_typewriter_write.ogg"
    play music "audio/bgm_newsroom.ogg" fadeout 1.0 fadein 1.2 volume 0.70 if_changed
    play ambient "audio/amb_newsroom.ogg" fadeout 1.0 fadein 1.0 volume 0.70 if_changed
    scene news_creation with dissolve
    "Time to review my Reporter's Notepad and write the rail depot edition."

label select_day5_clue:
    play sound "audio/ui_notepad_flip.ogg"
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
    play sound "audio/ui_notepad_flip.ogg"
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
    play sound "audio/ui_notepad_flip.ogg"
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
    call calculate_day5_credibility from _call_calculate_day5_credibility
    python:
        article_result = sheetdb_client.fetch_newspaper_article(day5_clue, day5_item, day5_witness, "day5")
        daily_headline = article_result.get("headline", "Error: Story Not Found")
        daily_body = article_result.get("body", "Error: Check database connection.")

    scene desk_newspaper
    play sound "audio/sfx_newspaper_print.ogg"
    "Let's see how the evening edition turned out..."
    if day5_score >= 2:
        play sting "audio/sting_rating_high.ogg" volume 0.80
    else:
        play sting "audio/sting_rating_low.ogg" volume 0.80
    call screen newspaper_results_ui(daily_headline, daily_body, daily_rating, total_credibility_score)
    play sound "audio/sfx_paper_rustle.ogg"
    $ renpy.force_autosave(True)
    jump day5_path_a_climax

label day5_path_a_climax:
    $ current_day = 4
    $ preferences.set_mixer("music", 0.70)
    $ hide_all_investigation_screens()
    show screen global_hud
    $ set_cutscene_lock(True, 22)

    play sting "audio/sting_day_transition.ogg" volume 0.75
    play music "audio/bgm_day5_docks_tension.ogg" fadeout 1.0 fadein 1.5 volume 0.70 if_changed
    play ambient "audio/amb_newsroom.ogg" fadeout 0.8 fadein 1.2 volume 0.70 if_changed
    scene black with fade

    play sound "audio/sfx_footsteps_move.ogg"
    scene day5_pas1_1 with dissolve
    "{cps=22}(Night had fallen over the Herald News Station. Most of the desks were dark and empty, save for the dim glow of a lamp where Arthur sat reviewing his notes.){/cps}{w=2.8}{nw}"

    play sound "audio/sfx_footsteps_move.ogg"
    scene day5_pas1_2 with dissolve
    "{cps=22}Arthur, you still have your spare camera gear, right? Drop whatever you're working on—you need to see this.{/cps}{w=2.8}{nw}"
    arthur "{cps=22}Huh? What's got you worked up at this hour, rookie? I thought we were done for the night.{/cps}{w=2.5}{nw}"

    play sound "audio/sfx_phone_vibrate.ogg"
    play sting "audio/sting_clue_major.ogg" volume 0.75
    scene day5_pas1_3 with dissolve
    "{cps=22}(I pulled out the burner phone I recovered from the rail depot triage and held the glowing screen up in front of him.){/cps}{w=2.8}{nw}"
    "{cps=22}Read the texts. The River Boys and the Iron Syndicate are meeting at the shipping docks at midnight to settle everything. It's going to be an all-out war.{/cps}{w=3.2}{nw}"

    scene day5_pas1_4 with dissolve
    arthur "{cps=22}Midnight at the docks... If we capture this, it won't just be front-page news—it'll be the biggest story this town has ever seen.{/cps}{w=3.0}{nw}"
    "{cps=22}(Arthur stood up from his chair and locked eyes with me, all trace of our old rivalry replaced by pure determination.){/cps}{w=2.8}{nw}"
    arthur "{cps=22}Let's move. We're covering this together.{/cps}{w=2.2}{nw}"

    play sound "audio/sfx_door_open.ogg"
    scene day5_pas1_5 with dissolve
    "{cps=22}(Grabbing our cameras, the two of us hurried out of the newsroom into the cold night, heading straight for the shipping docks.){/cps}{w=2.8}{nw}"

    stop ambient fadeout 1.0
    scene black with fade

    play music "audio/bgm_day5_docks_tension.ogg" fadein 1.2 volume 0.70 if_changed
    play ambient "audio/amb_docks_night.ogg" fadein 1.5 volume 0.80

    play sound "audio/sfx_footsteps_move.ogg"
    scene day5_pas2_1 with fade
    "{cps=22}(In the cover of the night, Arthur and I crept up a grassy hill overlooking the shipping yard, crouching low in the shadows as the two gangs assembled below.){/cps}{w=3.0}{nw}"

    play sound "audio/sfx_gun_cock.ogg"
    scene day5_pas2_2 with dissolve
    "{cps=22}(Down between the towering cargo containers, dozens of armed men from both syndicates stood face-to-face with guns drawn. A single spark was going to set the whole yard ablaze.){/cps}{w=3.2}{nw}"

    scene day5_pas2_3 with dissolve
    arthur "{cps=22}Damn it, it's too dark from up here... My lens can't make out their faces from this distance.{/cps}{w=2.8}{nw}"
    arthur "{cps=22}Listen, I'm going to sneak down behind those cargo crates at the edge of the pier. It's risky, I know—but one clear shot of their leaders will nail them for good.{/cps}{w=3.2}{nw}"

    play ambient "audio/sfx_heartbeat_timer.ogg" fadein 0.4 volume 0.80
    scene day5_pas2_4 with dissolve
    "{cps=22}(My chest tightened as I looked down at the armed gunmen below, then back at Arthur waiting for my signal. If he goes down there, he'll be right in the line of fire... there is a high chance that he will die){/cps}{w=3.0}{nw}"

    hide screen prologue_cutscene_lock
    call screen day5_docks_choice
    $ docks_decision = _return
    stop ambient fadeout 0.4
    show screen prologue_cutscene_lock

    if docks_decision == "send_arthur":
        play music "audio/bgm_day4_betrayal.ogg" fadeout 0.8 fadein 1.2 volume 0.70
        play ambient "audio/amb_docks_night.ogg" fadein 0.8 volume 0.75

        scene day5_ea1_1 with dissolve
        "{cps=22}You're right, Arthur. We only get one shot at a career-defining scoop like this. Get down there and get the close-up—I'll cover the wide angle from here.{/cps}{w=3.2}{nw}"
        arthur "{cps=22}Wish me luck, partner. Keep your head down.{/cps}{w=2.4}{nw}"

        play sound "audio/sfx_footsteps_move.ogg"
        scene day5_ea1_2 with dissolve
        "{cps=22}(I stayed crouched on the ridge, watching silently as Arthur slipped down the dark slope toward the shipping containers.){/cps}{w=2.8}{nw}"

        play sound "audio/sfx_camera_shutter.ogg"
        scene day5_ea1_3 with dissolve
        "{cps=22}(Reaching the bottom of the yard, Arthur pressed his back against a steel cargo crate and raised his camera, snapping photos of the standoff just yards away.){/cps}{w=3.0}{nw}"

        play music "audio/bgm_day4_heist_action.ogg" fadeout 0.4 fadein 0.3 volume 0.70
        play ambient "audio/sfx_gunfight_loop.ogg" fadein 0.2 volume 0.75
        scene day5_ea1_4 with vpunch
        "{cps=22}(Suddenly, all hell broke loose! Deafening gunfire erupted across the docks as muzzle flashes lit up the night, forcing Arthur to curl tighter behind the crate.){/cps}{w=3.0}{nw}"

        stop music
        stop ambient
        play sound "audio/sfx_gunshot_execution.ogg"
        play sting "audio/sting_tragedy_shot.ogg" volume 0.85
        scene day5_ea1_5 with vpunch
        "{cps=22}(BANG! A stray heavy-caliber round punched straight through the corner of the container, striking Arthur directly in the neck.){/cps}{w=3.0}{nw}"

        play music "audio/bgm_ending_dark.ogg" fadein 1.5 volume 0.70
        play ambient "audio/amb_docks_night.ogg" fadein 1.5 volume 0.75
        scene day5_ea1_6 with dissolve
        "{cps=22}(His camera tumbled from his grasp and shattered against the concrete. Beneath the flickering dock lights, Arthur lay motionless on the cold pavement—alone, and dead.){/cps}{w=3.2}{nw}"

        play sound "audio/sfx_police_sirens.ogg"
        scene day5_ea1_7 with dissolve
        "{cps=22}(Minutes later, wailing police sirens flooded the waterfront, scattering the surviving gang members into the night while I stood untouched atop the hill.){/cps}{w=3.0}{nw}"

        play sting "audio/sting_greed_grin.ogg" volume 0.85
        scene day5_ea1_8 with dissolve
        "{cps=22}(Arthur was gone. Kenneth was gone. There were no rivals left in my way—the biggest story in town belonged to me, and me alone.){/cps}{w=3.5}{nw}"
        stop ambient fadeout 1.2
        scene black with fade

        if took_cash:
            play sound "audio/sfx_cash_briefcase.ogg"
            play sound "audio/sfx_whiskey_sip.ogg"
            scene day5_ea1_9 with fade
            "{cps=22}(My exclusive front-page headline—'TRAGEDY AT THE DOCKS: SYNDICATE WAR CLAIMS LOCAL REPORTER'—catapulted me to the very top of The Daily Herald.){/cps}{w=3.2}{nw}"
            "{cps=22}(With the stolen bank fortune resting beside my glass of whiskey, I had wealth, fame, and complete control over the town's emotions){/cps}{w=3.2}{nw}"
            scene day5_ea1_10 with dissolve
            "{cps=22}In the end, the truth is whatever the last man standing writes down.{/cps}{w=2.8}{nw}"
            "{cps=22}ENDING UNLOCKED: The Darker Path.{/cps}{w=3.0}{nw}"
            $ current_ending_name = "The Darker Path"
        else:
            play sound "audio/sfx_whiskey_sip.ogg"
            scene day5_ea1_9_nomoney with fade
            "{cps=22}(My exclusive front-page headline—'TRAGEDY AT THE DOCKS: SYNDICATE WAR CLAIMS LOCAL REPORTER'—catapulted me to the very top of The Daily Herald.){/cps}{w=3.2}{nw}"
            "{cps=22}(Sitting in my new executive office, with the newspaper that made me famous at the cost of my rival, Arthur's life.){/cps}{w=3.2}{nw}"
            scene day5_ea1_10_nomoney with dissolve
            "{cps=22}In the end, the truth is whatever the last man standing writes down.{/cps}{w=2.8}{nw}"
            "{cps=22}ENDING UNLOCKED: The Dark Path.{/cps}{w=3.0}{nw}"
            $ current_ending_name = "The Dark Path"

        call play_end_credits("The Redemption Path") from _call_play_end_credits
        return

    else:
        play music "audio/bgm_day4_heist_action.ogg" fadeout 0.8 fadein 1.0 volume 0.70
        play ambient "audio/amb_docks_night.ogg" fadein 0.8 volume 0.75

        play sound "audio/sfx_pickup_item.ogg"
        scene day5_ea2_1 with dissolve
        "{cps=22}No! Hold on, Arthur—don't go down there! Look at how many guns they have. No photograph is worth throwing your life away!{/cps}{w=3.0}{nw}"
        arthur "{cps=22}Tch... You're right. If they spot either of us down there, we're dead men.{/cps}{w=2.6}{nw}"

        play ambient "audio/sfx_gunfight_loop.ogg" fadein 0.3 volume 0.70
        play sound "audio/sfx_camera_shutter.ogg"
        scene day5_ea2_2 with vpunch
        "{cps=22}(Seconds later, the docks erupted into a violent crossfire! Lying flat on the hilltop together, Arthur and I snapped shot after shot as bullets tore through the very crates he had planned to hide behind.){/cps}{w=3.5}{nw}"

        stop ambient fadeout 1.0
        play music "audio/bgm_ending_redemption.ogg" fadeout 1.2 fadein 1.5 volume 0.70
        play ambient "audio/amb_docks_night.ogg" fadein 1.0 volume 0.75
        scene day5_ea2_3 with dissolve
        arthur "{cps=22}Did you see that cargo container get shredded...? If you hadn't grabbed my arm when you did, I wouldn't have walked away from this.{/cps}{w=3.0}{nw}"
        arthur "{cps=22}Thanks for having my back, partner. Seriously... I owe you my life.{/cps}{w=2.6}{nw}"
        "{cps=22}Come on, partner. I think the action is done, lets go back to the station and put an end to this local scoop together.{/cps}{w=2.8}{nw}"

        stop ambient fadeout 1.0
        scene black with fade

        play sting "audio/sting_victory_press.ogg" volume 0.80
        play ambient "audio/amb_press_flashes.ogg" fadein 0.8 volume 0.80
        play sound "audio/sfx_camera_shutter.ogg"
        scene day5_ea2_4 with fade
        "{cps=22}(The next morning, The Daily Herald held a special press briefing packed with reporters from across the country, blinding camera flashes illuminating the stage.){/cps}{w=3.2}{nw}"
        "{cps=22}(Standing shoulder-to-shoulder, Arthur and I held up our co-authored front page—'THE MIDNIGHT BUST: RIVER BOYS AND IRON SYNDICATE EXPOSED'—no longer rivals, but true friends who broke the biggest scoop in town.){/cps}{w=3.5}{nw}"
        "{cps=22}ENDING UNLOCKED: The Redemption Path.{/cps}{w=3.0}{nw}"

        stop music fadeout 2.0
        stop ambient fadeout 2.0
        scene black with fade
        $ set_cutscene_lock(False)
        return

label day5_path_b_start:
    $ current_day = 4
    $ preferences.set_mixer("music", 0.70)
    $ hide_all_investigation_screens()
    show screen global_hud
    $ set_cutscene_lock(True, 22)

    play sting "audio/sting_day_transition.ogg" volume 0.75
    play music "audio/bgm_day5_docks_tension.ogg" fadeout 1.0 fadein 1.5 volume 0.70 if_changed
    play ambient "audio/amb_night_street.ogg" fadeout 0.8 fadein 1.2 volume 0.75 if_changed

    scene day5_b5_1 with fade
    "{cps=22}(Night had settled quietly over the town police station, its warm windows cutting through the dark after the chaos of the afternoon bank heist.){/cps}{w=3.0}{nw}"

    play ambient "audio/amb_police_station.ogg" fadeout 0.8 fadein 1.0 volume 0.75
    scene day5_b5_2 with dissolve
    "{cps=22}(Bruised, scratched, and completely drained, I sat slumped in front of the precinct desk until a familiar, steady hand rested on my shoulder.){/cps}{w=3.0}{nw}"
    arthur "{cps=22}Easy there, kid. Take a breath. You're in one piece.{/cps}{w=2.5}{nw}"

    scene day5_b5_3 with dissolve
    "{cps=22}(I looked up at Arthur in disbelief, the memory of those final, terrifying seconds in the alleyway rushing back all at once.){/cps}{w=2.8}{nw}"
    "{cps=22}Arthur... back in that alley, when Kenneth pulled the trigger... how am I still alive?{/cps}{w=2.8}{nw}"

    play music "audio/bgm_day4_betrayal.ogg" fadeout 0.6 fadein 0.8 volume 0.70
    stop ambient fadeout 0.5
    play sound "audio/sfx_gun_cock.ogg"
    scene day5_b5_4 with fade
    "{cps=22}I remembered staring straight down the barrel of Editor Kenneth's gun, frozen in terror as his finger tightened on the trigger.{/cps}{w=2.8}{nw}"

    play sound "audio/sfx_gunshot_execution.ogg"
    play sound "audio/sfx_body_tackle.ogg"
    scene day5_b5_5 with vpunch
    "{cps=22}Just as the gunshot rang out, Arthur had lunged out of nowhere and slammed his full weight into Kenneth, knocking his aim wide as both of them crashed onto the concrete!{/cps}{w=3.2}{nw}"

    scene day5_b5_6 with dissolve
    "{cps=22}Paralyzed by shock and half-convinced I had already been shot dead, I could only watch in a daze as Arthur wrestled with Kenneth on the ground to keep the gun pinned.{/cps}{w=3.2}{nw}"

    play sound "audio/sfx_police_sirens.ogg"
    play sound "audio/sfx_run_panting.ogg"
    scene day5_b5_7 with dissolve
    "{cps=22}When police sirens closed in on the mouth of the alley, Kenneth wrenched himself free and bolted into the shadows, leaving the two of us behind.{/cps}{w=3.0}{nw}"

    play music "audio/bgm_day5_docks_tension.ogg" fadeout 0.8 fadein 1.2 volume 0.70
    play ambient "audio/amb_police_station.ogg" fadein 1.0 volume 0.75

    play sound "audio/sfx_desk_slam.ogg"
    play sting "audio/sting_clue_major.ogg" volume 0.85
    scene day5_bea3_1 with fade
    "{cps=22}Refusing to let Kenneth get away, Arthur and I marched straight into the Police Chief's office and laid every piece of hard evidence across his desk—the Brass Lighter, the Extortion Letter, and the Bloody Ledger.{/cps}{w=3.5}{nw}"
    police_chief "{cps=22}Good God... The Daily Herald's Kenneth is the mastermind behind the Iron Syndicate?! And both gangs are converging on the shipping docks tonight?!{/cps}{w=3.2}{nw}"

    play sound "audio/sfx_pickup_item.ogg"
    scene day5_bea3_2 with dissolve
    police_chief "{cps=22}Dispatch, mobilize every unit in the city immediately! Lock down the waterfront and surround the shipping docks—nobody gets in or out!{/cps}{w=3.2}{nw}"

    stop ambient fadeout 0.8
    scene black with fade

    play music "audio/bgm_day4_heist_action.ogg" fadein 0.8 volume 0.70
    play ambient "audio/amb_docks_night.ogg" fadein 1.0 volume 0.75
    play sound "audio/sfx_police_sirens.ogg"
    scene day5_bea3_3 with fade
    "{cps=22}(Before a single shot could be fired at the docks, a massive wall of police cruisers and tactical units surrounded the entire pier, outnumbering both gangs two-to-one.){/cps}{w=3.2}{nw}"
    play sound "audio/sfx_police_megaphone.ogg"
    police_chief "{cps=22}THIS IS THE POLICE! THE DOCKS ARE COMPLETELY SURROUNDED! DROP YOUR WEAPONS AND SURRENDER IMMEDIATELY!{/cps}{w=3.0}{nw}"

    play sound "audio/sfx_gun_cock.ogg"
    scene day5_bea3_4 with dissolve
    "{cps=22}(Trapped inside a steel cargo container with floodlights blinding them from every angle, Kenneth and his syndicate enforcers realized they had nowhere left to run.){/cps}{w=3.2}{nw}"

    play music "audio/bgm_ending_redemption.ogg" fadeout 1.0 fadein 1.5 volume 0.70
    play sound "audio/sfx_handcuffs_click.ogg"
    scene day5_bea3_5 with dissolve
    "{cps=22}(Defeated at last, Kenneth and his men threw down their weapons and stepped out with their hands raised, marching away in steel handcuffs as officers led them into custody.){/cps}{w=3.2}{nw}"

    stop ambient fadeout 1.0
    scene black with fade

    play sting "audio/sting_victory_press.ogg" volume 0.85
    play ambient "audio/amb_press_flashes.ogg" fadein 0.8 volume 0.80
    play sound "audio/sfx_camera_shutter.ogg"
    scene day5_bea3_6 with fade
    "{cps=22}(The next day, cameras flashed endlessly as Arthur and I stood side-by-side before a packed press conference, recounting how we connected every clue across town to stop the gang war before it began.){/cps}{w=3.5}{nw}"

    play sound "audio/sfx_camera_shutter.ogg"
    scene day5_bea3_7 with dissolve
    "{cps=22}Together, we hadn't just written the biggest headline in the history of The Daily Herald, we had saved the town and proven what true journalism was all about.{/cps}{w=3.5}{nw}"
    "{cps=22}ENDING UNLOCKED: The Clean Sweep.{/cps}{w=3.0}{nw}"

    call play_end_credits("The Clean Sweep") from _call_play_end_credits_1
    return