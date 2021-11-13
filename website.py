from flask import Flask, render_template
import json

app = Flask(__name__)

# gets the python representation of a JSON file's data
def fetch_food_dict_from_json_file(filename):
    f = open(filename, "r")
    contents = f.read()
    f.close()
    data = json.loads(contents)
    return data

@app.route('/')
def hello():
    dinner_data = fetch_food_dict_from_json_file("dining_jsons/dinner.json")
    food_by_station = dinner_data["Stetson East"] # change
    return render_template('index-steast.html', food_by_station=food_by_station)
