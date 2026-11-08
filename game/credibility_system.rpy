default total_credibility_score = 0

init python:
    def evaluate_credibility(clue, item, witness, target_clue, target_item, target_witness):
        score = (clue == target_clue) + (item == target_item) + (witness == target_witness)
        if score == 3:
            store.daily_rating = "True Journalism"
            store.total_credibility_score += 10
        elif score == 2:
            store.daily_rating = "Sensationalist"
            store.total_credibility_score += 5
        else:
            store.daily_rating = "Fake News"
            store.total_credibility_score -= 5
        return score

label calculate_day1_credibility:
    $ day1_score = evaluate_credibility(day1_clue, day1_item, day1_witness, "The Smashed Paint Can", "Missing blueprint", "Watchman 1")
    return

label calculate_day2_credibility:
    $ day2_score = evaluate_credibility(day2_clue, day2_item, day2_witness, "The Scorched Gas Can", "The Melted Camera", "Vendor 1")
    return

label calculate_day3_credibility:
    $ day3_score = evaluate_credibility(day3_clue, day3_item, day3_witness, "The Bullet-Riddled Wall", "The VIP Pass", "Dealer 1")
    return

label calculate_day5_credibility:
    $ day5_score = evaluate_credibility(day5_clue, day5_item, day5_witness, "The Bloody Tire Tracks", "The Train Ticket Stub", "Medic 1")
    return