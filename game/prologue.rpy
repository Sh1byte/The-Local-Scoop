image prologue_s1_1 = "gui/prologue/Shot 1.1.jpg"
image prologue_s1_2 = "gui/prologue/Shot 1.2.jpg"
image prologue_s1_3 = "gui/prologue/Shot 1.3.jpg"
image prologue_s1_4 = "gui/prologue/Shot 1.4.jpg"
image prologue_s1_5 = "gui/prologue/Shot 1.5.jpg"
image prologue_s1_6 = "gui/prologue/Shot 1.6.jpg"

image prologue_s2_1 = "gui/prologue/Shot 2.1.jpg"
image prologue_s2_2 = "gui/prologue/Shot 2.2.jpg"
image prologue_s2_3 = "gui/prologue/Shot 2.3.jpg"
image prologue_s2_4 = "gui/prologue/Shot 2.4.jpg"

image prologue_s3_1 = "gui/prologue/Shot 3.1.jpg"

image prologue_s4_1 = "gui/prologue/Shot 4.1.jpg"
image prologue_s4_2 = "gui/prologue/Shot 4.2.jpg"

screen prologue_cutscene_lock():
    zorder 100
    key "dismiss" action Function(finish_cps_only)
    key "skip" action NullAction()
    key "fast_skip" action NullAction()
    key "toggle_skip" action NullAction()
    key "rollback" action NullAction()
    key "rollforward" action NullAction()

label prologue_start:
    $ current_day = 4
    $ hide_all_investigation_screens()
    show screen global_hud
    $ set_cutscene_lock(True, 22)

    play music "audio/bgm_ending_dark.ogg" fadeout 1.0 fadein 1.5 volume 0.55 if_changed
    play ambient "audio/amb_newsroom.ogg" fadeout 0.8 fadein 1.5 volume 0.70 if_changed
    scene black

    scene prologue_s1_1 with fade
    "{cps=22}My first job was an office job.{/cps}{w=2.2}{nw}"
    "{cps=22}I thought all I ever needed was a desk job and I'll be set for life, how hard is it to sit all day right?{/cps}{w=3.0}{nw}"

    play sound "audio/sfx_paper_rustle.ogg"
    scene prologue_s1_2 with dissolve
    "{cps=22}At first I thought I just need to adjust on the workload, maybe once I get used to it everything will go smoother.{/cps}{w=3.0}{nw}"

    play sound "audio/sfx_paper_rustle.ogg"
    scene prologue_s1_3 with dissolve
    "{cps=22}But every time I tried to trick myself that I can handle this job...{/cps}{w=2.5}{nw}"

    play sound "audio/sfx_paper_rustle.ogg"
    scene prologue_s1_4 with dissolve
    "{cps=22}The paper works say otherwise.{/cps}{w=2.5}{nw}"

    play sound "audio/sfx_paper_rustle.ogg"
    scene prologue_s1_5 with dissolve
    "{cps=22}Again, and again and again.{/cps}{w=2.5}{nw}"

    scene prologue_s1_6 with dissolve
    "{cps=22}Until I decided to make a change.{/cps}{w=2.5}{nw}"

    stop ambient fadeout 1.0
    scene black with fade

    play ambient "audio/amb_market_plaza.ogg" fadein 1.2 volume 0.70
    scene prologue_s2_1 with fade
    "{cps=22}Since I was a child I have always wanted to be a reporter,{/cps}{w=2.5}{nw}"

    scene prologue_s2_2 with dissolve
    "{cps=22}the guys you see on TV and the ones other kids ignored.{/cps}{w=2.5}{nw}"

    scene prologue_s2_3 with dissolve
    "{cps=22}But not me.{/cps}{w=2.2}{nw}"

    scene prologue_s2_4 with dissolve
    "{cps=22}I don't want to fail that kid.{/cps}{w=2.5}{nw}"
    stop ambient fadeout 0.8

    play sound "audio/sfx_paper_rustle.ogg"
    play sting "audio/sting_clue_major.ogg" volume 0.75
    play music "audio/bgm_ending_dark.ogg" fadein 0.8 volume 0.55 if_changed
    play ambient "audio/amb_newsroom.ogg" fadein 0.8 volume 0.70
    scene prologue_s3_1 with dissolve
    "{cps=22}That's why I'll make a change.{/cps}{w=2.8}{nw}"

    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black with fade

    play sting "audio/sting_day_transition.ogg" volume 0.75
    play music "audio/bgm_newsroom.ogg" fadein 1.5 volume 0.50
    play ambient "audio/amb_city_daytime.ogg" fadein 1.2 volume 0.80
    play sound "audio/sfx_footsteps_move.ogg"

    scene prologue_s4_1 with fade
    "{cps=22}Looks like this is it, Herald News Station, Lualhati street, Barangay Ligalig.{/cps}{w=3.0}{nw}"

    scene prologue_s4_2 with dissolve
    pause 2.5
    stop ambient fadeout 1.0
    scene black with fade

    $ set_cutscene_lock(False)
    $ current_day = 1
    $ renpy.force_autosave(True)
    jump tutorial_start