label day4_start:
    $ current_day = 4 # Hides the global HUD bag icon
    
    # SCENE 1: KENNETH'S OFFICE
    scene bg newsroom
    #Scene 1.1 showing kenneth's office with kenneth sitting behind his desk and arthur and the player standing in front of him getting yelled at
    #Scene 1.2 showing the desk of kenneth and him slamming his hands on it
    #Scene 1.3 showing kenneth yelling at the player and arthur
    kenneth "I TOLD BOTH OF YOU TO DROP THE GANG STORY AND FOCUS ON SOMETHING ELSE. YET YOU DISRESPECTED MY ORDER AND SNUCK BEHIND MY BACK TO MAKE A REPORT ABOUT THE CASINO ISSUE!!"
    #Scene 1.4 showing arthur reasoning with kenneth
    arthur "But boss, these events seem to be connected and part of something much bigger."
    #Scene 1.5 showing arthur and the player side by side trying to reason with kenneth
    "Yeah, and I even overheard a group of people at the bar saying that the man behind one of the gangs is someone powerful who can control the entire town."
    #Scene 1.6 showing kenneth talking to both with open arms
    kenneth "I get it that you both want this big break, but meddling with something as dangerous as this could cost me my 2 greatest reporters."
    #Scene 1.7 showing arthur and the player looking at each other
    #Scene 1.8 showing kenneth reaching out his arm to take away their camera
    kenneth "I think both of you need to take a day off. I'll be confiscating your camera and take the day to do something other than putting yourselves in danger."
    #Scene 1.9 showing kenneth's desk with 2 cameras on it 

    scene black with fade
    
    # SCENE 2: THE BANK HEIST
    scene bg main_street with fade
    
    #Scene 2.1 showing the bank far away
    #Scene 2.2 showing the front of the bank closer
    "(Since the boss laid me off, I think I'll treat myself to some alone time at the mall.)"
    "(But first I'll need to get some money from the bank.)"
    #Scene 2.3 showing the inside of the bank nothing special
    #Scene 2.4 showing a sudden explosion of the front door of the bank
    #Scene 2.5 showing multiple masked men entering the bank
    #Scene 2.6 showing masked men taking money from the banks vault
    #Scene 2.7 showing police entering the building
    #Scene 2.8 showing the masked men attempting to exit the building
    #Scene 2.9 showing the masked men get blocked by the police
    #Scene 2.10 showing the masked men getting into a shootout with the police
    #Scene 2.11 showing the pov of the player in the alley on the front of the bank shootout
    #Scene 2.12 showing one masked man running away from the bank while getting shot at by the police
    #Scene 2.13 showing the masked man firing back at the police
    #Scene 2.14 showing the wide shot aerial view of the bank shootout
    #Scene 2.15 showing the police shooting at the maske man while saying his dialogue
    "Police" "STOP RIGHT THERE! AND SURRENDER, YOUR GANG HAS CAUSED THIS TOWN TOO MUCH DAMAGE!!"
    #Scene 2.16 showing the masked man getting into the getaway vehicle
    "Man in mask" "SHIT! THE COPS ARE HERE!"
    #Scene 2.17 showing the car driving away from the bank
    #Scene 2.18 showing the tire of the car get shot by the police and burst and skids on the road
    #Scene 2.19 showing the car tuppleing over now upside down
    #Scene 2.20 showing the briefcase fly out of the car
    #Scene 2.21 showing the briefcase land close to the player
    #Scene 2.22 showing the player pov while looking down to the briefcase contemplating if he should take it or not

    
    
    call screen day4_timer_choice
    $ choice = _return
    
    if choice == "take":
        # CHOICE 1: TOOK THE BRIEFCASE
        #Scene C1.1 showing the player picking up the briefcase
        #Scene C1.2 showing the player running away from the bank with the briefcase
        "(I AM IN BIG TROUBLE!!)"
        "(IT'S FINE, THEY DIDN'T SEE MY FACE, I'LL BE FINE)"
        #Scene C1.3 showing the player slowing down to catch his breath
        "(I should stop somewhere to catch my breath.)"
        #Scene C1.4 showing player in an alley trying to open the briefcase
        #Scene C1.5 showing the player opening the briefcase and seeing money inside
        "HOLY SHIT, IT'S MONEY! A BRIEFCASE FULL OF MONEY!"
        "(Maybe they would think that the rival gang took the money and this would finally start a war between the two.)"
        #Scene C1.6 showing the player clutching the briefcase with a grin on his face
        "Looks like the problem will solve itself."

        $ renpy.force_autosave(True)

        jump day5_path_a_start
        
    elif choice == "leave":
        # CHOICE 2: DID NOT TAKE THE BRIEFCASE
        
        #Scene C2.1 showing the foot of the player facing away from the briefcase
        #Scene C2.2 showing the player running away from the bank
        #Scene C2.3 showing the player running much further away from the bank
        "(HOLY COW, I THOUGHT I WAS A GONNER!)"  
        #Scene C2.4 showing the player going into a park to catch his breath
        "I think I'm safe here."
        #Scene C2.5 showing the player sitting on a bench in the park
        "Well, I guess mall time is cancelled. I should go home and rest."

        $ renpy.force_autosave(True)
        
        jump day5_path_a_start
        
    elif choice == "timeout":
        # CHOICE 3: TIMER RAN OUT (CAUGHT BY KENNETH)
        #Scene C3.1 using Scene C1.1.jpg showing the player picking up the briefcase
        "(I wonder what could be insi—)"
        #Scene C3.2 showing Kenneth shouting at the player while limping towards him
        "Man in mask" "HEY YOU! GET AWAY FROM THERE!"
        
        #Scene C3.3 showing the player raising his hands in surrender while kenneth points a gun at him
        "I'm sorry, I wasn't gonna do anything, please don't shoot me!"
        #Scene C3.4 showing Kenneth pointing a gun at the player his face more visible now
        "Man in mask" "I TOLD YOU TO GET AWAY, NOT RAISE YOUR HANDS AND BEG!"
        
        
        "Right, right. I'm sorry."
        
        #Scene C3.5 showing the player realizing he knows this robber
        "BOSS?!"
        "Man in mask" "Why did you have to notice, kid?"
        "So all this time you weren't keeping us away from the gang stories to protect us? You were keeping us away to protect you!"
        "Man in mask" "Eyy, he's all caught up."
        "I get it now. You're the man powerful enough to control the entire town—the boss of the local newspaper company. Powerful enough to control the town's feelings."
        #Scene C3.6 Close up view of Kenneth's gun pointing at the player
        "Man in mask" "You don't have to analyze the situation anymore, because you won't get the chance to write a report about this."
        #Scene C3.7 Close up view of Kenneth's gun firing at the player
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