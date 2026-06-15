# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month:str) :
    month = month.lower()
    season_dict = {
        "december":"Winter",
        "january":"Winter",
        "february":"Winter",
        "march":"Spring",
        "april":"Spring",
        "may":"Spring",
        "june":"Summer",
        "july":"Summer",
        "august":"Summer",
        "september":"Autumn",
        "october":"Autumn",
        "november":"Autumn"
    }
    return season_dict.get(month, "Invalid month")

print(check_season("January"))
print(check_season("Hello"))

