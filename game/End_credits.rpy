default persistent.unlocked_endings = []
default current_ending_name = ""

init python:
    def format_pick_name(name):
        mapping = {
            "Missing blueprint": "the Missing Blueprint",
            "The Melted Camera": "the Blurry Photograph",
            "Watchman 1": "the Watchman",
            "Fisherman 1": "the Fisherman",
            "Delivery Driver 1": "the Delivery Driver",
            "Jogger 1": "the Jogger",
            "Vendor 1": "the Vendor",
            "Shopper 1": "the Shopper",
            "Baker 1": "the Baker",
            "Street Musician 1": "the Street Musician",
            "Dealer 1": "the Dealer",
            "Cleaner 1": "the Cleaner",
            "Waitress 1": "the Waitress",
            "Drunk Patron 1": "the Drunk Patron",
            "Medic 1": "the Medic",
            "Train Engineer 1": "the Train Engineer",
            "Hobo 1": "the Hobo",
            "Tourist 1": "the Tourist"
        }
        return mapping.get(name, name if name else "nothing")

    def build_day_recap(day_num, clue, item, witness, target_clue, target_item, target_witness):
        if not clue and not item and not witness:
            if day_num == 5:
                return "On Day 5, you bypassed the morning edition and handed your hard evidence straight to the Police Chief to stop the dock war."
            return f"On Day {day_num}, no newspaper report was filed."

        mistakes = []
        if clue != target_clue:
            mistakes.append(f"{format_pick_name(clue)} instead of {format_pick_name(target_clue)}")
        if item != target_item:
            mistakes.append(f"{format_pick_name(item)} instead of {format_pick_name(target_item)}")
        if witness != target_witness:
            mistakes.append(f"{format_pick_name(witness)} instead of {format_pick_name(target_witness)}")

        if len(mistakes) == 0:
            return (
                f"On Day {day_num}, you got the True Journalism rating! You published the complete truth using "
                f"{format_pick_name(target_clue)}, {format_pick_name(target_item)}, and {format_pick_name(target_witness)}."
            )
        elif len(mistakes) == 1:
            return (
                f"On Day {day_num}, you got the Sensationalist rating—an almost perfect news report, "
                f"but you chose {mistakes[0]}."
            )
        elif len(mistakes) == 2:
            return (
                f"On Day {day_num}, you got the Fake News rating because you chose "
                f"{mistakes[0]}, and {mistakes[1]}."
            )
        else:
            return (
                f"On Day {day_num}, you got the Fake News rating, missing all three leads by choosing "
                f"{mistakes[0]}, {mistakes[1]}, and {mistakes[2]}."
            )

    def get_all_day_recaps():
        return [
            build_day_recap(1, store.day1_clue, store.day1_item, store.day1_witness, "The Smashed Paint Can", "Missing blueprint", "Watchman 1"),
            build_day_recap(2, store.day2_clue, store.day2_item, store.day2_witness, "The Scorched Gas Can", "The Melted Camera", "Vendor 1"),
            build_day_recap(3, store.day3_clue, store.day3_item, store.day3_witness, "The Bullet-Riddled Wall", "The VIP Pass", "Dealer 1"),
            build_day_recap(5, store.day5_clue, store.day5_item, store.day5_witness, "The Bloody Tire Tracks", "The Train Ticket Stub", "Medic 1")
        ]

    def get_score_verdict(score):
        if score >= 30:
            return f"Your total journalism score is {score}, you really are hungry for the truth!"
        elif score >= 15:
            return f"Your total journalism score is {score}, you have a sharp eye for a story even if a few leads slipped by!"
        elif score >= 0:
            return f"Your total journalism score is {score}, your headlines turned heads even when the facts took a backseat!"
        else:
            return f"Your total journalism score is {score}, the town loved the drama even if the truth stayed buried!"

    credits_list = [
        ("Project Lead", "Reden Gaspar"),
        ("Lead UI/UX Designer", "Nick Aeron James Castañeto Miranda"),
        ("Assistant UI/UX Designer", "Reden Gaspar"),
        ("System Analyst", "Cedric Chin"),
        ("Sound Designer", "Reden Gaspar"),
        ("API Specialist", "Josh Esteban"),
        ("Narrative Writer", "Reden Gaspar"),
        ("Game Tester", "Kenneth Angeles"),
        ("Music Composer", "Gemini Argon"),
        ("Game Engine", "Ren'Py")
    ]

