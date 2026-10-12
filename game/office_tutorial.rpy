label tutorial_start:
    scene bg tutorial_office
    
    kenneth "Welcome to THE DAILY HERALD, rookie. Before I send you out, you need to know the ropes."
    kenneth "Your job is to investigate scenes, find evidence, and write a compelling story."

    # Analyze
    "Let's start by observing your surroundings. Click on the glowing files on the desk."
    call screen tutorial_analyze
    "Good. Analyzing items gives you clues about the situation."

    # Pick Up
    "Now, pick up your Press Badge on the table. You'll need it out there."
    call screen tutorial_pickup
    $ inventory_bag_items.append("Press Badge")
    "Items you pick up go into your bag. You can view them anytime."

    # Interview
    "Talk to Arthur by clicking on him to get a witness testimony."
    call screen tutorial_interview
    arthur "I'm Arthur. We'll be working together. Always talk to witnesses to get their side of the story."

    # Navigation
    "Click the door to practice moving to another room."
    call screen tutorial_door

    # Create Story
    scene bg tutorial_office
    "Once you have enough evidence (a clue, an item, and a witness), you can visit the News Van to write your story."
    "Click the Van Icon at the top right to check your evidence."
    call screen tutorial_van_icon
    
    kenneth "That's everything. Now get out there and find me a front-page scoop!"
    return

screen tutorial_analyze():
    imagebutton xpos 450 ypos 500 idle "gui/tutorial/files_idle.png" action Return("files")

screen tutorial_pickup():
    imagebutton xpos 800 ypos 600 idle "gui/tutorial/badge_idle.png" action Return("badge")

screen tutorial_interview():
    imagebutton xpos 300 ypos 300 idle "gui/tutorial/arthur_idle.png" action Return("arthur")

screen tutorial_door():
    imagebutton xpos 1200 ypos 200 idle "gui/tutorial/door_idle.png" action Return("door")

screen tutorial_van_icon():
    imagebutton xalign 0.95 yalign 0.05 idle "gui/tutorial/ui_icon_van_idle.png" action Return("van")