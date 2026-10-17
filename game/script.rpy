label splashscreen:
    play music "gui/startup_menu_music.mp3" loop
    scene black
    show screen title_intro
    pause
    return

label start:
    stop music fadeout 1.0
    
    show screen global_hud

    # Jump directly into your Day 1 script
    jump stage1_briefing