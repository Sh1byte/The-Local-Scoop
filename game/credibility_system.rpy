default total_credibility_score = 0

# ----------------------------------------
# Day 1 Credibility Calculator
# ----------------------------------------
label calculate_day1_credibility:
    $ day1_score = 0
    
    if day1_clue == "The Smashed Paint Can":
        $ day1_score += 1
    if day1_item == "Missing blueprint":
        $ day1_score += 1
    if day1_witness == "Watchman 1":
        $ day1_score += 1

    if day1_score == 3:
        $ daily_rating = "True Journalism"
        $ total_credibility_score += 10
    elif day1_score == 2:
        $ daily_rating = "Sensationalist"
        $ total_credibility_score += 5
    else:
        $ daily_rating = "Fake News"
        $ total_credibility_score -= 5
        
    return

# ----------------------------------------
# Day 2 Credibility Calculator
# ----------------------------------------
label calculate_day2_credibility:
    $ day2_score = 0
    
    if day2_clue == "The Scorched Gas Can":
        $ day2_score += 1
    if day2_item == "The Melted Camera":
        $ day2_score += 1
    if day2_witness == "Vendor 1":
        $ day2_score += 1

    if day2_score == 3:
        $ daily_rating = "True Journalism"
        $ total_credibility_score += 10
    elif day2_score == 2:
        $ daily_rating = "Sensationalist"
        $ total_credibility_score += 5
    else:
        $ daily_rating = "Fake News"
        $ total_credibility_score -= 5
        
    return

# ----------------------------------------
# Day 3 Credibility Calculator
# ----------------------------------------
label calculate_day3_credibility:
    $ day3_score = 0
    
    if day3_clue == "The Bullet-Riddled Wall":
        $ day3_score += 1
    if day3_item == "The VIP Pass":
        $ day3_score += 1
    if day3_witness == "Dealer 1":
        $ day3_score += 1

    if day3_score == 3:
        $ daily_rating = "True Journalism"
        $ total_credibility_score += 10
    elif day3_score == 2:
        $ daily_rating = "Sensationalist"
        $ total_credibility_score += 5
    else:
        $ daily_rating = "Fake News"
        $ total_credibility_score -= 5
        
    return

# ----------------------------------------
# Day 5 (Path A) Credibility Calculator
# ----------------------------------------
label calculate_day5_credibility:
    $ day5_score = 0
    
    if day5_clue == "The Bloody Tire Tracks":
        $ day5_score += 1
    if day5_item == "The Train Ticket Stub":
        $ day5_score += 1
    if day5_witness == "Medic 1":
        $ day5_score += 1

    if day5_score == 3:
        $ daily_rating = "True Journalism"
        $ total_credibility_score += 10
    elif day5_score == 2:
        $ daily_rating = "Sensationalist"
        $ total_credibility_score += 5
    else:
        $ daily_rating = "Fake News"
        $ total_credibility_score -= 5
        
    return