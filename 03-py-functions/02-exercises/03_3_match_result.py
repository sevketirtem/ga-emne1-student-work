def show_match_result(home_team, away_team, home_score, away_score):
    print(f"{home_team}: {home_score} - {away_team}: {away_score}")

    if home_score == away_score:
        print("The match ended in a draw.")
    elif away_score > home_score:
        print(f"The {away_team} won.")
    else:
        print(f"The {home_team} won.")


show_match_result("Barcelona", "Galatasaray", 2,5)
show_match_result("Barcelona", "Galatasaray", 2,0)
show_match_result("Barcelona", "Galatasaray", 2,2)

