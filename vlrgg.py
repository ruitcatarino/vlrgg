import requests
import argparse
import json

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--team", required = False, help = "Team Name")
ap.add_argument("-l", "--last", action='store_true', required = False, help = "Only get last game")
ap.add_argument("-u", "--upcoming", action='store_true', required = False, help = "Get upcoming matches")
args = vars(ap.parse_args())

team = args["team"] if args["team"] else ""
last = True if args["last"] else False
url = "https://vlrggapi.vercel.app/match/upcoming" if args["upcoming"] else "https://vlrggapi.vercel.app/match/results"

results = json.loads(requests.get(url).text)
results = results["data"]["segments"]
print("")

for game in results:
    if (team in game["team1"]) or (team in game["team2"]):
        print(f"{game['round_info'].lstrip()} in {game['tournament_name']}")
        print(f"{game['team1']} vs {game['team2']}")
        print(f"{game['time_until_match']}") if args["upcoming"] else print(f"{game['score1']} - {game['score2']}")
        print(f"More info: https://www.vlr.gg{game['match_page']}")
        print("")
        if last: break
