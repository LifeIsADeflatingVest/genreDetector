from flask import Flask, render_template, request, jsonify
from scriptWebFile import classify_text

app = Flask(__name__)

@app.route('/classify', methods=['POST'])
def process_array():
    data = request.get_json()
    my_array = data.get('submittedArray', [])
    print("Length of my_array is:", len(my_array))
    print("First element of my_array is:", my_array[0])
    average_score = classify_text(my_array)
    return jsonify(average_score)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8999)

