from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def hello():
    f = open("./food.json", "r")
    contents = f.read()
    f.close()
    food_data = json.loads(contents)
    stwest_food_list = food_data["Food Hall at Stetson West"]
    return render_template('index.html', stwest_food_list=stwest_food_list)

