# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

label splashscreen:
    play music "gui/startup_menu_music.mp3" loop
    scene black
    show screen title_intro
    pause
    return

# The game starts here.
label start:
    stop music fadeout 1.0
    
    # Jump directly into your Day 1 script
    jump stage1_briefing