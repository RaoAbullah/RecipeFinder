from flask import Flask, render_template, request
import requests

app = Flask("RecipeFinder")

API_KEY = 'de88fbbbb94d4b6487e863aa57597086'

def get_recipes(ingredients):
    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number=5&apiKey={API_KEY}"
    response = requests.get(url)
    return response.json()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest', methods=['POST'])
def suggest():
    ingredients = request.form.get('ingredients')
    recipes = get_recipes(ingredients)
    return render_template('results.html', recipes=recipes)

if "RecipeFinder" == '_main_':
    app.run(debug=True)