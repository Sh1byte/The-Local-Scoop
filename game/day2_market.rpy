# Day 2 Character Definitions
define vendor = Character("Vendor", color="#cccccc")
define shopper = Character("Shopper", color="#cccccc")
define baker = Character("Baker", color="#cccccc")
define musician = Character("Street Musician", color="#cccccc")

# Day 2 Investigation Variables
default day2_clue = ""
default day2_item = ""
default day2_witness = ""
default evidence_letter = False

label day2_start:
    # Day 2: The 1st Plot Point
    scene bg newsroom
    
    "The tension is stepping up."
    vance "Market plaza. Fruit stand burned to the ground in broad daylight. Go."
    
    scene bg market_plaza
    
    "I arrive at the smoking ruins of the market. Arthur is already here."
    "He bumps my shoulder intentionally, blocking my camera lens."
    arthur "Go back to the office, rookie. Leave the front-page news to the professionals."
    "I have to work around him to find the truth."
    
    jump day2_investigation_hub

label day2_investigation_hub:
    menu:
        "Inspect the Scorched Gas Can" if day2_clue == "":
            "It reeks of accelerant."
            "This proves the fire was started on purpose with gasoline."
            $ day2_clue = "The Scorched Gas Can"
            jump day2_investigation_hub
            
        "Inspect the Melted Toy Car" if day2_clue == "":
            "Sad collateral damage."
            "It makes me wonder if a child was playing with matches."
            $ day2_clue = "The Melted Toy Car"
            jump day2_investigation_hub
            
        "Inspect the Spilled Cooking Oil" if day2_clue == "":
            "A greasy puddle near a stove."
            "This could easily trick someone into thinking it was a simple kitchen accident."
            $ day2_clue = "The Spilled Cooking Oil"
            jump day2_investigation_hub

        "Search the rubble" if day2_item == "":
            "I spot a damaged security camera in the debris."
            "Taking this to the town electronics shop gives me a blurry photo of the fire starting."
            $ day2_item = "The Melted Camera"
            jump day2_investigation_hub

        "Check near the puddle" if day2_item == "":
            "A half-smoked, imported cigar was dropped nearby."
            "This might trick people into thinking a wealthy politician ordered the fire."
            $ day2_item = "The Expensive Cigar"
            jump day2_investigation_hub

        "Look at the scattered papers" if day2_item == "":
            "It's a winning scratch ticket."
            "This could mislead me into writing a story about a lucky vendor getting robbed."
            $ day2_item = "The Dropped Lottery Ticket"
            jump day2_investigation_hub

        "Check under the burned cash register" if not evidence_letter:
            "There's a piece of paper tucked away here..."
            "It's an extortion letter demanding weekly payments, signed with the blue anchor stamp of The River Boys gang."
            "I must keep this secret for now, but it's vital proof for later."
            # This triggers the Reporter's Notepad Inventory update
            $ evidence_letter = True 
            jump day2_investigation_hub

        "Interview the crying Vendor" if day2_witness == "":
            vendor "I stopped paying protection money to The River Boys... and they burned my shop in revenge!"
            $ day2_witness = "Vendor 1"
            jump day2_investigation_hub

        "Interview the loud Shopper" if day2_witness == "":
            shopper "She caused the fire herself to get the insurance money! I know it!"
            $ day2_witness = "Shopper 1"
            jump day2_investigation_hub

        "Interview the Baker" if day2_witness == "":
            baker "It was a targeted hit by the secret society of rival bakers! They're ruthless!"
            $ day2_witness = "Baker 1"
            jump day2_investigation_hub

        "Interview the Street Musician" if day2_witness == "":
            musician "I saw it with my own eyes! A freak lightning strike from a perfectly clear sky!"
            $ day2_witness = "Street Musician 1"
            jump day2_investigation_hub

        "Return to the Newsroom to write the article" if day2_clue != "" and day2_item != "" and day2_witness != "":
            jump day2_newspaper_minigame

label day2_newspaper_minigame:
    scene bg newsroom
    "Time to compile the facts for Day 2."
    # Josh's Python script triggers here to query SheetDB using the 3 chosen variables
    "Chosen Clue: [day2_clue]"
    "Chosen Item: [day2_item]"
    "Chosen Witness: [day2_witness]"
    return