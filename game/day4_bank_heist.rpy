default took_cash = False

# ==============================================================================
# DAY 4 IMAGE DEFINITIONS (1920 x 1080)
# ==============================================================================

# --- Scene 1: Kenneth's Office (.jpg) ---
image day4_s1_1 = "gui/day4/Scene 1/Scene 1_1.jpg"
image day4_s1_2 = "gui/day4/Scene 1/Scene 1_2.jpg"
image day4_s1_3 = "gui/day4/Scene 1/Scene 1_3.jpg"
image day4_s1_4 = "gui/day4/Scene 1/Scene 1_4.jpg"
image day4_s1_5 = "gui/day4/Scene 1/Scene 1_5.jpg"
image day4_s1_6 = "gui/day4/Scene 1/Scene 1_6.jpg"
image day4_s1_7 = "gui/day4/Scene 1/Scene 1_7.jpg"
image day4_s1_8 = "gui/day4/Scene 1/Scene 1_8.jpg"
image day4_s1_9 = "gui/day4/Scene 1/Scene 1_9.jpg"

# --- Scene 2: The Bank Heist (.jpg) ---
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

# --- Choice 1: Took the Briefcase (.jpeg) ---
image day4_c1_1 = "gui/day4/Choice 1/Scene C1_1.jpeg"
image day4_c1_2 = "gui/day4/Choice 1/Scene C1_2.jpeg"
image day4_c1_3 = "gui/day4/Choice 1/Scene C1_3.jpeg"
image day4_c1_4 = "gui/day4/Choice 1/Scene C1_4.jpeg"
image day4_c1_5 = "gui/day4/Choice 1/Scene C1_5.jpeg"
image day4_c1_6 = "gui/day4/Choice 1/Scene C1_6.jpeg"

# --- Choice 2: Left the Briefcase (.jpeg) ---
image day4_c2_1 = "gui/day4/Choice 2/Scene C2_1.jpeg"
image day4_c2_2 = "gui/day4/Choice 2/Scene C2_2.jpeg"
image day4_c2_3 = "gui/day4/Choice 2/Scene C2_3.jpeg"
image day4_c2_4 = "gui/day4/Choice 2/Scene C2_4.jpeg"
image day4_c2_5 = "gui/day4/Choice 2/Scene C2_5.jpeg"

# --- Choice 3: Timeout / Caught by Kenneth (.jpeg & .jpg) ---
image day4_c3_1 = "gui/day4/Choice 1/Scene C1_1.jpeg"
image day4_c3_2 = "gui/day4/Choice 3/Scene C3_2.jpeg"
image day4_c3_3 = "gui/day4/Choice 3/Scene C3_3.jpeg"
image day4_c3_4 = "gui/day4/Choice 3/Scene C3_4.jpeg"
image day4_c3_5 = "gui/day4/Choice 3/Scene C3_5.jpeg"
image day4_c3_6 = "gui/day4/Choice 3/Scene C3_6.jpeg"
image day4_c3_7 = "gui/day4/Choice 3/Scene C3_7.jpg"


# ==============================================================================
# SCREENS & TRANSFORMS FOR UNSKIPPABLE CUTSCENE & TIMED CHOICE
# ==============================================================================

# Blocks mouse clicks, Space, Enter, Ctrl, Tab, and Scrollback during cutscenes
screen day4_cutscene_lock():
    zorder 100
    key "dismiss" action NullAction()
    key "skip" action NullAction()
    key "fast_skip" action NullAction()
    key "toggle_skip" action NullAction()
    key "rollback" action NullAction()
    key "rollforward" action NullAction()

# Hover effect for "TAKE IT" and "LEAVE IT" buttons
transform day4_choice_hover:
    transform_anchor True
    on idle:
        easein 0.15 zoom 1.0
    on hover:
        easein 0.15 zoom 1.18

# Yellow timer bar shrinking over 15 seconds at the bottom of the screen
transform day4_yellow_timer_bar(duration=15.0):
    xalign 0.5
    yalign 0.96
    xzoom 1.0
    linear duration xzoom 0.0

screen day4_timer_choice(has_all_evidence=False):
    modal True
    zorder 50

    # Only enable the 15-second timer if the player gathered ALL police evidence
    if has_all_evidence:
        timer 15.0 action Return("timeout")

    # Side-by-side red choices
    hbox:
        align (0.5, 0.82)
        spacing 220
        textbutton "TAKE IT":
            at day4_choice_hover
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

    # Only show the shrinking yellow timer bar if the timer is active
    if has_all_evidence:
        add Solid("#000000AA", xsize=1720, ysize=14) xalign 0.5 yalign 0.96
        add Solid("#FFFF00", xsize=1720, ysize=14) at day4_yellow_timer_bar(15.0)


