default took_cash = False

image day4_s1_1 = "gui/day4/Scene 1/Scene 1_1.jpg"
image day4_s1_2 = "gui/day4/Scene 1/Scene 1_2.jpg"
image day4_s1_3 = "gui/day4/Scene 1/Scene 1_3.jpg"
image day4_s1_4 = "gui/day4/Scene 1/Scene 1_4.jpg"
image day4_s1_5 = "gui/day4/Scene 1/Scene 1_5.jpg"
image day4_s1_6 = "gui/day4/Scene 1/Scene 1_6.jpg"
image day4_s1_7 = "gui/day4/Scene 1/Scene 1_7.jpg"
image day4_s1_8 = "gui/day4/Scene 1/Scene 1_8.jpg"
image day4_s1_9 = "gui/day4/Scene 1/Scene 1_9.jpg"

image day4_s2_1  = "gui/day4/Scene 2/Scene 2_1.jpg"
image day4_s2_2  = "gui/day4/Scene 2/Scene 2_2.jpg"
image day4_s2_3  = "gui/day4/Scene 2/Scene 2_3.jpg"
image day4_s2_4  = "gui/day4/Scene 2/Scene 2_4.jpg"
image day4_s2_5  = "gui/day4/Scene 2/Scene 2_5.jpg"
image day4_s2_6  = "gui/day4/Scene 2/Scene 2_6.jpg"
image day4_s2_7  = "gui/day4/Scene 2/Scene 2_7.jpg"
image day4_s2_8  = "gui/day4/Scene 2/Scene 2_8.jpg"
image day4_s2_9  = "gui/day4/Scene 2/Scene 2_9.jpg"
image day4_s2_10 = "gui/day4/Scene 2/Scene 2_10.jpg"
image day4_s2_11 = "gui/day4/Scene 2/Scene 2_11.jpg"
image day4_s2_12 = "gui/day4/Scene 2/Scene 2_12.jpg"
image day4_s2_13 = "gui/day4/Scene 2/Scene 2_13.jpg"
image day4_s2_14 = "gui/day4/Scene 2/Scene 2_14.jpg"
image day4_s2_15 = "gui/day4/Scene 2/Scene 2_15.jpg"
image day4_s2_16 = "gui/day4/Scene 2/Scene 2_16.jpg"
image day4_s2_17 = "gui/day4/Scene 2/Scene 2_17.jpg"
image day4_s2_18 = "gui/day4/Scene 2/Scene 2_18.jpg"
image day4_s2_19 = "gui/day4/Scene 2/Scene 2_19.jpg"
image day4_s2_20 = "gui/day4/Scene 2/Scene 2_20.jpg"
image day4_s2_21 = "gui/day4/Scene 2/Scene 2_21.jpg"
image day4_s2_22 = "gui/day4/Scene 2/Scene 2_22.jpg"

image day4_c1_1 = "gui/day4/Choice 1/Scene C1_1.jpeg"
image day4_c1_2 = "gui/day4/Choice 1/Scene C1_2.jpeg"
image day4_c1_3 = "gui/day4/Choice 1/Scene C1_3.jpeg"
image day4_c1_4 = "gui/day4/Choice 1/Scene C1_4.jpeg"
image day4_c1_5 = "gui/day4/Choice 1/Scene C1_5.jpeg"
image day4_c1_6 = "gui/day4/Choice 1/Scene C1_6.jpeg"

image day4_c2_1 = "gui/day4/Choice 2/Scene C2_1.jpeg"
image day4_c2_2 = "gui/day4/Choice 2/Scene C2_2.jpeg"
image day4_c2_3 = "gui/day4/Choice 2/Scene C2_3.jpeg"
image day4_c2_4 = "gui/day4/Choice 2/Scene C2_4.jpeg"
image day4_c2_5 = "gui/day4/Choice 2/Scene C2_5.jpeg"

image day4_c3_1 = "gui/day4/Choice 1/Scene C1_1.jpeg"
image day4_c3_2 = "gui/day4/Choice 3/Scene C3_2.jpeg"
image day4_c3_3 = "gui/day4/Choice 3/Scene C3_3.jpeg"
image day4_c3_4 = "gui/day4/Choice 3/Scene C3_4.jpeg"
image day4_c3_5 = "gui/day4/Choice 3/Scene C3_5.jpeg"
image day4_c3_6 = "gui/day4/Choice 3/Scene C3_6.jpeg"
image day4_c3_7 = "gui/day4/Choice 3/Scene C3_7.jpg"

