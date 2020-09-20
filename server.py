from flask import Flask, render_template
import pyjokes
app = Flask(__name__)

@app.route('/lang-<lang>')
def get_lang_joke(lang=None):
    try:
        joke = pyjokes.get_joke(str(lang))
        return render_template('index.html', joke=joke)
    except pyjokes.pyjokes.LanguageNotFoundError:
        return "Oops! Language Not Found. Try again"

@app.route('/category-<category>')
def get_category_joke(category=None):
    try:
        joke = pyjokes.get_joke(category=str(category))
        return render_template('index.html', joke=joke)
    except pyjokes.pyjokes.CategoryNotFoundError:
        return "Oops! Category Not Found. Try again"

@app.route('/')
def get_joke_de():
    return render_template('about.html')
