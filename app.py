from flask import Flask, render_template, jsonify
import fastf1
import json

app = Flask(__name__)
fastf1.Cache.enable_cache('cache')

DRIVER_DATA = [
    {"abbr": "VER", "name": "Max Verstappen", "team": "Red Bull", "num": 1, "points": 75, "wins": 3, "podiums": 3},
    {"abbr": "LEC", "name": "Charles Leclerc", "team": "Ferrari", "num": 16, "points": 51, "wins": 0, "podiums": 3},
    {"abbr": "HAM", "name": "Lewis Hamilton", "team": "Mercedes", "num": 44, "points": 45, "wins": 0, "podiums": 2},
    {"abbr": "NOR", "name": "Lando Norris", "team": "McLaren", "num": 4, "points": 39, "wins": 0, "podiums": 1},
    {"abbr": "RUS", "name": "George Russell", "team": "Mercedes", "num": 63, "points": 30, "wins": 0, "podiums": 0},
]

RACE_RESULTS = [
    {"name": "Bahrain GP", "round": "01", "date": "Mar 2", "flag": "🇧🇭", "podium": ["VER","LEC","HAM"]},
    {"name": "Saudi Arabia GP", "round": "02", "date": "Mar 9", "flag": "🇸🇦", "podium": ["VER","NOR","LEC"]},
    {"name": "Australian GP", "round": "03", "date": "Mar 16", "flag": "🇦🇺", "podium": ["VER","HAM","LEC"]},
]

CALENDAR = [
    {"round": "01", "name": "Bahrain GP", "circuit": "Bahrain International Circuit", "date": "Mar 2, 2026", "flag": "🇧🇭", "status": "done"},
    {"round": "02", "name": "Saudi Arabia GP", "circuit": "Jeddah Corniche Circuit", "date": "Mar 9, 2026", "flag": "🇸🇦", "status": "done"},
    {"round": "03", "name": "Australian GP", "circuit": "Albert Park Circuit", "date": "Mar 16, 2026", "flag": "🇦🇺", "status": "done"},
    {"round": "04", "name": "Japanese GP", "circuit": "Suzuka Circuit", "date": "Apr 6, 2026", "flag": "🇯🇵", "status": "next"},
    {"round": "05", "name": "Chinese GP", "circuit": "Shanghai International Circuit", "date": "Apr 20, 2026", "flag": "🇨🇳", "status": "upcoming"},
    {"round": "06", "name": "Miami GP", "circuit": "Miami International Autodrome", "date": "May 4, 2026", "flag": "🇺🇸", "status": "upcoming"},
    {"round": "07", "name": "Emilia Romagna GP", "circuit": "Autodromo Enzo e Dino Ferrari", "date": "May 18, 2026", "flag": "🇮🇹", "status": "upcoming"},
    {"round": "08", "name": "Monaco GP", "circuit": "Circuit de Monaco", "date": "May 25, 2026", "flag": "🇲🇨", "status": "upcoming"},
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        driver_data=json.dumps(DRIVER_DATA),
        race_results=json.dumps(RACE_RESULTS),
        calendar=json.dumps(CALENDAR),
    )

@app.route("/api/standings")
def api_standings():
    return jsonify(DRIVER_DATA)

@app.route("/api/results")
def api_results():
    return jsonify(RACE_RESULTS)

@app.route("/api/calendar")
def api_calendar():
    return jsonify(CALENDAR)

if __name__ == "__main__":
    app.run(debug=True)