transform day4_choice_hover:
    transform_anchor True
    on idle:
        easein 0.15 zoom 1.0
    on hover:
        easein 0.15 zoom 1.18

transform day4_yellow_timer_bar(duration=15.0):
    xalign 0.5
    yalign 0.96
    xzoom 1.0
    linear duration xzoom 0.0

screen day4_timer_choice(has_all_evidence=False):
    modal True
    zorder 50
    on "show" action Show("global_hud")
    if has_all_evidence:
        timer 15.0 action Return("timeout")
    hbox:
        align (0.5, 0.82)
        spacing 220
        textbutton "TAKE IT":
            at day4_choice_hover
            hover_sound "audio/ui_hover.ogg"
            activate_sound "audio/ui_click.ogg"
            action Return("take")
            background None
            hover_background Solid("#FF000038")
            padding (28, 14)
            text_size 48
            text_bold True
            text_color "#FF0000"
            text_hover_color "#FF5555"
            text_outlines [(3, "#000000", 0, 0)]
            text_hover_outlines [(4, "#FFFF00", 0, 0), (2, "#000000", 0, 0)]
        textbutton "LEAVE IT":
            at day4_choice_hover
            hover_sound "audio/ui_hover.ogg"
            activate_sound "audio/ui_click.ogg"
            action Return("leave")
            background None
            hover_background Solid("#FF000038")
            padding (28, 14)
            text_size 48
            text_bold True
            text_color "#FF0000"
            text_hover_color "#FF5555"
            text_outlines [(3, "#000000", 0, 0)]
            text_hover_outlines [(4, "#FFFF00", 0, 0), (2, "#000000", 0, 0)]
    if has_all_evidence:
        add Solid("#000000AA", xsize=1720, ysize=14) xalign 0.5 yalign 0.96
        add Solid("#FFFF00", xsize=1720, ysize=14) at day4_yellow_timer_bar(15.0)
    if not renpy.get_screen("global_hud"):
        use global_hud

