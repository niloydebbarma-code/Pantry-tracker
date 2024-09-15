from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory pantry storage
pantry = []

@app.route('/')
def index():
    return render_template('index.html', items=pantry)

@app.route('/add_item', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        pantry.append(item)
    return jsonify(pantry)

@app.route('/remove_item', methods=['POST'])
def remove_item():
    item = request.form.get('item')
    if item in pantry:
        pantry.remove(item)
    return jsonify(pantry)

@app.route('/get_items', methods=['GET'])
def get_items():
    return jsonify(pantry)

if __name__ == '__main__':
    app.run(debug=True)