transform end_credits_scroll:
    xpos 0.5
    xanchor 0.5
    ypos 1080
    yanchor 0.0
    linear 36.0 ypos 1080 yanchor 1.0

screen end_credits_screen(ending_name):
    modal True
    zorder 400
    add Solid("#0a0a0a")

    $ recaps = get_all_day_recaps()
    $ score_line = get_score_verdict(total_credibility_score)
    $ unlocked_count = len(persistent.unlocked_endings)

    vbox:
        at end_credits_scroll
        xsize 1500
        spacing 75

        vbox:
            xalign 0.5
            spacing 16
            text "THE LOCAL SCOOP" xalign 0.5 size 64 bold True color "#f0c75e" outlines [(3, "#000000", 0, 0)]
            text "Official Credits" xalign 0.5 size 28 italic True color "#bbbbbb"

        for role_title, person_name in credits_list:
            vbox:
                xalign 0.5
                spacing 10
                text "[role_title]" xalign 0.5 size 26 bold True color "#f0c75e"
                text "[person_name]" xalign 0.5 size 34 color "#ffffff"

        null height 30
        text "ALL IMAGES IN THIS GAME ARE AI GENERATED" xalign 0.5 size 28 bold True color "#d9534f" outlines [(2, "#000000", 0, 0)]
        null height 280

        fixed:
            xsize 1500
            ysize 1080
            vbox:
                align (0.5, 0.5)
                xsize 1380
                spacing 24

                text "INVESTIGATION PERFORMANCE" xalign 0.5 size 42 bold True color "#f0c75e" outlines [(2, "#000000", 0, 0)]
                null height 6

                for recap_line in recaps:
                    frame:
                        xfill True
                        background Solid("#181818E6")
                        padding (26, 16)
                        text "[recap_line]" xalign 0.5 text_align 0.5 size 23 color "#eeeeee" line_spacing 4

                null height 10
                text "[score_line]" xalign 0.5 text_align 0.5 size 30 bold True color "#f0c75e"
                text "You chose the \"[ending_name]\" ending ([unlocked_count] out of 4 endings unlocked!)" xalign 0.5 text_align 0.5 size 26 color "#ffffff"

                null height 16
                text "Thank you for playing our game, now go out and seek the truth of your life!" xalign 0.5 text_align 0.5 size 30 italic True color "#fff4d6"

                null height 24
                textbutton "Return to Main Menu":
                    xalign 0.5
                    hover_sound "audio/ui_hover.ogg"
                    activate_sound "audio/ui_click.ogg"
                    action Return()
                    background Solid("#c99838")
                    hover_background Solid("#e3b34c")
                    padding (36, 14)
                    text_size 26
                    text_bold True
                    text_color "#111111"

    key "K_ESCAPE" action Return()

label play_end_credits(ending_name="The Redemption Path"):
    $ hide_all_investigation_screens()
    $ current_day = 4
    hide screen global_hud
    $ set_cutscene_lock(False)

    python:
        if persistent.unlocked_endings is None:
            persistent.unlocked_endings = []
        if ending_name not in persistent.unlocked_endings:
            persistent.unlocked_endings.append(ending_name)
            renpy.save_persistent()

    stop ambient fadeout 1.5
    stop siren fadeout 1.5
    if not renpy.music.get_playing(channel="music"):
        play music "audio/bgm_main_menu.ogg" fadein 1.5 volume 0.70

    scene black with fade
    call screen end_credits_screen(ending_name)
    stop music fadeout 1.5
    return