label day4_start:
    $ current_day = 4
    $ preferences.set_mixer("music", 0.70)
    $ hide_all_investigation_screens()
    show screen global_hud
    $ set_cutscene_lock(True, 22)

    play sting "audio/sting_day_transition.ogg" volume 0.75
    play music "audio/bgm_day4_confrontation.ogg" fadeout 1.0 fadein 1.5 volume 0.70 if_changed
    play ambient "audio/amb_newsroom.ogg" fadeout 0.8 fadein 1.0 volume 0.35 if_changed
    scene bg newsroom

    scene day4_s1_1 with dissolve
    "{cps=22}The air inside Kenneth's office was heavy with tension as Arthur and I stood motionless in front of his desk, bracing ourselves for his anger.{/cps}{w=2.5}{nw}"

    play sound "audio/sfx_desk_slam.ogg"
    scene day4_s1_2 with dissolve
    "{cps=22}Without warning, Kenneth slammed both of his hands hard onto the desk, the loud thud echoing across the entire room.{/cps}{w=2.5}{nw}"

    scene day4_s1_3 with dissolve
    kenneth "{cps=22}I TOLD BOTH OF YOU TO DROP THE GANG STORY AND FOCUS ON SOMETHING ELSE. YET YOU DISRESPECTED MY ORDER AND SNUCK BEHIND MY BACK TO MAKE A REPORT ABOUT THE CASINO ISSUE!!{/cps}{w=3.0}{nw}"

    scene day4_s1_4 with dissolve
    arthur "{cps=22}But boss, these events seem to be connected and part of something much bigger.{/cps}{w=2.5}{nw}"

    scene day4_s1_5 with dissolve
    "{cps=22}Yeah, and I even overheard a group of people at the bar saying that the man behind one of the gangs is someone powerful who can control the entire town.{/cps}{w=3.0}{nw}"

    scene day4_s1_6 with dissolve
    kenneth "{cps=22}I get it that you both want this big break, but meddling with something as dangerous as this could cost me my 2 greatest reporters.{/cps}{w=3.0}{nw}"

    scene day4_s1_7 with dissolve
    "{cps=22}Arthur and I exchanged a frustrated glance. We knew we were closer to the truth than ever, yet there was no convincing him right now.{/cps}{w=2.5}{nw}"

    scene day4_s1_8 with dissolve
    kenneth "{cps=22}I think both of you need to take a day off. I'll be confiscating your camera and take the day to do something other than putting yourselves in danger.{/cps}{w=3.0}{nw}"

    play sound "audio/sfx_camera_surrender.ogg"
    scene day4_s1_9 with dissolve
    "{cps=22}Reluctantly, we surrendered our cameras onto his desk. Stripped of our equipment and forced off the case, we had no choice but to walk out.{/cps}{w=2.5}{nw}"

    play sound "audio/sfx_door_open.ogg"
    stop music fadeout 1.5
    stop ambient fadeout 1.0
    scene black with fade

    play ambient "audio/amb_city_daytime.ogg" fadein 1.0 volume 0.45
    scene bg main_street with fade

    play sound "audio/sfx_footsteps_move.ogg"
    scene day4_s2_1 with dissolve
    "{cps=22}Hours passed as I walked down the busy streets of town, trying to clear my head after the heated confrontation at the office.{/cps}{w=2.5}{nw}"
    "{cps=22}(Since the boss laid me off, I think I'll treat myself to some alone time at the mall.){/cps}{w=2.5}{nw}"

    play sound "audio/sfx_footsteps_move.ogg"
    scene day4_s2_2 with dissolve
    "{cps=22}(But first I'll need to get some money from the bank.){/cps}{w=2.5}{nw}"

    play sound "audio/sfx_door_open.ogg"
    play ambient "audio/amb_bank_lobby.ogg" fadeout 0.6 fadein 0.8 volume 0.45
    scene day4_s2_3 with dissolve
    "{cps=22}It was just a normal, quiet afternoon inside the bank. People stood calmly in line while the tellers went about their usual business... until suddenly—{/cps}{w=2.5}{nw}"

    stop ambient
    play sound "audio/sfx_bank_explosion.ogg"
    play ambient "audio/sfx_crowd_panic.ogg" fadein 0.1 volume 0.65
    play music "audio/bgm_day4_heist_action.ogg" fadein 0.2 volume 0.70
    scene day4_s2_4 with vpunch
    "{cps=22}BOOM! The front doors violently exploded inward, sending shattered glass, smoke, and debris flying everywhere!{/cps}{w=2.5}{nw}"

    scene day4_s2_5 with dissolve
    "{cps=22}Through the thick cloud of smoke, a crew of heavily armed men in masks stormed into the building, aiming rifles as panicked screams filled the lobby.{/cps}{w=2.8}{nw}"

    stop ambient fadeout 0.4
    play sound "audio/sfx_cash_briefcase.ogg"
    scene day4_s2_6 with dissolve
    "{cps=22}Moving quickly and ruthlessly, the masked men breached the open vault and began stuffing stacks of cash into metal briefcases.{/cps}{w=2.8}{nw}"

    play siren "audio/sfx_police_sirens.ogg" fadein 0.3 volume 0.55
    scene day4_s2_7 with dissolve
    "{cps=22}Before the robbers could slip away unnoticed, sirens wailed in the distance and armed police officers rushed in to surround the bank.{/cps}{w=2.8}{nw}"

    scene day4_s2_8 with dissolve
    "{cps=22}Carrying the stolen money, the masked crew sprinted back toward the ruined front entrance to make their escape.{/cps}{w=2.5}{nw}"

    play sound "audio/sfx_gun_cock.ogg"
    scene day4_s2_9 with dissolve
    "{cps=22}However, the police had already formed a tight blockade outside, cutting off their exit with guns drawn.{/cps}{w=2.5}{nw}"

    play ambient "audio/sfx_gunfight_loop.ogg" fadein 0.2 volume 0.55
    scene day4_s2_10 with vpunch
    "{cps=22}Refusing to surrender, the robbers opened fire! Within seconds, the front of the bank erupted into a fierce, deafening shootout.{/cps}{w=2.8}{nw}"

    scene day4_s2_11 with dissolve
    "{cps=22}Having scrambled out into a narrow alley across the street, I crouched behind cover and watched the deadly crossfire unfold right before my eyes.{/cps}{w=2.8}{nw}"

    play sound "audio/sfx_footsteps_move.ogg"
    scene day4_s2_12 with dissolve
    "{cps=22}In the middle of the chaos, one masked man clutching a briefcase broke away from the pack, sprinting down the street as bullets chipped the pavement behind him.{/cps}{w=3.0}{nw}"

    scene day4_s2_13 with dissolve
    "{cps=22}He twisted around as he ran, firing blind shots back at the pursuing officers to keep them pinned down.{/cps}{w=2.5}{nw}"

    scene day4_s2_14 with dissolve
    "{cps=22}The entire street had descended into total pandemonium, with gunfire echoing off the buildings and smoke rising into the sky.{/cps}{w=2.8}{nw}"

    scene day4_s2_15 with dissolve
    "Police" "{cps=22}STOP RIGHT THERE! AND SURRENDER, YOUR GANG HAS CAUSED THIS TOWN TOO MUCH DAMAGE!!{/cps}{w=2.8}{nw}"

    scene day4_s2_16 with dissolve
    "Man in mask" "{cps=22}SHIT! THE COPS ARE HERE!{/cps}{w=2.2}{nw}"

    stop ambient fadeout 0.8
    play sound "audio/sfx_car_getaway.ogg"
    scene day4_s2_17 with dissolve
    "{cps=22}Tires screeched against the asphalt as the getaway car lurched forward, roaring down the road in a desperate bid to escape.{/cps}{w=2.5}{nw}"

    stop siren fadeout 0.4
    play sound "audio/sfx_tire_blowout.ogg"
    scene day4_s2_18 with vpunch
    "{cps=22}BANG! A well-placed shot from the police blew out the car's tire, sending the vehicle skidding violently across the road!{/cps}{w=2.8}{nw}"

    play sound "audio/sfx_car_crash.ogg"
    scene day4_s2_19 with vpunch
    "{cps=22}With a screech of tearing metal, the car lost balance, flipped through the air, and crashed upside down onto the street.{/cps}{w=2.8}{nw}"

    play sound "audio/sfx_briefcase_slide.ogg"
    scene day4_s2_20 with dissolve
    "{cps=22}The force of the crash sent the heavy briefcase flying right out of the shattered window.{/cps}{w=2.5}{nw}"

    scene day4_s2_21 with dissolve
    "{cps=22}It tumbled across the concrete and slid to a halt right at my feet inside the alley.{/cps}{w=2.5}{nw}"

    play ambient "audio/sfx_heartbeat_timer.ogg" fadein 0.3 volume 0.70
    scene day4_s2_22 with dissolve
    "{cps=22}My heart hammered against my ribs as I stared down at the briefcase. No one was looking this way yet... Should I take it and run, or leave it behind?!{/cps}{w=2.5}{nw}"

    $ all_police_evidence = (evidence_lighter and evidence_letter and evidence_ledger)
    hide screen prologue_cutscene_lock
    call screen day4_timer_choice(has_all_evidence=all_police_evidence)
    $ choice = _return
    stop ambient fadeout 0.3
    show screen prologue_cutscene_lock

    if choice == "take":
        $ took_cash = True
        play sound "audio/sfx_pickup_item.ogg"
        scene day4_c1_1 with dissolve
        "{cps=22}Acting on pure adrenaline, I reached down, grabbed the handle of the briefcase, and pulled it off the ground.{/cps}{w=2.5}{nw}"

        play sound "audio/sfx_run_panting.ogg"
        scene day4_c1_2 with dissolve
        "{cps=22}(I AM IN BIG TROUBLE!!){/cps}{w=2.2}{nw}"
        "{cps=22}(IT'S FINE, THEY DIDN'T SEE MY FACE, I'LL BE FINE){/cps}{w=2.5}{nw}"

        play music "audio/bgm_day4_confrontation.ogg" fadeout 1.5 fadein 1.5 volume 0.70
        scene day4_c1_3 with dissolve
        "{cps=22}(I should stop somewhere to catch my breath.){/cps}{w=2.5}{nw}"

        play sound "audio/sfx_cash_briefcase.ogg"
        scene day4_c1_4 with dissolve
        "{cps=22}Ducking deep into a secluded alleyway far from the gunfire, I checked my surroundings and unlatched the locks on the briefcase.{/cps}{w=2.8}{nw}"

        play sting "audio/sting_greed_grin.ogg" volume 0.80
        scene day4_c1_5 with dissolve
        "{cps=22}HOLY SHIT, IT'S MONEY! A BRIEFCASE FULL OF MONEY!{/cps}{w=2.5}{nw}"
        "{cps=22}(Maybe they would think that the rival gang took the money and this would finally start a war between the two.){/cps}{w=3.0}{nw}"

        scene day4_c1_6 with dissolve
        "{cps=22}Looks like the problem will solve itself.{/cps}{w=2.5}{nw}"
        stop music fadeout 1.5

        $ set_cutscene_lock(False)
        $ renpy.force_autosave(True)
        jump day5_path_a_start

    elif choice == "leave":
        $ took_cash = False
        play sound "audio/sfx_footsteps_move.ogg"
        scene day4_c2_1 with dissolve
        "{cps=22}No amount of money was worth getting killed over. I took a step back and turned away from the briefcase.{/cps}{w=2.5}{nw}"

        play sound "audio/sfx_run_panting.ogg"
        scene day4_c2_2 with dissolve
        "{cps=22}Without looking back, I sprinted out of the alley as fast as my legs could carry me, desperate to get away from the gunfire.{/cps}{w=2.8}{nw}"

        scene day4_c2_3 with dissolve
        "{cps=22}(HOLY COW, I THOUGHT I WAS A GONNER!){/cps}{w=2.5}{nw}"

        stop music fadeout 2.0
        play ambient "audio/amb_city_daytime.ogg" fadein 1.5 volume 0.45
        scene day4_c2_4 with dissolve
        "{cps=22}I think I'm safe here.{/cps}{w=2.2}{nw}"

        scene day4_c2_5 with dissolve
        "{cps=22}Well, I guess mall time is cancelled. I should go home and rest.{/cps}{w=2.5}{nw}"
        stop ambient fadeout 1.5

        $ set_cutscene_lock(False)
        $ renpy.force_autosave(True)
        jump day5_path_a_start

    elif choice == "timeout":
        play music "audio/bgm_day4_betrayal.ogg" fadeout 0.8 fadein 1.0 volume 0.70

        play sound "audio/sfx_glass_footsteps.ogg"
        scene day4_c3_1 with dissolve
        "{cps=22}I hesitated for too long, finally reaching down toward the briefcase just as footsteps crunched against the broken glass behind me.{/cps}{w=2.8}{nw}"
        "{cps=22}(I wonder what could be insi—){/cps}{w=2.0}{nw}"

        scene day4_c3_2 with dissolve
        "Man in mask" "{cps=22}HEY YOU! GET AWAY FROM THERE!{/cps}{w=2.5}{nw}"

        play sound "audio/sfx_gun_cock.ogg"
        scene day4_c3_3 with dissolve
        "{cps=22}I'm sorry, I wasn't gonna do anything, please don't shoot me!{/cps}{w=2.5}{nw}"

        scene day4_c3_4 with dissolve
        "Man in mask" "{cps=22}I TOLD YOU TO GET AWAY, NOT RAISE YOUR HANDS AND BEG!{/cps}{w=2.5}{nw}"
        "{cps=22}Right, right. I'm sorry.{/cps}{w=2.2}{nw}"

        play sting "audio/sting_boss_twist.ogg" volume 0.85
        scene day4_c3_5 with dissolve
        "{cps=22}BOSS?!{/cps}{w=2.0}{nw}"
        "Man in mask" "{cps=22}Why did you have to notice, kid?{/cps}{w=2.5}{nw}"
        "{cps=22}So all this time you weren't keeping us away from the gang stories to protect us? You were keeping us away to protect you!{/cps}{w=3.0}{nw}"
        "Man in mask" "{cps=22}Eyy, he's all caught up.{/cps}{w=2.2}{nw}"
        "{cps=22}I get it now. You're the man powerful enough to control the entire town—the boss of the local newspaper company. Powerful enough to control the town's feelings.{/cps}{w=3.5}{nw}"

        play sound "audio/sfx_gun_cock.ogg"
        scene day4_c3_6 with dissolve
        "Man in mask" "{cps=22}You don't have to analyze the situation anymore, because you won't get the chance to write a report about this.{/cps}{w=3.0}{nw}"

        stop music
        stop ambient
        stop siren
        play sound "audio/sfx_gunshot_execution.ogg"
        scene day4_c3_7 with vpunch
        "{cps=22}A blinding flash erupted from the barrel as a deafening gunshot echoed through the alley, and everything went pitch black.{/cps}{w=2.8}{nw}"
        scene black with fade

        $ set_cutscene_lock(False)
        $ renpy.force_autosave(True)
        jump day5_path_b_start