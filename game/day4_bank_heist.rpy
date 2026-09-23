# Day 4 Global Variables
default took_briefcase = False

label day4_start:
    # Day 4: The 3rd Plot Point
    scene bg main_street
    
    "The town breaks out into total chaos."
    "The Iron Syndicate attempts a massive mid-town bank robbery. However, just as they run out of the bank with the money, The River Boys ambush them in the street!"
    
    "I am watching from behind a parked car. Smoke fills the air, police sirens wail, and bullets fly."
    "During the fight, a heavy leather briefcase full of stolen bank cash slides across the pavement and hits my shoes."[cite: 13]
    "I am hidden by the smoke. I have only two choices."[cite: 13]

    menu:
        "Take it and run":
            $ took_briefcase = True
            "I grab the heavy briefcase of cash and sprint away down an alley, keeping the money for myself."[cite: 13]
            "Safe back at the office, I write my daily report."[cite: 13]
            jump day4_newspaper_path_a
            
        "Do nothing":
            $ took_briefcase = False
            "I freeze in shock."[cite: 13]
            "A moment later, the massive leader of the Iron Syndicate stomps through the smoke to grab the briefcase."[cite: 13]
            "His mask is torn from the fight. I look at his face and gasp—it is Editor Vance, my grumpy boss!"[cite: 13]
            "He has been controlling the newspaper to cover up his gang's crimes."[cite: 13]
            "Realizing a reporter has seen his true identity, Vance raises his gun and fires directly at me."[cite: 13]
            
            scene black
            
            "..."
            "The screen instantly cuts to black. The audience is left believing I have been killed."[cite: 13]
            jump day5_path_b_start

label day4_newspaper_path_a:
    scene bg newsroom
    "Time to publish the story. There are no clues to piece together today, just the raw truth of the violence."
    
    # Static output for Day 4 Path A
    "THE DAILY HERALD"
    "Headline: War on Main Street: Bank Heist Ends in Bloody Gang Ambush"[cite: 13]
    "Body: Main Street was turned into a war zone today as a brazen bank robbery by the Iron Syndicate was violently interrupted by their rivals, The River Boys. In the chaotic shootout that followed, the stolen bank funds vanished into the smoke. Law enforcement was powerless to stop the open street warfare. The missing money has pushed the tension between these two violent factions past the point of no return."[cite: 13]
    
    jump day5_path_a_start