# Day 5 Character Definitions
define medic = Character("Medic", color="#cccccc")
define engineer = Character("Train Engineer", color="#cccccc")
define hobo = Character("Hobo", color="#cccccc")
define tourist = Character("Tourist", color="#cccccc")

# Day 5 Investigation Variables (Path A Only)
default day5_clue = ""
default day5_item = ""
default day5_witness = ""
default evidence_phone = False

label day5_path_a_start:
    # Path A: The Rising Action and Climax (If you chose "Take it and run")
    scene bg rail_depot
    
    "The morning of the 5th day arrives. Because the money is missing, both gangs blame each other."
    "I am dispatched to investigate a morning lead at an old rail depot where a getaway driver was found injured."
    "Arthur meets me there in the morning sun, completely unaware that I stole the cash."
    
    jump day5_investigation_hub

label day5_investigation_hub:
    menu:
        "Inspect the Bloody Tire Tracks" if day5_clue == "":
            "They show the exact escape route of the ambushed gangsters."
            $ day5_clue = "The Bloody Tire Tracks"
            jump day5_investigation_hub
            
        "Inspect the Wild Dog Tracks" if day5_clue == "":
            "Just stray animals drawn to the blood."
            $ day5_clue = "The Wild Dog Tracks"
            jump day5_investigation_hub
            
        "Inspect the Leaking Oil Puddle" if day5_clue == "":
            "Looks like normal car trouble, hiding the fact there was a violent shootout here."[cite: 13]
            $ day5_clue = "The Leaking Oil Puddle"
            jump day5_investigation_hub

        "Check the driver's pockets" if day5_item == "":
            "I found a Train Ticket Stub."[cite: 13]
            "It proves the gangs were planning to leave town."[cite: 13]
            $ day5_item = "The Train Ticket Stub"
            jump day5_investigation_hub

        "Check the discarded trash" if day5_item == "":
            "Just an Empty Wallet. A pickpocket's discarded trash that distracts from the big picture."[cite: 13]
            $ day5_item = "The Empty Wallet"
            jump day5_investigation_hub

        "Look inside the Rusty Toolbox" if day5_item == "":
            "Heavy junk left behind by a mechanic. It adds nothing to my story."[cite: 13]
            $ day5_item = "The Rusty Toolbox"
            jump day5_investigation_hub

        "Search near the medical supplies" if not evidence_phone:
            "Someone dropped a cheap Burner Phone."[cite: 13]
            "A text message on the screen confirms a massive gang war at the shipping docks at midnight."[cite: 13]
            "I need to add this to my Reporter's Notepad."
            $ evidence_phone = True 
            jump day5_investigation_hub

        "Interview the Medic" if day5_witness == "":
            medic "They forced me to treat a wounded gangster! He kept muttering about a midnight war at the docks!"[cite: 13]
            $ day5_witness = "Medic 1"
            jump day5_investigation_hub

        "Interview the Train Engineer" if day5_witness == "":
            engineer "That driver just fell off a moving cargo train, plain and simple."[cite: 13]
            $ day5_witness = "Train Engineer 1"
            jump day5_investigation_hub

        "Interview the Hobo" if day5_witness == "":
            hobo "The government is poisoning the water supply! That's what happened here!"[cite: 13]
            $ day5_witness = "Hobo 1"
            jump day5_investigation_hub

        "Interview the Tourist" if day5_witness == "":
            tourist "Oh, I thought they were just filming a zombie action movie here with fake blood."[cite: 13]
            $ day5_witness = "Tourist 1"
            jump day5_investigation_hub

        "Return to the Newsroom" if day5_clue != "" and day5_item != "" and day5_witness != "" and evidence_phone:
            jump day5_morning_newspaper

label day5_morning_newspaper:
    scene bg newsroom
    "I compile the facts and prep the morning edition."
    # Josh's Python script triggers here to query SheetDB for the Day 5 morning paper
    "Chosen Clue: [day5_clue]"
    "Chosen Item: [day5_item]"
    "Chosen Witness: [day5_witness]"
    
    "That evening, I approach my former rival in the newsroom."[cite: 13]
    "I look Arthur in the eye and say, 'I’ve got a big lead, Arthur. A massive gang clash at the shipping docks tonight. I need you to come with me to help gather information.'"[cite: 13]
    "Arthur nods, trusting me completely."[cite: 13]
    
    jump day5_path_a_climax

label day5_path_a_climax:
    scene bg docks_midnight
    "We hide on a hill overlooking the docks. The two gangs arrive, heavily armed."[cite: 13]
    "I face my final choice."[cite: 13]
    
    menu:
        "Tell Arthur to sneak down closer for a picture":
            "Arthur trusts me and moves in. The shooting starts, and Arthur is killed in the crossfire."[cite: 13]
            "I walk away with the stolen bank money and publish the final story alone, becoming rich but completely corrupt."[cite: 13]
            
            # Ending 1
            "THE DAILY HERALD"
            "Headline: Tragedy at the Docks: Syndicate War Claims the Life of Local Reporter"[cite: 13]
            "Ending 1: The Dark Path Unlocked."[cite: 13]
            return
            
        "Grab Arthur’s arm and stop him":
            "I tell him it is too dangerous. We both stay hidden and survive."[cite: 13]
            "The next day, I publish a co-authored story exposing the gangs, cementing a lifelong friendship with my former rival."[cite: 13]
            
            # Ending 2
            "THE DAILY HERALD"
            "Headline: The Midnight Bust: River Boys and Iron Syndicate Exposed in Dockyard Showdown"[cite: 13]
            "Ending 2: The Redemption Path Unlocked."[cite: 13]
            return

label day5_path_b_start:
    # Path B: The Master Investigator (If you chose "Do nothing")
    scene bg police_station
    with fade
    
    "The screen slowly fades up from black. It is the night of the 5th day. I am sitting in the police station, breathing heavily."[cite: 13]
    "A flashback reveals what really happened yesterday: Arthur had been watching my back during the bank robbery."[cite: 13]
    "Just as Editor Vance pulled the trigger, Arthur tackled Vance to the ground, saving my life!"[cite: 13]
    "The fight stalled Vance just long enough for the police sirens to arrive. Panicked, Vance had to flee the scene, leaving the briefcase of money behind."[cite: 13]
    
    if evidence_lighter and evidence_letter and evidence_ledger:
        "Because Arthur saved me and fought the gang leader, our rivalry turns into absolute brotherhood."[cite: 13]
        "Together, we realize we have everything we need: The Brass Lighter, The Extortion Letter, The Bloody Ledger, and the ultimate twist—the true identity of Editor Vance."[cite: 13]
        "We dump all this irrefutable evidence on the Police Chief's desk."[cite: 13]
        
        scene bg docks_midnight
        "At midnight, as Editor Vance and the two gangs prepare to fight at the docks, dozens of police cars surround them."[cite: 13]
        "Both gangs are arrested before a single punch is thrown. Arthur and I write the biggest story in the state, safely putting an end to the chaos forever."[cite: 13]
        
        # Ending 3
        "Ending 3: The Clean Sweep Unlocked."[cite: 13]
        return
    else:
        "We survived, but I didn't gather enough hard evidence to take down Editor Vance and the gangs for good."
        "The war continues..."
        return