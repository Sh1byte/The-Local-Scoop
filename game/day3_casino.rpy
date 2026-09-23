# Day 3 Character Definitions
define dealer = Character("Dealer", color="#cccccc")
define cleaner = Character("Cleaner", color="#cccccc")
define waitress = Character("Waitress", color="#cccccc")
define drunk = Character("Drunk Patron", color="#cccccc")

# Day 3 Investigation Variables
default day3_clue = ""
default day3_item = ""
default day3_witness = ""
default evidence_ledger = False

label day3_start:
    # Day 3: The Midpoint
    scene bg newsroom
    
    "The town is living in total fear."
    vance "I've had enough of this! Both of you, drop the gang story entirely!"
    vance "Go cover the local bake sale. If I catch you digging into the warehouse or the market, you're fired."
    
    "I can't let this go. That same morning, I defy his orders and sneak out to an abandoned underground casino that was smashed up the night before."
    
    scene bg casino_basement
    
    "The basement is dark and messy. Suddenly, I hear footsteps. I shine my flashlight..."
    "It's Arthur!"
    arthur "You too, huh?"
    "Realizing that Editor Vance is hiding something and this story is too big for one person, Arthur's massive ego finally drops."
    arthur "Look, this is getting deadly. We need to split the work and watch each other's backs."
    "The rivalry dies right here in this dusty room. We are a team now."
    
    jump day3_investigation_hub

label day3_investigation_hub:
    menu:
        "Inspect the Bullet-Riddled Wall" if day3_clue == "":
            "Over fifty bullet holes scar the masonry."
            "This proves heavy firepower was used, not just baseball bats."
            $ day3_clue = "The Bullet-Riddled Wall"
            jump day3_investigation_hub
            
        "Inspect the Scattered Marked Cards" if day3_clue == "":
            "Decks of crooked playing cards littered everywhere."
            "It suggests the fight was just between cheating gamblers."
            $ day3_clue = "The Scattered Marked Cards"
            jump day3_investigation_hub
            
        "Inspect the Smashed Jukebox" if day3_clue == "":
            "Broken glass, vacuum tubes, and loose wiring."
            "It makes the scene look like a normal drunken bar brawl."
            $ day3_clue = "The Smashed Jukebox"
            jump day3_investigation_hub

        "Search the floor" if day3_item == "":
            "I find a silver casino card."
            "It's a VIP Pass. I can use this later to get past a bouncer at a local club and overhear a crucial conversation."
            $ day3_item = "The VIP Pass"
            jump day3_investigation_hub

        "Examine the debris" if day3_item == "":
            "There's a fake diamond earring on the floor."
            "This might lead me to incorrectly write a story about a jewel heist."
            $ day3_item = "The Diamond Earring"
            jump day3_investigation_hub

        "Check under the tables" if day3_item == "":
            "It's a stolen plastic credit card."
            "This will just distract me into writing a boring story about local identity theft."
            $ day3_item = "The Stolen Credit Card"
            jump day3_investigation_hub

        "Investigate the smashed wall safe" if not evidence_ledger:
            "Hidden inside the ruined safe is a torn page..."
            "It's a Bloody Ledger. It lists illegal weapon purchases made by both gangs."
            "This is the undeniable proof we need to link them together."
            # This triggers the final Notepad entry before the climax
            $ evidence_ledger = True 
            jump day3_investigation_hub

        "Interview the hiding Dealer" if day3_witness == "":
            dealer "The Iron Syndicate raided us because this place is secretly owned by The River Boys!"
            $ day3_witness = "Dealer 1"
            jump day3_investigation_hub

        "Interview the Cleaner" if day3_witness == "":
            cleaner "The police raided the place in secret and took all the money!"
            $ day3_witness = "Cleaner 1"
            jump day3_investigation_hub

        "Interview the shocked Waitress" if day3_witness == "":
            waitress "An angry ghost haunts the basement! It smashed the walls!"
            $ day3_witness = "Waitress 1"
            jump day3_investigation_hub

        "Interview the Drunk Patron" if day3_witness == "":
            drunk "A rival casino owner drove a literal bulldozer into the wall and drove away!"
            $ day3_witness = "Drunk Patron 1"
            jump day3_investigation_hub

        "Return to the Newsroom to write the article" if day3_clue != "" and day3_item != "" and day3_witness != "":
            jump day3_newspaper_minigame

label day3_newspaper_minigame:
    scene bg newsroom
    "Time to meet up with Arthur and compile the facts for Day 3."
    # Josh's Python script triggers here to query SheetDB using the 3 chosen variables
    "Chosen Clue: [day3_clue]"
    "Chosen Item: [day3_item]"
    "Chosen Witness: [day3_witness]"
    return