# ==============================================================================
# PROLOGUE IMAGE DEFINITIONS (1920 x 1080)
# ==============================================================================
# --- Scene 1: The Cubicle Labyrinth (.jpg) ---
image prologue_s1_1 = "gui/prologue/Shot 1.1.jpg"
image prologue_s1_2 = "gui/prologue/Shot 1.2.jpg"
image prologue_s1_3 = "gui/prologue/Shot 1.3.jpg"
image prologue_s1_4 = "gui/prologue/Shot 1.4.jpg"
image prologue_s1_5 = "gui/prologue/Shot 1.5.jpg"
image prologue_s1_6 = "gui/prologue/Shot 1.6.jpg"
# --- Scene 2: The Window to Another World (.jpg) ---
image prologue_s2_1 = "gui/prologue/Shot 2.1.jpg"
image prologue_s2_2 = "gui/prologue/Shot 2.2.jpg"
image prologue_s2_3 = "gui/prologue/Shot 2.3.jpg"
image prologue_s2_4 = "gui/prologue/Shot 2.4.jpg"
# --- Scene 3: The Catalyst (.jpg) ---
image prologue_s3_1 = "gui/prologue/Shot 3.1.jpg"
# --- Scene 4: New Beginnings (.jpg) ---
image prologue_s4_1 = "gui/prologue/Shot 4.1.jpg"
image prologue_s4_2 = "gui/prologue/Shot 4.2.jpg"

# ==============================================================================
# SCREEN FOR UNSKIPPABLE PROLOGUE CUTSCENE
# ==============================================================================
# Clicking finishes the CPS typewriter effect immediately while still waiting
# for the {w=...} pause duration; blocks skipping and rollback
screen prologue_cutscene_lock():
    zorder 100
    key "dismiss" action Function(finish_cps_only)
    key "skip" action NullAction()
    key "fast_skip" action NullAction()
    key "toggle_skip" action NullAction()
    key "rollback" action NullAction()
    key "rollforward" action NullAction()

