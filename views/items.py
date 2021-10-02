import json
from flask import Blueprint, render_template, request
from models.item import Item

items_blueprint = Blueprint('items', __name__)


@items_blueprint.route('/')
def index():
    items = Item.all()
    return render_template('items/index.html', items=items)


@items_blueprint.route("/new", methods=['GET', 'POST'])
def new_item():
    if request.method == 'POST':
        url = request.form['url']
        tag_name = request.form['tag_name']
        query = json.loads(request.form['query'])
        item = Item(url, tag_name, query)
        item.save_to_database()
    return render_template('items/new_item.html')
