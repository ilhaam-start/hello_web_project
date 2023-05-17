import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/submit', methods=['POST'])
def post_hello():
    name = request.form['name']
    message = request.form['message']

    return f'Thanks {name}, you sent this message: "{message}" '
#run (curl -X POST -d "name=Leo&message=Hello world" http://127.0.0.1:5000/submit)

@app.route('/submit', methods=['GET'])
def get_name():
    name = request.args['name']
    return f"I am waving at {name}"
#run(curl "http://127.0.0.1:5000/submit?name=Leo")

@app.route('/count_vowels', methods=['POST'])
def post_vowel_count():
    text = request.form['text']
    vowels = "aeiou"
    count = sum(1 for i in text if i in vowels)
    return f'There are {count} vowels in "{text}"'
#run (curl -X POST -d "text=eee" http://127.0.0.1:5000/count_vowels)

@app.route('/sort-names', methods=['POST'])
def post_sort_names():
    if 'names' not in request.form:
        return 'Please provide some names', 400
    names = request.form['names'].split(',')
    return ','.join(sorted(names))

@app.route('/names', methods=['GET'])
def get_names():
    predefined_names = ["Julia", "Alice", "Karim"]
    add_name = request.args['add_name'].split(',')
    result = ', '.join(predefined_names + add_name)
    return result

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

