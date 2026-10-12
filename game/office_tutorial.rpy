image bg tutorial_office = "gui/tutorial/bg_tutorial_office.png"

# Variables to track what the player has interacted with
default tutorial_files_analyzed = False
default tutorial_badge_picked = False
default tutorial_arthur_talked = False
default tutorial_door_checked = False

label tutorial_start:
    # Temporarily hide the main game HUD so it doesn't overlap the tutorial icons
    hide screen global_hud
    
    scene bg tutorial_office
    
    kenneth "Welcome to THE DAILY HERALD, rookie. Before I send you out, you need to know the ropes."
    kenneth "Your job is to investigate scenes, find evidence, and write a compelling story."
    kenneth "Look around the office. Practice analyzing files, picking up your badge, talking to Arthur, and checking the door."
    
    jump tutorial_investigation_hub

label tutorial_investigation_hub:
    call screen tutorial_office_environment
    $ clicked_object = _return
    
    # Keep the cutouts visible during dialogue
    show screen tutorial_office_environment
    
    if clicked_object == "files":
        "Let's start by observing your surroundings."
        "It's a stack of glowing case files."
        "Good. Analyzing items gives you clues about the situation."
        $ tutorial_files_analyzed = True
        
        hide screen tutorial_office_environment
        jump tutorial_investigation_hub
        
    elif clicked_object == "badge":
        "Now, pick up your Press Badge on the table. You'll need it out there."
        if "Press Badge" not in inventory_bag_items:
            $ inventory_bag_items.append("Press Badge")
            $ renpy.notify("You got the Press Badge.")
        "Items you pick up go into your bag. You can view them anytime."
        $ tutorial_badge_picked = True
        
        hide screen tutorial_office_environment
        jump tutorial_investigation_hub
        
    elif clicked_object == "arthur":
        "Talk to Arthur by clicking on him to get a witness testimony."
        arthur "I'm Arthur. We'll be working together. Always talk to witnesses to get their side of the story."
        $ tutorial_arthur_talked = True
        
        hide screen tutorial_office_environment
        jump tutorial_investigation_hub
        
    elif clicked_object == "door":
        "Click the door to practice moving to another room."
        "In a real case, this is how you navigate between different areas of the crime scene."
        $ tutorial_door_checked = True
        
        hide screen tutorial_office_environment
        jump tutorial_investigation_hub
        
    elif clicked_object == "van":
        # Check if the player finished all the other tutorial steps first
        if tutorial_files_analyzed and tutorial_badge_picked and tutorial_arthur_talked and tutorial_door_checked:
            hide screen tutorial_office_environment
            "Once you have enough evidence (a clue, an item, and a witness), you can visit the News Van to write your story."
            "Let's practice submitting your first test article."
            jump tutorial_newspaper_minigame
        else:
            "I should finish investigating the office first before checking the news van."
            "I still need to interact with the files, my badge, Arthur, and the door."
            
            hide screen tutorial_office_environment
            jump tutorial_investigation_hub
            
    else:
        hide screen tutorial_office_environment
        jump tutorial_investigation_hub

label tutorial_newspaper_minigame:
    scene bg newsroom
    
    "THE ROOKIE HERALD"
    "Headline: BREAKING NEWS: Fresh Talent Hits the Streets!"
    "A tenacious new rookie reporter has just joined the ranks of The Daily Herald's local news office. Eager to make a name for himself, he is prepared to hit the gritty streets, interview tough witnesses, and piece together the hard facts. Driven by a relentless pursuit of the truth, he will stop at nothing to uncover the real scoop and achieve the prestigious TRUE JOURNALISM award."
    
    kenneth "Looks like you're ready for the real news!"
    kenneth "Go on out there rookie and give me the best local scoop."
    
    # Turn the global HUD back on for the main game and seamlessly transition into Day 1
    show screen global_hud
    jump day1_path