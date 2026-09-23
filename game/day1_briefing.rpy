# Character Definitions
define vance = Character("Editor Vance", color="#b30000")
define arthur = Character("Arthur", color="#ff9900")
define watchman = Character("Watchman", color="#cccccc")
define fisherman = Character("Fisherman", color="#cccccc")
define driver = Character("Delivery Driver", color="#cccccc")
define jogger = Character("Jogger", color="#cccccc")

# Day 1 Investigation Variables (To be sent to the SheetDB Matrix)
default day1_clue = ""
default day1_item = ""
default day1_witness = ""
default evidence_lighter = False

label stage1_briefing:
    # Day 1: The Hook and Inciting Event
    scene bg newsroom 
    
    vance "Listen up, rookie. I don't want you digging into the rising crime rate. That's an order."
    vance "Head down to the riverside shipping warehouse. Someone vandalized it. Get a simple quote and come back."
    
    scene bg warehouse
    
    "As I arrive at the scene, my rivalry with the star reporter is already flaring up."
    arthur "Well, look who finally showed up."
    arthur "Stay out of my way, rookie. Leave the front-page news to the professionals."
    
    "Arthur laughs at me, calls me clueless, and drives off to interview the mayor, leaving me alone in the morning light."
    
    jump day1_investigation_hub

label day1_investigation_hub:
    # Nick will eventually replace this text menu with clickable image maps for the UI
    menu:
        "Inspect the Smashed Paint Can" if day1_clue == "":
            "It smells like industrial-grade spray paint."
            "This shows it was a planned job, not a random act."
            $ day1_clue = "The Smashed Paint Can"
            jump day1_investigation_hub
            
        "Inspect the Broken Whiskey Bottle" if day1_clue == "":
            "Just a cheap bottle left by a homeless person."
            "It's meant to trick me into thinking it was a random drunk's doing."
            $ day1_clue = "The Broken Whiskey Bottle"
            jump day1_investigation_hub
            
        "Inspect the Torn Pizza Box" if day1_clue == "":
            "Empty food boxes scattered around."
            "This makes it look like teenagers were just hanging out here."
            $ day1_clue = "The Torn Pizza Box"
            jump day1_investigation_hub

        "Investigate the fence" if day1_item == "":
            "I see something hanging on a fence..."
            "It's a Janitor's Keyring."
            "I use this key to unlock a restricted office door inside the warehouse. Inside, I find a Vandalized Blueprint."
            $ day1_item = "The Janitor's Keyring"
            jump day1_investigation_hub

        "Investigate the puddle" if day1_item == "":
            "There's a Broken Pocket Watch in the water."
            "It looks expensive, but it has zero connection to the crime."
            $ day1_item = "The Broken Pocket Watch"
            jump day1_investigation_hub

        "Investigate the dirt" if day1_item == "":
            "A Lost Dog Collar lies in the dirt."
            "A dirty pet collar that wastes my time and will lead to a completely fake story."
            $ day1_item = "The Lost Dog Collar"
            jump day1_investigation_hub

        "Search the tall grass" if not evidence_lighter:
            "Wait, there is something heavy hidden in the grass..."
            "It's a Brass Lighter engraved with a skull and crossed wrenches."
            "I cannot use this for my daily article, but I will keep it as hard proof of the Iron Syndicate gang."
            # This triggers the Reporter's Notepad Inventory update
            $ evidence_lighter = True 
            jump day1_investigation_hub

        "Interview the nervous Watchman" if day1_witness == "":
            watchman "I saw them... men in heavy leather jackets marking the warehouse as their territory."
            $ day1_witness = "Watchman 1"
            jump day1_investigation_hub

        "Interview the Fisherman" if day1_witness == "":
            fisherman "I swear, the warehouse was attacked by angry teenagers!"
            $ day1_witness = "Fisherman 1"
            jump day1_investigation_hub

        "Interview the Delivery Driver" if day1_witness == "":
            driver "It was a rival shipping company trying to steal business. Simple as that."
            $ day1_witness = "Delivery Driver 1"
            jump day1_investigation_hub

        "Interview the sweaty Jogger" if day1_witness == "":
            jogger "I was running by in the middle of the night and saw a glowing ghost damage the walls!"
            $ day1_witness = "Jogger 1"
            jump day1_investigation_hub

        "Return to the Newsroom to write the article" if day1_clue != "" and day1_item != "" and day1_witness != "":
            jump day1_newspaper_minigame

label day1_newspaper_minigame:
    scene bg newsroom
    "Time to review my Reporter's Notepad and write the evening edition."
    # Josh's Python script will take over here to query SheetDB using the 3 chosen variables
    "Chosen Clue: [day1_clue]"
    "Chosen Item: [day1_item]"
    "Chosen Witness: [day1_witness]"
    return