# ==============================================================================
# PROLOGUE STORY SCRIPT
# ==============================================================================
label prologue_start:
    # Set current_day = 4 so global_hud hides the Bag & News Van icons while keeping Settings visible
    $ current_day = 4
    $ hide_all_investigation_screens()
    show screen global_hud

    # Lock skipping, rollback, pause dismissal, and force typing effect (Day 4 style)
    $ _prologue_old_cps = preferences.text_cps
    $ preferences.text_cps = 22
    $ _skipping = False
    $ _rollback = False
    $ _dismiss_pause = False
    $ quick_menu = False
    show screen prologue_cutscene_lock

    # --------------------------------------------------------------------------
    # SCENE 1: THE CUBICLE LABYRINTH (DAYTIME — SHIFTING HOURS)
    # --------------------------------------------------------------------------
    play music "audio/bgm_ending_dark.ogg" fadeout 1.0 fadein 1.5 volume 0.55 if_changed
    play ambient "audio/amb_newsroom.ogg" fadeout 0.8 fadein 1.5 volume 0.70 if_changed
    scene black
    # Shot 1.1: Wide high-angle establishing shot of the depressing corporate office & cubicles
    scene prologue_s1_1 with fade
    "{cps=22}My first job was an office job.{/cps}{w=2.2}{nw}"
    "{cps=22}I thought all I ever needed was a desk job and I'll be set for life, how hard is it to sit all day right?{/cps}{w=3.0}{nw}"
    # Shot 1.2: Eye-level medium shot inside the cubicle (Morning) — small stack of paperwork
    play sound "audio/sfx_paper_rustle.ogg"
    scene prologue_s1_2 with dissolve
    "{cps=22}At first I thought I just need to adjust on the workload, maybe once I get used to it everything will go smoother.{/cps}{w=3.0}{nw}"
    # Shot 1.3: Same framing in late afternoon/evening — taller paperwork stack, rubbing temple
    play sound "audio/sfx_paper_rustle.ogg"
    scene prologue_s1_3 with dissolve
    "{cps=22}But every time I tried to trick myself that I can handle this job...{/cps}{w=2.5}{nw}"
    # Shot 1.4: Same framing late at night — dark office, desk lamp on, towering stacks of paperwork
    play sound "audio/sfx_paper_rustle.ogg"
    scene prologue_s1_4 with dissolve
    "{cps=22}The paper works say otherwise.{/cps}{w=2.5}{nw}"
    # Shot 1.5: Same framing next morning — mountains of paperwork swallowing the desk, slumped forward
    play sound "audio/sfx_paper_rustle.ogg"
    scene prologue_s1_5 with dissolve
    "{cps=22}Again, and again and again.{/cps}{w=2.5}{nw}"
    # Shot 1.6: Extreme close-up on the main character's tired eyes hardening with determination
    scene prologue_s1_6 with dissolve
    "{cps=22}Until I decided to make a change.{/cps}{w=2.5}{nw}"
    stop ambient fadeout 1.0
    scene black with fade

    # --------------------------------------------------------------------------
    # SCENE 2: THE WINDOW TO ANOTHER WORLD (CHILDHOOD FLASHBACK)
    # --------------------------------------------------------------------------
    play ambient "audio/amb_market_plaza.ogg" fadein 1.2 volume 0.70
    # Shot 2.1: Inside the traditional Filipino house at dusk while the CRT TV plays the evening news
    scene prologue_s2_1 with fade
    "{cps=22}Since I was a child I have always wanted to be a reporter,{/cps}{w=2.5}{nw}"
    # Shot 2.2: Outside the house showing the kid peeking through the window while other kids play
    scene prologue_s2_2 with dissolve
    "{cps=22}the guys you see on TV and the ones other kids ignored.{/cps}{w=2.5}{nw}"
    # Shot 2.3: Extreme close-up of the child's eyes illuminated by the light cast through the window
    scene prologue_s2_3 with dissolve
    "{cps=22}But not me.{/cps}{w=2.2}{nw}"
    # Shot 2.4: First-person POV of the kid peeking through the window at the tuxedoed TV news reporter
    scene prologue_s2_4 with dissolve
    "{cps=22}I don't want to fail that kid.{/cps}{w=2.5}{nw}"
    stop ambient fadeout 0.8

    # --------------------------------------------------------------------------
    # SCENE 3: THE CATALYST (THE CUBICLE — PRESENT DAY MATCH-CUT)
    # --------------------------------------------------------------------------
    # Shot 3.1: First-person top-down POV match-cut looking down at "HERALD NEWS IS NOW HIRING! APPLY NOW!"
    play sound "audio/sfx_paper_rustle.ogg"
    play sting "audio/sting_clue_major.ogg" volume 0.75
    play music "audio/bgm_ending_dark.ogg" fadein 0.8 volume 0.55 if_changed
    play ambient "audio/amb_newsroom.ogg" fadein 0.8 volume 0.70
    scene prologue_s3_1 with dissolve
    "{cps=22}That's why I'll make a change.{/cps}{w=2.8}{nw}"
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black with fade

    # --------------------------------------------------------------------------
    # SCENE 4: NEW BEGINNINGS (HERALD NEWS STATION — MORNING)
    # --------------------------------------------------------------------------
    play sting "audio/sting_day_transition.ogg" volume 0.75
    play music "audio/bgm_newsroom.ogg" fadein 1.5 volume 0.50
    play ambient "audio/amb_city_daytime.ogg" fadein 1.2 volume 0.80
    play sound "audio/sfx_footsteps_move.ogg"
    # Shot 4.1: First-person low-angle POV looking up at the Herald News building in the morning
    scene prologue_s4_1 with fade
    "{cps=22}Looks like this is it, Herald News Station, Lualhati street, Barangay Ligalig.{/cps}{w=3.0}{nw}"
    # Shot 4.2: Low-angle medium shot of the main character smiling hopefully outside the entrance
    scene prologue_s4_2 with dissolve
    pause 2.5
    stop ambient fadeout 1.0
    scene black with fade

    # Restore normal game controls and proceed to the Office Tutorial
    hide screen prologue_cutscene_lock
    $ preferences.text_cps = _prologue_old_cps
    $ _skipping = True
    $ _rollback = True
    $ _dismiss_pause = True
    $ quick_menu = True
    $ current_day = 1
    $ renpy.force_autosave(True)
    jump tutorial_start