# ==============================================================================
# DAY 4 STORY SCRIPT
# ==============================================================================

label day4_start:
    $ current_day = 4 # Hides the global HUD bag icon

    # Lock skipping, rollback, pause dismissal, and force typing effect
    $ _day4_old_cps = preferences.text_cps
    $ preferences.text_cps = 22
    $ _skipping = False
    $ _rollback = False
    $ _dismiss_pause = False
    $ quick_menu = False
    show screen day4_cutscene_lock

    # --------------------------------------------------------------------------
    # SCENE 1: KENNETH'S OFFICE
    # --------------------------------------------------------------------------
    scene bg newsroom

    #Scene 1.1 showing kenneth's office with kenneth sitting behind his desk and arthur and the player standing in front of him getting yelled at
    scene day4_s1_1 with dissolve
    "{cps=22}The air inside Kenneth's office was heavy with tension as Arthur and I stood motionless in front of his desk, bracing ourselves for his anger.{/cps}{w=2.5}{nw}"

    #Scene 1.2 showing the desk of kenneth and him slamming his hands on it
    scene day4_s1_2 with dissolve
    "{cps=22}Without warning, Kenneth slammed both of his hands hard onto the desk, the loud thud echoing across the entire room.{/cps}{w=2.5}{nw}"

    #Scene 1.3 showing kenneth yelling at the player and arthur
    scene day4_s1_3 with dissolve
    kenneth "{cps=22}I TOLD BOTH OF YOU TO DROP THE GANG STORY AND FOCUS ON SOMETHING ELSE. YET YOU DISRESPECTED MY ORDER AND SNUCK BEHIND MY BACK TO MAKE A REPORT ABOUT THE CASINO ISSUE!!{/cps}{w=3.0}{nw}"

    #Scene 1.4 showing arthur reasoning with kenneth
    scene day4_s1_4 with dissolve
    arthur "{cps=22}But boss, these events seem to be connected and part of something much bigger.{/cps}{w=2.5}{nw}"

    #Scene 1.5 showing arthur and the player side by side trying to reason with kenneth
    scene day4_s1_5 with dissolve
    "{cps=22}Yeah, and I even overheard a group of people at the bar saying that the man behind one of the gangs is someone powerful who can control the entire town.{/cps}{w=3.0}{nw}"

    #Scene 1.6 showing kenneth talking to both with open arms
    scene day4_s1_6 with dissolve
    kenneth "{cps=22}I get it that you both want this big break, but meddling with something as dangerous as this could cost me my 2 greatest reporters.{/cps}{w=3.0}{nw}"

    #Scene 1.7 showing arthur and the player looking at each other
    scene day4_s1_7 with dissolve
    "{cps=22}Arthur and I exchanged a frustrated glance. We knew we were closer to the truth than ever, yet there was no convincing him right now.{/cps}{w=2.5}{nw}"

    #Scene 1.8 showing kenneth reaching out his arm to take away their camera
    scene day4_s1_8 with dissolve
    kenneth "{cps=22}I think both of you need to take a day off. I'll be confiscating your camera and take the day to do something other than putting yourselves in danger.{/cps}{w=3.0}{nw}"

    #Scene 1.9 showing kenneth's desk with 2 cameras on it
    scene day4_s1_9 with dissolve
    "{cps=22}Reluctantly, we surrendered our cameras onto his desk. Stripped of our equipment and forced off the case, we had no choice but to walk out.{/cps}{w=2.5}{nw}"

    scene black with fade

    # --------------------------------------------------------------------------
    # SCENE 2: THE BANK HEIST
    # --------------------------------------------------------------------------
    scene bg main_street with fade

    #Scene 2.1 showing the bank far away
    scene day4_s2_1 with dissolve
    "{cps=22}Hours passed as I walked down the busy streets of town, trying to clear my head after the heated confrontation at the office.{/cps}{w=2.5}{nw}"
    "{cps=22}(Since the boss laid me off, I think I'll treat myself to some alone time at the mall.){/cps}{w=2.5}{nw}"

    #Scene 2.2 showing the front of the bank closer
    scene day4_s2_2 with dissolve
    "{cps=22}(But first I'll need to get some money from the bank.){/cps}{w=2.5}{nw}"

    #Scene 2.3 showing the inside of the bank nothing special
    scene day4_s2_3 with dissolve
    "{cps=22}It was just a normal, quiet afternoon inside the bank. People stood calmly in line while the tellers went about their usual business... until suddenly—{/cps}{w=2.5}{nw}"

    #Scene 2.4 showing a sudden explosion of the front door of the bank
    scene day4_s2_4 with vpunch
    "{cps=22}BOOM! The front doors violently exploded inward, sending shattered glass, smoke, and debris flying everywhere!{/cps}{w=2.5}{nw}"

    #Scene 2.5 showing multiple masked men entering the bank
    scene day4_s2_5 with dissolve
    "{cps=22}Through the thick cloud of smoke, a crew of heavily armed men in masks stormed into the building, aiming rifles as panicked screams filled the lobby.{/cps}{w=2.8}{nw}"

    #Scene 2.6 showing masked men taking money from the banks vault
    scene day4_s2_6 with dissolve
    "{cps=22}Moving quickly and ruthlessly, the masked men breached the open vault and began stuffing stacks of cash into metal briefcases.{/cps}{w=2.8}{nw}"

    #Scene 2.7 showing police entering the building
    scene day4_s2_7 with dissolve
    "{cps=22}Before the robbers could slip away unnoticed, sirens wailed in the distance and armed police officers rushed in to surround the bank.{/cps}{w=2.8}{nw}"

    #Scene 2.8 showing the masked men attempting to exit the building
    scene day4_s2_8 with dissolve
    "{cps=22}Carrying the stolen money, the masked crew sprinted back toward the ruined front entrance to make their escape.{/cps}{w=2.5}{nw}"

    #Scene 2.9 showing the masked men get blocked by the police
    scene day4_s2_9 with dissolve
    "{cps=22}However, the police had already formed a tight blockade outside, cutting off their exit with guns drawn.{/cps}{w=2.5}{nw}"

    #Scene 2.10 showing the masked men getting into a shootout with the police
    scene day4_s2_10 with vpunch
    "{cps=22}Refusing to surrender, the robbers opened fire! Within seconds, the front of the bank erupted into a fierce, deafening shootout.{/cps}{w=2.8}{nw}"

    #Scene 2.11 showing the pov of the player in the alley on the front of the bank shootout
    scene day4_s2_11 with dissolve
    "{cps=22}Having scrambled out into a narrow alley across the street, I crouched behind cover and watched the deadly crossfire unfold right before my eyes.{/cps}{w=2.8}{nw}"

    #Scene 2.12 showing one masked man running away from the bank while getting shot at by the police
    scene day4_s2_12 with dissolve
    "{cps=22}In the middle of the chaos, one masked man clutching a briefcase broke away from the pack, sprinting down the street as bullets chipped the pavement behind him.{/cps}{w=3.0}{nw}"

    #Scene 2.13 showing the masked man firing back at the police
    scene day4_s2_13 with dissolve
    "{cps=22}He twisted around as he ran, firing blind shots back at the pursuing officers to keep them pinned down.{/cps}{w=2.5}{nw}"

    #Scene 2.14 showing the wide shot aerial view of the bank shootout
    scene day4_s2_14 with dissolve
    "{cps=22}The entire street had descended into total pandemonium, with gunfire echoing off the buildings and smoke rising into the sky.{/cps}{w=2.8}{nw}"

    #Scene 2.15 showing the police shooting at the maske man while saying his dialogue
    scene day4_s2_15 with dissolve
    "Police" "{cps=22}STOP RIGHT THERE! AND SURRENDER, YOUR GANG HAS CAUSED THIS TOWN TOO MUCH DAMAGE!!{/cps}{w=2.8}{nw}"

    #Scene 2.16 showing the masked man getting into the getaway vehicle
    scene day4_s2_16 with dissolve
    "Man in mask" "{cps=22}SHIT! THE COPS ARE HERE!{/cps}{w=2.2}{nw}"

    #Scene 2.17 showing the car driving away from the bank
    scene day4_s2_17 with dissolve
    "{cps=22}Tires screeched against the asphalt as the getaway car lurched forward, roaring down the road in a desperate bid to escape.{/cps}{w=2.5}{nw}"

    #Scene 2.18 showing the tire of the car get shot by the police and burst and skids on the road
    scene day4_s2_18 with vpunch
    "{cps=22}BANG! A well-placed shot from the police blew out the car's tire, sending the vehicle skidding violently across the road!{/cps}{w=2.8}{nw}"

    #Scene 2.19 showing the car tuppleing over now upside down
    scene day4_s2_19 with vpunch
    "{cps=22}With a screech of tearing metal, the car lost balance, flipped through the air, and crashed upside down onto the street.{/cps}{w=2.8}{nw}"

    #Scene 2.20 showing the briefcase fly out of the car
    scene day4_s2_20 with dissolve
    "{cps=22}The force of the crash sent the heavy briefcase flying right out of the shattered window.{/cps}{w=2.5}{nw}"

    #Scene 2.21 showing the briefcase land close to the player
    scene day4_s2_21 with dissolve
    "{cps=22}It tumbled across the concrete and slid to a halt right at my feet inside the alley.{/cps}{w=2.5}{nw}"

    #Scene 2.22 showing the player pov while looking down to the briefcase contemplating if he should take it or not
    scene day4_s2_22 with dissolve
    "{cps=22}My heart hammered against my ribs as I stared down at the briefcase. No one was looking this way yet... Should I take it and run, or leave it behind?!{/cps}{w=2.5}{nw}"

    # --------------------------------------------------------------------------
    # PLAYER CHOICE (15 SECONDS)
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # PLAYER CHOICE (TIMED ONLY IF ALL POLICE EVIDENCE IS GATHERED)
    # --------------------------------------------------------------------------
    $ all_police_evidence = (evidence_lighter and evidence_letter and evidence_ledger)
    hide screen day4_cutscene_lock
    call screen day4_timer_choice(has_all_evidence=all_police_evidence)
    $ choice = _return
    show screen day4_cutscene_lock

    if choice == "take":
        $ took_cash = True
        # ----------------------------------------------------------------------
        # CHOICE 1: TOOK THE BRIEFCASE
        # ----------------------------------------------------------------------
        #Scene C1.1 showing the player picking up the briefcase
        scene day4_c1_1 with dissolve
        "{cps=22}Acting on pure adrenaline, I reached down, grabbed the handle of the briefcase, and pulled it off the ground.{/cps}{w=2.5}{nw}"
        #Scene C1.2 showing the player running away from the bank with the briefcase
        scene day4_c1_2 with dissolve
        "{cps=22}(I AM IN BIG TROUBLE!!){/cps}{w=2.2}{nw}"
        "{cps=22}(IT'S FINE, THEY DIDN'T SEE MY FACE, I'LL BE FINE){/cps}{w=2.5}{nw}"
        #Scene C1.3 showing the player slowing down to catch his breath
        scene day4_c1_3 with dissolve
        "{cps=22}(I should stop somewhere to catch my breath.){/cps}{w=2.5}{nw}"
        #Scene C1.4 showing player in an alley trying to open the briefcase
        scene day4_c1_4 with dissolve
        "{cps=22}Ducking deep into a secluded alleyway far from the gunfire, I checked my surroundings and unlatched the locks on the briefcase.{/cps}{w=2.8}{nw}"
        #Scene C1.5 showing the player opening the briefcase and seeing money inside
        scene day4_c1_5 with dissolve
        "{cps=22}HOLY SHIT, IT'S MONEY! A BRIEFCASE FULL OF MONEY!{/cps}{w=2.5}{nw}"
        "{cps=22}(Maybe they would think that the rival gang took the money and this would finally start a war between the two.){/cps}{w=3.0}{nw}"
        #Scene C1.6 showing the player clutching the briefcase with a grin on his face
        scene day4_c1_6 with dissolve
        "{cps=22}Looks like the problem will solve itself.{/cps}{w=2.5}{nw}"
        # Restore normal game controls before jumping to Day 5
        hide screen day4_cutscene_lock
        $ preferences.text_cps = _day4_old_cps
        $ _skipping = True
        $ _rollback = True
        $ _dismiss_pause = True
        $ quick_menu = True
        $ renpy.force_autosave(True)
        jump day5_path_a_start

    elif choice == "leave":
        $ took_cash = False
        # ----------------------------------------------------------------------
        # CHOICE 2: DID NOT TAKE THE BRIEFCASE
        # ----------------------------------------------------------------------
        #Scene C2.1 showing the foot of the player facing away from the briefcase
        scene day4_c2_1 with dissolve
        "{cps=22}No amount of money was worth getting killed over. I took a step back and turned away from the briefcase.{/cps}{w=2.5}{nw}"
        #Scene C2.2 showing the player running away from the bank
        scene day4_c2_2 with dissolve
        "{cps=22}Without looking back, I sprinted out of the alley as fast as my legs could carry me, desperate to get away from the gunfire.{/cps}{w=2.8}{nw}"
        #Scene C2.3 showing the player running much further away from the bank
        scene day4_c2_3 with dissolve
        "{cps=22}(HOLY COW, I THOUGHT I WAS A GONNER!){/cps}{w=2.5}{nw}"
        #Scene C2.4 showing the player going into a park to catch his breath
        scene day4_c2_4 with dissolve
        "{cps=22}I think I'm safe here.{/cps}{w=2.2}{nw}"
        #Scene C2.5 showing the player sitting on a bench in the park
        scene day4_c2_5 with dissolve
        "{cps=22}Well, I guess mall time is cancelled. I should go home and rest.{/cps}{w=2.5}{nw}"
        # Restore normal game controls before jumping to Day 5
        hide screen day4_cutscene_lock
        $ preferences.text_cps = _day4_old_cps
        $ _skipping = True
        $ _rollback = True
        $ _dismiss_pause = True
        $ quick_menu = True
        $ renpy.force_autosave(True)
        jump day5_path_a_start 

    elif choice == "timeout":
        # ----------------------------------------------------------------------
        # CHOICE 3: TIMER RAN OUT (CAUGHT BY KENNETH)
        # ----------------------------------------------------------------------
        #Scene C3.1 using Scene C1.1.jpg showing the player picking up the briefcase
        scene day4_c3_1 with dissolve
        "{cps=22}I hesitated for too long, finally reaching down toward the briefcase just as footsteps crunched against the broken glass behind me.{/cps}{w=2.8}{nw}"
        "{cps=22}(I wonder what could be insi—){/cps}{w=2.0}{nw}"

        #Scene C3.2 showing Kenneth shouting at the player while limping towards him
        scene day4_c3_2 with dissolve
        "Man in mask" "{cps=22}HEY YOU! GET AWAY FROM THERE!{/cps}{w=2.5}{nw}"

        #Scene C3.3 showing the player raising his hands in surrender while kenneth points a gun at him
        scene day4_c3_3 with dissolve
        "{cps=22}I'm sorry, I wasn't gonna do anything, please don't shoot me!{/cps}{w=2.5}{nw}"

        #Scene C3.4 showing Kenneth pointing a gun at the player his face more visible now
        scene day4_c3_4 with dissolve
        "Man in mask" "{cps=22}I TOLD YOU TO GET AWAY, NOT RAISE YOUR HANDS AND BEG!{/cps}{w=2.5}{nw}"
        "{cps=22}Right, right. I'm sorry.{/cps}{w=2.2}{nw}"

        #Scene C3.5 showing the player realizing he knows this robber
        scene day4_c3_5 with dissolve
        "{cps=22}BOSS?!{/cps}{w=2.0}{nw}"
        "Man in mask" "{cps=22}Why did you have to notice, kid?{/cps}{w=2.5}{nw}"
        "{cps=22}So all this time you weren't keeping us away from the gang stories to protect us? You were keeping us away to protect you!{/cps}{w=3.0}{nw}"
        "Man in mask" "{cps=22}Eyy, he's all caught up.{/cps}{w=2.2}{nw}"
        "{cps=22}I get it now. You're the man powerful enough to control the entire town—the boss of the local newspaper company. Powerful enough to control the town's feelings.{/cps}{w=3.5}{nw}"

        #Scene C3.6 Close up view of Kenneth's gun pointing at the player
        scene day4_c3_6 with dissolve
        "Man in mask" "{cps=22}You don't have to analyze the situation anymore, because you won't get the chance to write a report about this.{/cps}{w=3.0}{nw}"

        #Scene C3.7 Close up view of Kenneth's gun firing at the player
        scene day4_c3_7 with vpunch
        "{cps=22}A blinding flash erupted from the barrel as a deafening gunshot echoed through the alley, and everything went pitch black.{/cps}{w=2.8}{nw}"

        scene black with fade

        # Restore normal game controls before jumping to Day 5
        hide screen day4_cutscene_lock
        $ preferences.text_cps = _day4_old_cps
        $ _skipping = True
        $ _rollback = True
        $ _dismiss_pause = True
        $ quick_menu = True

        $ renpy.force_autosave(True)
        jump day5_path_b_start