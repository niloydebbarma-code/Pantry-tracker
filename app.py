from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

# In-memory pantry storage
pantry = []

@app.route('/')
def index():
    return render_template('index.html', items=pantry)

@app.route('/add_item', methods=['POST'])
def add_item():
    item = request.form.get('item')
    category = request.form.get('category')
    expiration_date = request.form.get('expiration_date')
    if item:
        pantry.append({
            'item': item,
            'category': category,
            'expiration_date': expiration_date
        })
    return jsonify(pantry)

@app.route('/remove_item', methods=['POST'])
def remove_item():
    item_name = request.form.get('item')
    pantry[:] = [item for item in pantry if item['item'] != item_name]
    return jsonify(pantry)

@app.route('/edit_item', methods=['POST'])
def edit_item():
    old_name = request.form.get('old_name')
    new_item = request.form.get('item')
    new_category = request.form.get('category')
    new_expiration_date = request.form.get('expiration_date')

    for item in pantry:
        if item['item'] == old_name:
            item['item'] = new_item
            item['category'] = new_category
            item['expiration_date'] = new_expiration_date
            break

    return jsonify(pantry)

@app.route('/get_items', methods=['GET'])
def get_items():
    return jsonify(pantry)

@app.route('/search_items', methods=['GET'])
def search_items():
    query = request.args.get('query')
    filtered_items = [item for item in pantry if query.lower() in item['item'].lower()]
    return jsonify(filtered_items)

if __name__ == '__main__':
    app.run(debug=True)