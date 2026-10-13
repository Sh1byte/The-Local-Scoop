# 1. Python class to draw the transparent circle cutout
init python:
    class CircleMask(renpy.Displayable):
        def __init__(self, cx, cy, radius, **kwargs):
            super(CircleMask, self).__init__(**kwargs)
            self.cx = cx
            self.cy = cy
            self.radius = radius
            
        def render(self, width, height, st, at):
            r = renpy.Render(1920, 1080)
            canvas = r.canvas()
            # Draws a solid white circle which AlphaMask translates into transparency
            canvas.circle((255, 255, 255, 255), (self.cx, self.cy), self.radius)
            return r

# 2. Image and Transform Definitions
image bg tutorial_office = "gui/tutorial/bg_tutorial_office.png"

image kenneth welcome = "gui/tutorial/kenneth_welcome.png"
image kenneth explaining = "gui/tutorial/kenneth_explaining.png"
image kenneth thinking = "gui/tutorial/kenneth_thinking.png"
image kenneth welcome_open = "gui/tutorial/kenneth_welcome_open.png"

# --- REPLACE YOUR TRANSFORM DEFINITIONS WITH THIS ---

# Transform 1: For Kenneth's normal dialogue background (No xpos/ypos shifting)
transform focus_blur:
    blur 15
    matrixcolor BrightnessMatrix(-0.1)

# Transform 2: Specifically tuned for your spotlight mask alignment
transform spotlight_blur:
    blur 15
    matrixcolor BrightnessMatrix(-0.1)
    xpos 960
    ypos 532   

transform upper_body:
    zoom 0.75
    yalign -0.3
    xalign -0.1

# 3. Variables
default tutorial_files_analyzed = False
default tutorial_badge_picked = False
default tutorial_arthur_talked = False
default tutorial_door_checked = False

# 4. Compile all clear, unblurred elements into a single composite layer
image unblurred_tutorial_layer:
    contains:
        "bg tutorial_office"
    contains:
        Transform("gui/tutorial/files_idle.png", xpos=0, ypos= 0)
    contains:
        ConditionSwitch("tutorial_badge_picked == False", Transform("gui/tutorial/badge_idle.png", xpos=0, ypos= 0), "True", Null())
    contains:
        Transform("gui/tutorial/arthur_tuts_idle.png", xpos=0, ypos= 0)
    contains:
        Transform("gui/tutorial/door_idle.png", xpos=0, ypos= 0)
    contains:
        Transform("gui/tutorial/ui_icon_van_idle.png", xalign=0.95, yalign=0.05, zoom=0.1)

screen tutorial_spotlight(cx, cy, radius):
    # Use the newly created spotlight_blur transform here instead
    add "bg tutorial_office" at spotlight_blur align (0.5, 0.5)
    add AlphaMask("unblurred_tutorial_layer", CircleMask(cx, cy, radius)) align (0.5, 0.5)
    
# 6. Tutorial Flow
label tutorial_start:
    hide screen global_hud
    hide screen tutorial_office_environment
   
    scene bg tutorial_office at focus_blur
   
    show kenneth welcome_open at upper_body
    kenneth "Welcome to THE DAILY HERALD, rookie. Before I send you out, you need to know the ropes."
    
    show kenneth explaining at upper_body
    kenneth "Your job is to investigate scenes, find evidence, and write a compelling story."
    
    show kenneth thinking at upper_body
    kenneth "Look around the office. Practice analyzing files, picking up your badge, and talking to Arthur."
   
    # Hide Kenneth and clear the background blur so the normal office is ready
    hide kenneth
    scene bg tutorial_office
    
    # --- 1. STACK OF FILES ---
    show screen tutorial_spotlight(710, 688, 65)
    "Let's start by observing your surroundings."
    "It's a stack of glowing case files."
    "Good. Analyzing items gives you clues about the situation."
    hide screen tutorial_spotlight
    
    label .wait_for_files:
        call screen tutorial_office_environment
        if _return != "files":
            "I should observe the stack of case files first."
            jump .wait_for_files
    $ tutorial_files_analyzed = True
    
    # --- 2. PRESS BADGE ---
    show screen tutorial_spotlight(190, 955, 50)
    "Now, pick up your Press Badge on the table. You'll need it out there."
    "Items you pick up go into your bag. You can view them anytime."
    hide screen tutorial_spotlight
    
    label .wait_for_badge:
        call screen tutorial_office_environment
        if _return != "badge":
            "I need to pick up my Press Badge first."
            jump .wait_for_badge
            
    if "Press Badge" not in inventory_bag_items:
        $ inventory_bag_items.append("Press Badge")
        $ renpy.notify("You got the Press Badge.")
    $ tutorial_badge_picked = True
    
    # --- 3. ARTHUR ---
    show screen tutorial_spotlight(1556, 643, 200)
    "Talk to Arthur by clicking on him to get a witness testimony."
    arthur "I'm Arthur. We'll be working together. Always talk to witnesses to get their side of the story."
    hide screen tutorial_spotlight
    
    label .wait_for_arthur:
        call screen tutorial_office_environment
        if _return != "arthur":
            "I should click on Arthur."
            jump .wait_for_arthur
    $ tutorial_arthur_talked = True
    
    # --- 4. NEWS VAN ---
    show screen tutorial_spotlight(1780, 100, 60)
    "Once you have enough evidence, you can visit the News Van to write your story."
    "Let's practice submitting your first test article."
    "Click on the News Van icon in the top right to proceed."
    hide screen tutorial_spotlight
    
    label .wait_for_van:
        call screen tutorial_office_environment
        if _return != "van":
            "I should click the News Van icon to proceed."
            jump .wait_for_van
            
    jump tutorial_newspaper_minigame
    
label tutorial_newspaper_minigame:
    # Ensure the office screen is fully hidden before transitioning
    hide screen tutorial_office_environment
    scene bg newsroom
   
    "THE ROOKIE HERALD"
    "Headline: BREAKING NEWS: Fresh Talent Hits the Streets!"
    "A tenacious new rookie reporter has just joined the ranks of The Daily Herald's local news office. Eager to make a name for himself, he is prepared to hit the gritty streets, interview tough witnesses, and piece together the hard facts. Driven by a relentless pursuit of the truth, he will stop at nothing to uncover the real scoop and achieve the prestigious TRUE JOURNALISM award."
   
    # Apply the blur and darken effect to the newsroom background
    scene bg newsroom at focus_blur
    
    show kenneth welcome at upper_body
    kenneth "Looks like you're ready for the real news!"
    
    show kenneth explaining at upper_body
    kenneth "Go on out there rookie and give me the best local scoop."
   
    # Clean up the screen before starting Day 1
    hide kenneth
    scene bg newsroom
    
    show screen global_hud
    jump day1_path