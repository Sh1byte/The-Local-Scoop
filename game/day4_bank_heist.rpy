label day4_start:
    $ current_day = 4 # Hides the global HUD bag icon
    
    # SCENE 1: KENNETH'S OFFICE
    scene bg newsroom
    
    kenneth "I TOLD BOTH OF YOU TO DROP THE GANG STORY AND FOCUS ON SOMETHING ELSE. YET YOU DISRESPECTED MY ORDER AND SNUCK BEHIND MY BACK TO MAKE A REPORT ABOUT THE CASINO ISSUE!!"
    arthur "But boss, these events seem to be connected and part of something much bigger."
    "Yeah, and I even overheard a group of people at the bar saying that the man behind one of the gangs is someone powerful who can control the entire town."
    kenneth "I get it that you both want this big break, but meddling with something as dangerous as this could cost me my 2 greatest reporters."
    
    
    kenneth "I think both of you need to take a day off. I'll be confiscating your camera and take the day to do something other than putting yourselves in danger."
    
    scene black with fade
    
    # SCENE 2: THE BANK HEIST
    scene bg main_street with fade
    
    "(Since the boss laid me off, I think I'll treat myself to some alone time at the mall.)"
    "(But first I'll need to get some money from the bank.)"
    
    
    "Police" "STOP RIGHT THERE! AND SURRENDER, YOUR GANG HAS CAUSED THIS TOWN TOO MUCH DAMAGE!!"
    "Man in mask" "SHIT! THE COPS ARE HERE!"
    
    
    call screen day4_timer_choice
    $ choice = _return
    
    if choice == "take":
        # CHOICE 1: TOOK THE BRIEFCASE
        
        "(I AM IN BIG TROUBLE!!)"
        "(IT'S FINE, THEY DIDN'T SEE MY FACE, I'LL BE FINE)"
        "(I should stop somewhere to catch my breath.)"
                
        "HOLY SHIT, IT'S MONEY! A BRIEFCASE FULL OF MONEY!"
        "(Maybe they would think that the rival gang took the money and this would finally start a war between the two.)"
        "Looks like the problem will solve itself."

        $ renpy.force_autosave(True)

        jump day5_path_a_start
        
    elif choice == "leave":
        # CHOICE 2: DID NOT TAKE THE BRIEFCASE
        
        "(HOLY COW, I THOUGHT I WAS A GONNER!)"
        "(“TAKE A BREAK,” HE SAID!)"
        "(“DO SOMETHING OTHER THAN PUTTING YOURSELVES IN DANGER,” HE SAID!)"
        
        
        "I think I'm safe here."
        "Well, I guess mall time is cancelled. I should go home and rest."

        $ renpy.force_autosave(True)
        
        jump day5_path_a_start
        
    elif choice == "timeout":
        # CHOICE 3: TIMER RAN OUT (CAUGHT BY KENNETH)
        
        "(I wonder what could be insi—)"
        "Man in mask" "HEY YOU! GET AWAY FROM THERE!"
        
        
        "I'm sorry, I wasn't gonna do anything, please don't shoot me!"
        "Man in mask" "I TOLD YOU TO GET AWAY, NOT RAISE YOUR HANDS AND BEG!"
        
        
        "Right, right. I'm sorry."
        
        
        "BOSS?!"
        "Man in mask" "Why did you have to notice, kid?"
        "So all this time you weren't keeping us away from the gang stories to protect us? You were keeping us away to protect you!"
        "Man in mask" "Eyy, he's all caught up."
        "I get it now. You're the man powerful enough to control the entire town—the boss of the local newspaper company. Powerful enough to control the town's feelings."
        "Man in mask" "You don't have to analyze the situation anymore, because you won't get the chance to write a report about this."
        
        scene black

        $ renpy.force_autosave(True)

        jump day5_path_b_start

screen day4_timer_choice():
    # 5-second red timer overlay
    timer 5.0 action Return("timeout")
    
    vbox:
        align (0.5, 0.8)
        spacing 20
        textbutton "GET THE BRIEFCASE AND RUN" action Return("take") text_size 35 text_color "#FF0000" text_outlines [(2, "#000000", 0, 0)]
        textbutton "DON'T TAKE THE BRIEFCASE, RUN" action Return("leave") text_size 35 text_color "#FF0000" text_outlines [(2, "#000000", 0, 0)]