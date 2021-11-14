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
def display_steast():
    dinner_data = fetch_food_dict_from_json_file("dining_jsons/steast_dinner.json")
    return render_template('index-steast-test.html', dinner_data=dinner_data)

@app.route('/iv')
def display_iv():
    dinner_data = fetch_food_dict_from_json_file("dining_jsons/iv_dinner.json")
    return render_template('index-iv-test.html', dinner_data=dinner_data)

@app.route('/stwest')
def display_iv():
    dinner_data = fetch_food_dict_from_json_file("dining_jsons/stwest_dinner.json")
    return render_template('index-stwest-test.html', dinner_data=dinner_data)


if __name__ == '__main__':  
   app.run(debug = True)  
